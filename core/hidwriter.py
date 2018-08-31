import platform


'''
class HIDWriter(object):

    def __init__(self):
        if 'Windows' in platform.platform():
            from core.winhidwriter import HIDWriter as writer
        else: # for linux platform
            from core.linuxhidwriter import HIDWriter as writer

        self.writer = writer()


    def read(self):
        return self.writer.read()

    def write(self, raw_data):
        return self.writer.write(raw_data)

    def close(self):
        self.writer.close()
'''

if platform.system() == 'Windows':
    from core.winhidwriter import main
else:
    from core.linuxhidwriter import main
