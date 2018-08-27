import usb


class HIDWriter(object):

    def __init__(self, vid=0x0483, pid=0x5750):

        self.dev = usb.core.find(idVendor=vid, idProduct=pid)
        if self.dev != None:
            self.ep_in = self.dev[0][(0, 0)][0].bEndpointAddress
            self.ep_out = self.dev[0][(0, 0)][1].bEndpointAddress
        else:
            print("the HID devices is not found")
    
    def read(self):
        data = dev.read(self.ep_in, 64, timeout=5000)
        try:
            data_list = data.tolist()
            print(data_list)
            return data_list
        except:
            print("read data failed!")
    
    def write(self, send_list):
        bytes_num = self.dev.write(self.ep_out, send_list, timeout=5000)
        print(bytes_num)
        return bytes_num

    def close(self):
        ''' not implemented '''
        pass
        

if __name__ == '__main__':
    import time
    dev = HIDWriter()

    send_list = [0xAA for i in range(64)]
    dev.write(send_list)
    # time.sleep(0.25)
    while True:
        try:
            mylist = dev.read()
            print mylist
            if mylist[1] == 0x02:
                break
        except:
            dev.stop()
            break
    dev.stop()
