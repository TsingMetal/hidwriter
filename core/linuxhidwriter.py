import sys

import usb

from util.utils import int_list_to_str


class HIDWriter(object):

    def __init__(self, vid=0xcd12, pid=0xc001):

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

        self.write_status = []

        # 'unread' the invalid data
        send_list = [0x1f, 0x11] + [0x00] * 29 + [0x0d]
        self.dev.write(self.ep_out, send_list, timeout=5000)
        self.dev.read(self.ep_in, 32, timeout=3000)

    def read(self):

        fixture_id_list = self.write([0x11])
        rest_list = self.write([0x12])
        fixture_id = int_list_to_str(fixture_id_list[2:31])
        count = int_list_to_str(rest_list[2:6])
        maintenance_time = int_list_to_str(rest_list[6:14])
        maintenance_count = int_list_to_str(rest_list[14:18])
        count_limit = int_list_to_str(rest_list[18:22])

        basc_data = '''
Count=%s\nFixture_ID=%s\nMaintenance_time=%s\n\
Maintenance_count=%s\nCount_limit=%s\nResult=%d
        ''' \
        % (count, fixture_id, maintenance_time,
                maintenance_count, count_limit,
                min(self.write_status))

        return basc_data
    
    def write(self, cmd):
        prefix = [0x1f]
        postfix = [0x0d]
        send_list = prefix + cmd + [0x00] * (30-len(cmd)) + postfix
        bytes_num = self.dev.write(self.ep_out, send_list, timeout=5000)
        received_data = self.dev.read(self.ep_in, 32, timeout=3000)
        received_data = received_data.tolist()
        if not received_data or \
                received_data[1] != cmd[0] or \
                received_data[-1] != 0x50:
            self.write_status.append(0)
            print(hex(cmd[0]) + ' write FAIL')
        else:
            self.write_status.append(1)
            print(hex(cmd[0]) + ' write OK')

        return received_data

    def close(self):
        usb.util.release_interface(self.dev, 0)
        self.dev.attach_kernel_driver(0)


if __name__ == '__main__':
    pass
