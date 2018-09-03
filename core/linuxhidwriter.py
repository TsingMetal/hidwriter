import sys

import usb

from util.cmd_data import COUNTER_CMD
from util.utils import int_list_to_int_str, int_list_to_str
from util.utils import str_to_int_list, verify_arg


class HIDWriter(object):

    def __init__(self, vid=0x0483, pid=0x5750):

        self.dev = usb.core.find(idVendor=vid, idProduct=pid)
        if self.dev != None:
            self.ep_in = self.dev[0][(0, 0)][0].bEndpointAddress
            self.ep_out = self.dev[0][(0, 0)][1].bEndpointAddress

            if self.dev.is_kernel_driver_active(0):
                self.dev.detach_kernel_driver(0)
        else:
            print("the HID devices is not found")
            sys.exit(-1)
    
    def read(self):
        # 'unread' the invalid data
        self.write(COUNTER_CMD[1:])
        self.dev.read(self.ep_in, 64, timeout=3000)

        self.write(COUNTER_CMD[1:])
        print(COUNTER_CMD[1:]) # fordebug
        data = self.dev.read(self.ep_in, 64, timeout=3000)
        try:
            data_list = data.tolist()
            basc_data = self._handle_raw_data(data_list)
            return basc_data
        except:
            print("read data failed!")
    
    def write(self, send_list):
        # self.dev.reset()
        bytes_num = self.dev.write(self.ep_out, send_list, timeout=5000)
        return bytes_num

    def close(self):
        ''' not implemented '''
        pass

    def _handle_raw_data(self, data):
        print(data[:]) # fordebug
        print(data[34: 42]) # fordebug
        self.count = int_list_to_int_str(data[0:4]) # index 0 ignored
        self.fixture_id = int_list_to_str(data[4:34])
        self.maintenance_time = int_list_to_str(data[34:38])
        self.maintenance_count = int_list_to_int_str(data[42:46])
        self.count_limit = int_list_to_int_str(data[46:50])
        self.basc_data = '''
Count=%s\nFixture_ID=%s\nMaintenance_time=%s\n\
Maintenance_count=%s\nCount_limit=%s
        ''' \
        % (self.count, self.fixture_id, self.maintenance_time,
                self.maintenance_count, self.count_limit)

        return self.basc_data


def main(
        cmd='cmd',          # commands, i.e. file name
        send_list=None,      # data sent to hid device
        max_len=6,          # max length of argument allowed
        hex_len=8,          # the length of hex string
        isnum=True          # whether only numeric allowed
    ):

    arg = \
        verify_arg(
                max_len=max_len, 
                cmd=cmd, 
                isnum=isnum
        )
    if arg == None:
        return

    writer = HIDWriter()

    # convert the arg to a list of integers 
    arg_list = str_to_int_list(arg, hex_len=hex_len)
        
    send_list = send_list[1:] # different from Windows
    # argument starts from index 2
    send_list[2: (hex_len // 2) + 2] = arg_list
    print('linux send_list:\r\n',send_list) # fordebug

    result = writer.write(send_list)
    if result:
        print('write OK')
    else:
        print('FAILED')

    writer.close()


if __name__ == '__main__':
    import os.path
    from util.cmd_data import INIT_COUNT_CMD
    cmd = os.path.basename(__file__)
    main(cmd, INIT_COUNT_CMD, 6, 8, True)
