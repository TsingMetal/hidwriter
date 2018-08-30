import time

import pywinusb.hid as hid

from util.utils import int_list_to_int
from util.cmd_data import COUNTER_CMD


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

    def read(self):
        '''
        read the input from HID device
        '''
        self.dev.set_raw_data_handler(self._handle_raw_data)
        self.write(COUNTER_CMD)
        self.count_limit = None 
        while True: # wait variants to be inited
            if self.count_limit != None:
                break

        return self.basc_data

    def write(self, send_list):
        self.reports[0].set_raw_data(send_list)
        result = self.reports[0].send() 
        return result

    def close(self):
        self.dev.close()

    def _handle_raw_data(self, data):
        print(data[1:]) # fordebug
        print(data[35: 43]) # fordebug
        self.count = int_list_to_int(data[1:5]) # index 0 ignored
        self.fixture_id = ''.join([str(i) for i in data[5:35]])
        self.maintenance_time = int_list_to_int(data[35:39])
        self.maintenance_count = ''.join([str(i) for i in data[43:47]])
        self.count_limit = ''.join([str(i) for i in data[47:51]])
        self.basc_data = '''
Count=%d\nFixture_ID=%s\nMaintenance_time=%s\n\
Maintenance_count=%s\nCount_limit=%s
        ''' \
        % (self.count, self.fixture_id, self.maintenance_time,
                self.maintenance_count, self.count_limit)



if __name__ == '__main__':
    writer = HIDWriter()
    writer.read()
    raw_data = [0, 1, 1] + [0] * 64
    writer.write(raw_data)
