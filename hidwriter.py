class HIDWriter(object):

    def __init__(self, vid=0x0483, pid=0x5750):
        self.vid = vid
        self.pid = pid
