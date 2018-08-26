import usb


class HIDWriter(object):

    def __init__(self, vid=0x0483, pid=0x5750):
        self.handle = None
        self.vid = vid
        self.pid = pid

    def start(self):
        self.dev = usb.core.find(idVendor=self.vid, idProduct=self.pid)
        if self.dev != None:
            self.ep_in = self.dev[0][(0, 0)][0].bEndpointAddress
            self.ep_out = self.dev[0][(0, 0)][1].bEndpointAddress
            self.size = self.dev[0][(0, 0)][1].wMaxPacketSize
        self.open()
    
    def open(self):
        '''
        打开usb设备
        '''
        busses = usb.busses()
        for bus in busses:
            devices = bus.devices
            for device in devices:
                if device.idVendor == self.vid and device.idProduct == self.pid:
                    self.handle = device.open()

    def read(self, timeout=0):
        '''
        读取usb设备发过来的数据
        '''
        if self.handle:
            data = self.handle.interruptRead(self.ep_in, timeout)

        try:
            data_list = data.tolist()
            return data_list
        except:
            return list()
    
    def write(self, send_list, timeout=1000):
        '''
        发送数据给usb设备
        '''
        if self.handle:
            bytes_num = self.handle.interruptWrite(
                self.ep_out, send_list, timeout)
            return bytes_num
        
    def stop(self):
        '''
        停止，关闭usb设备，释放接口
        '''
        self.alive = False
        if self.handle:
            self.handle.releaseInterface()


if __name__ == '__main__':
    import time
    dev = usbHelper()

    dev.start()

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
