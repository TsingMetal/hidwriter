import platform

if 'Windows' in platform.platform():
    from core.winhidwriter import HIDWriter as writer
    from core.winhidwriter import main
else: # for linux platform
    from core.linuxhidwriter import HIDWriter as writer
    from core.linuxhidwriter import main


class HIDWriter(object):

    def __init__(self):
        self.writer = writer()

    def read(self):
        return self.writer.read()

    def write(self, raw_data):
        return self.writer.write(raw_data)

    def close(self):
        self.writer.close()
