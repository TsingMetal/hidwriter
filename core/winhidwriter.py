import sys
import time

import pywinusb.hid as hid

from util.cmd_data import COUNTER_CMD
from util.utils import int_list_to_str


class HIDWriter(object):

    def __init__(self, vid=0xCD12, pid=0xC001):

        _filter = hid.HidDeviceFilter(vendor_id=vid, product_id=pid)
        devs = _filter.get_devices()
        if len(devs) > 0:
            self.dev = devs[0]
            self.dev.open()
            self.reports = self.dev.find_output_reports()
        else:
            print('Counter NOT FOUND!')
            basc_data = '''
Count=%s\nFixture_ID=%s\nMaintenance_time=%s\n\
Maintenance_count=%s\nCount_limit=%s\nResult=0
            ''' % ('nah', 'nah', 'nah', 'nah', 'nah')
            open('counter.ini', 'w').write(basc_data.strip())
            sys.exit(-1)

        # write for the first time to ensure following writes succed
        self.write(COUNTER_CMD[:32] + [0x0D])
        time.sleep(1)

    def read(self):
        '''
        read the input from HID device
        '''
        prefix = [0x00, 0x1f]
        postfix = [0x0d]
        fixture_cmd = prefix + [0x11] + [0x00] * 29 + postfix
        count_cmd = prefix + [0x12] + [0x00] * 29 + postfix
        self.dev.set_raw_data_handler(self._handle_raw_data)
        self.write(fixture_cmd)
        time.sleep(1)
        # print('1 self.received_data:', self.received_data)
        fixture_id = int_list_to_str(self.received_data[3:32])
        # self.dev.set_raw_data_handler(self._handle_raw_data)
        self.write(count_cmd)
        time.sleep(1)
        # print('2 self.received_data:', self.received_data)
        count = int_list_to_str(self.received_data[3:7])
        maintenance_time = int_list_to_str(self.received_data[7:15])
        maintenance_count = int_list_to_str(self.received_data[15:19])
        count_limit = int_list_to_str(self.received_data[19:23])
        print('count: %s' % count)
        print('fixture_id:', fixture_id)
        print('maintenance_time: %s' % maintenance_time)
        print('maintenance_count: %s' % maintenance_count)
        print('count_limit: %s' % count_limit)
        
        
        '''
        print('data received:')
        print(self.data)
        time.sleep(1)
        print('second:', self.data)
        print('length of data:', len(self.data))
    
        print('sending data list:')
        print(COUNTER_CMD[:32] + [0x0D])
        '''

        self.basc_data = None 
        for i in range(5): # wait variants to be inited
            if self.basc_data != None:
                break
            time.sleep(0.1)

        return 'this is for test'

    def write(self, send_list):
        self.reports[0].set_raw_data(send_list[:32] + [0x0d])
        result = self.reports[0].send() 
        return result

    def close(self):
        self.dev.close()

    def _handle_raw_data(self, data):
        self.received_data = data
        # print(self.received_data)
        
        """
        count = int_list_to_str(data[32:36]) # index 0 ignored
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
        """


if __name__ == '__main__':
    pass
