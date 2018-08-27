import platform


class HIDWriter(object):

    def __init__(self):
        if 'Windows' in platform.platform():
            from winhidwriter import HIDWriter as writer
        else: # for linux platform
            from linuxhidwriter import HIDWriter as writer

        self.writer = writer()


    def read(self):
        self.writer.read()

    def write(self, raw_data):
        self.writer.write(raw_data)

    def close(self):
        self.close()
