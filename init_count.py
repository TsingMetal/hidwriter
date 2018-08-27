import sys

from cmd_data import init_count_cmd
from hidwriter import HIDWriter


if __name__ == '__main__':
    raw_data = init_count_cmd
    writer = HIDWriter()

    arg = sys.argv[1]
    raw_data[2:6] = [int(i, 16) for i in arg]

    writer.write(raw_data)
    writer.close()
