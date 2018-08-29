import time

from cmd_data import counter_cmd

from hidwriter import HIDWriter


if __name__ == '__main__':
    raw_data = counter_cmd

    writer = HIDWriter()
    writer.read()
    writer.write(raw_data)
    time.sleep(0.5)
    writer.close()
