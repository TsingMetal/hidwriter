import time

from core.hidwriter import HIDWriter


if __name__ == '__main__':
    writer = HIDWriter()
    print(writer.read())
    time.sleep(0.5)
    writer.close()
