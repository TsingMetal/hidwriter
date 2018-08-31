import sys

import usb

from util.cmd_data import COUNTER_CMD
from util.utils import int_list_to_int


class HIDWriter(object):

    def __init__(self, vid=0x0483, pid=0x5750):

        self.dev = usb.core.find(idVendor=vid, idProduct=pid)
        if self.dev != None:
            self.ep_in = self.dev[0][(0, 0)][0].bEndpointAddress
            self.ep_out = self.dev[0][(0, 0)][1].bEndpointAddress

            if self.dev.is_kernel_driver_active(0):
                self.dev.detach_kernal_driver(0)
        else:
            print("the HID devices is not found")
            sys.exit(-1)
    
    def read(self):
        self.write(self.ep_out, COUNTER_CMD[1:], timeout=3000)
        data = dev.read(self.ep_in, 64, timeout=3000)
        try:
            data_list = data.tolist()
            basc_data = self._handle_raw_data(data_list)
            return basc_data
        except:
            print("read data failed!")
    
    def write(self, send_list):
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


        

if __name__ == '__main__':
    import time
    dev = HIDWriter()

    send_list = [0x01, 0x01] + [0x00] * 62
    dev.write(send_list)
    # time.sleep(0.25)
    while True:
        try:
            mylist = dev.read()
            print mylist
            if mylist:
                break
        except:
            dev.stop()
            break
    dev.stop()
