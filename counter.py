import time

from cmd_data import COUNTER_CMD

from hidwriter import HIDWriter


if __name__ == '__main__':
    raw_data = COUNTER_CMD

    writer = HIDWriter()
    writer.read()
    writer.write(raw_data)
    time.sleep(0.5)
    writer.close()
