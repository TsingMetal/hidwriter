import sys
import time

import pywinusb.hid as hid

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
        send_list = [0x00, 0x1f, 0x11] + [0x00] * 29 + [0x0d]
        self.reports[0].set_raw_data(send_list)
        result = self.reports[0].send() 
        time.sleep(1)

    def read(self):
        '''
        read the input from HID device
        '''
        fixture_id_list = self.write([0x11])
        rest_list = self.write([0x12])
        fixture_id = int_list_to_str(fixture_id_list[3:32])
        count = int_list_to_str(rest_list[3:7])
        maintenance_time = int_list_to_str(rest_list[7:15])
        maintenance_count = int_list_to_str(rest_list[15:19])
        count_limit = int_list_to_str(rest_list[19:23])
        '''
        print('count: %s' % count)
        print('fixture_id:', fixture_id)
        print('maintenance_time: %s' % maintenance_time)
        print('maintenance_count: %s' % maintenance_count)
        print('count_limit: %s' % count_limit)
        '''

        basc_data = '''
Count=%s\nFixture_ID=%s\nMaintenance_time=%s\n\
Maintenance_count=%s\nCount_limit=%s\nResult=1
        ''' \
        % (count, fixture_id, maintenance_time,
                maintenance_count, count_limit)

        return basc_data

    def write(self, cmd):
        prefix = [0x00, 0x1f]
        postfix = [0x0d]
        send_list = prefix + cmd + [0x00] * (30-len(cmd)) + postfix
        self.dev.set_raw_data_handler(self._handle_raw_data)
        self.reports[0].set_raw_data(send_list)
        result = self.reports[0].send() 
        self.received_data = None
        for i in range(5):
            if self.received_data != None:
                break
            time.sleep(0.1)
        if not self.received_data or \
                self.received_data[2] != cmd[0] or \
                self.received_data[-1] != 0x50:
            print('write FAIL')

        return self.received_data

    def close(self):
        self.dev.close()

    def _handle_raw_data(self, data):
        self.received_data = data


if __name__ == '__main__':
    pass
