from cmd_data import counter_cmd

from hidwriter import HIDWriter


if __name__ == '__main__':
    raw_data = counter_cmd

    writer = HIDWriter()
    writer.write(raw_data)
    writer.read()
    writer.close()
