import pywinusb.hid as hid


class HIDWriter(object):

    def __init__(self, vid=0x0483, pid=0x5750):
        _filter = hid.HidDeviceFilter(vendor_id=vid, product_id=pid)
        devs = _filter.get_devices()
        self.dev = devs[0]
        self.dev.open()
        self.reports = self.dev.find_output_reports()

    def read(self):
        def handle_raw_data(data):
            print([hex(i).upper() for i in data[1:]])
        self.dev.set_raw_data_handler(handle_raw_data)

    def write(self, send_list):
        self.reports[0].set_raw_data(send_list)
        bytes_num = self.reports[0].send() 
        print(bytes_num)
        return bytes_num

    def close(self):
        self.dev.close()


if __name__ == '__main__':
    writer = HIDWriter()
    writer.read()
    raw_data = [0x00 for i in range(64)]
    writer.write(raw_data)
