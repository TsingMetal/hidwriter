import sys

import usb

from util.cmd_data import COUNTER_CMD
from util.utils import int_list_to_str


class HIDWriter(object):

    def __init__(self, vid=0x0483, pid=0x5750):

        self.dev = usb.core.find(idVendor=vid, idProduct=pid)
        if self.dev != None:
            self.ep_in = self.dev[0][(0, 0)][0].bEndpointAddress
            self.ep_out = self.dev[0][(0, 0)][1].bEndpointAddress

            if self.dev.is_kernel_driver_active(0):
                self.dev.detach_kernel_driver(0)
        else:
            print('Counter NOT FOUND')
            basc_data = '''
Count=%s\nFixture_ID=%s\nMaintenance_time=%s\n\
Maintenance_count=%s\nCount_limit=%s\nResult=0
            ''' % ('nah', 'nah', 'nah', 'nah', 'nah')
            open('counter.ini', 'w').write(basc_data.strip())
            sys.exit(-1)

        # 'unread' the invalid data
        self.dev.write(self.ep_out, COUNTER_CMD[1: 33], timeout=5000)
        self.dev.read(self.ep_in, 32, timeout=3000)

    def read(self):

        self.dev.write(self.ep_out, COUNTER_CMD[1:33], timeout=5000)
        data = self.dev.read(self.ep_in, 32, timeout=3000)
        try:
            data_list = data.tolist()
            basc_data = self._handle_raw_data(data_list)
            return basc_data
        except Exception as e:
            print(e)
            print("read data failed!")
            sys.exit(-1)
    
    def write(self, send_list):
        bytes_num = self.dev.write(self.ep_out, send_list, timeout=5000)
        # self.dev.read(self.ep_in, 64, timeout=3000)
        return bytes_num

    def close(self):
        ''' not implemented '''
        usb.util.release_interface(self.dev, 0)
        self.dev.attach_kernel_driver(0)

    def _handle_raw_data(self, data):
        count = int_list_to_str(data[32:36])
        fixture_id = int_list_to_str(data[1:30])
        maintenance_time = int_list_to_str(data[36:44])
        maintenance_count = int_list_to_str(data[44:48])
        count_limit = int_list_to_str(data[48:52])
        self.basc_data = '''
Count=%s\nFixture_ID=%s\nMaintenance_time=%s\n\
Maintenance_count=%s\nCount_limit=%s\nResult=1
        ''' \
        % (count, fixture_id, maintenance_time,
                maintenance_count, count_limit)

        return self.basc_data


if __name__ == '__main__':
    pass
