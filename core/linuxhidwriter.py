import sys

import usb

from util.cmd_data import COUNTER_CMD
from util.utils import int_list_to_int
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
        self.count = int_list_to_int(data[0:4]) # index 0 ignored
        self.fixture_id = ''.join([str(i) for i in data[4:34]])
        self.maintenance_time = int_list_to_int(data[34:38])
        self.maintenance_count = ''.join([str(i) for i in data[42:46]])
        self.count_limit = ''.join([str(i) for i in data[46:50]])
        self.basc_data = '''
Count=%d\nFixture_ID=%s\nMaintenance_time=%s\n\
Maintenance_count=%s\nCount_limit=%s
        ''' \
        % (self.count, self.fixture_id, self.maintenance_time,
                self.maintenance_count, self.count_limit)

        return self.basc_data


def main(
        cmd='cmd',
        raw_data=None, max_len=8,
        isnum=True
    ):
    writer = HIDWriter()

    arg = \
        verify_arg(
                max_len=max_len//2, 
                cmd=cmd, 
                isnum=isnum
        )

    # convert the arg to a list of integers 
    arg_list = str_to_int_list(arg, length=max_len)
        
    raw_data = raw_data[1:] # different from Windows
    raw_data[2: (max_len // 2) + 2] = arg_list
    print('linux raw_data:\n',raw_data) # fordebug

    result = writer.write(raw_data)
    if result:
        print('write OK')
    else:
        print('FAILED')

    writer.close()


if __name__ == '__main__':
    import os.path
    from util.cmd_data import INIT_COUNT_CMD
    cmd = os.path.basename(__file__)
    main(cmd, INIT_COUNT_CMD, 8, True)
