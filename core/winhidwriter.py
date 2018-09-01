import sys
import time

import pywinusb.hid as hid

from util.utils import int_list_to_int_str, int_list_to_hex_str
from util.cmd_data import COUNTER_CMD
from util.utils import str_to_int_list, verify_arg


class HIDWriter(object):

    def __init__(self, vid=0x0483, pid=0x5750):

        _filter = hid.HidDeviceFilter(vendor_id=vid, product_id=pid)
        devs = _filter.get_devices()
        if len(devs) > 0:
            self.dev = devs[0]
            self.dev.open()
            self.reports = self.dev.find_output_reports()
        else:
            print("No HID devices found")
            sys.exit(-1)

    def read(self):
        '''
        read the input from HID device
        '''
        self.dev.set_raw_data_handler(self._handle_raw_data)
        self.write(COUNTER_CMD)
        # write twice to get the valid result(there is a 
        # bug in the usb device)
        self.write(COUNTER_CMD)
        self.basc_data = None 
        
        for i in range(5): # wait variants to be inited
            if self.basc_data != None:
                break
            time.sleep(0.1)

        return self.basc_data

    def write(self, send_list):
        self.reports[0].set_raw_data(send_list)
        result = self.reports[0].send() 
        return result

    def close(self):
        self.dev.close()

    def _handle_raw_data(self, data):
        self.count = int_list_to_int_str(data[1:5]) # index 0 ignored
        self.fixture_id = int_list_to_hex_str(data[5:20])
        self.maintenance_time = int_list_to_int_str(data[35:43])
        self.maintenance_count = int_list_to_int_str(data[43:47])
        self.count_limit = int_list_to_int_str(data[47:51])
        self.basc_data = '''
Count=%s\nFixture_ID=%s\nMaintenance_time=%s\n\
Maintenance_count=%s\nCount_limit=%s
        ''' \
        % (self.count, self.fixture_id, self.maintenance_time,
                self.maintenance_count, self.count_limit)


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
        
    send_list[3: len(arg_list)+3] = arg_list
    print('win send_list:\n', send_list) # fordebug

    result = writer.write(send_list)
    if result:
        print('write OK')
        time.sleep(0.5)
    else:
        print('FAILED')

    writer.close()


if __name__ == '__main__':
    import os.path
    from util.cmd_data import INIT_COUNT_CMD
    cmd = os.path.basename(__file__)
    main(cmd, INIT_COUNT_CMD, 8, True)
