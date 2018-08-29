import sys
import time

from cmd_data import INIT_COUNT_CMD
from hidwriter import HIDWriter


if __name__ == '__main__':
    raw_data = INIT_COUNT_CMD
    writer = HIDWriter()

    arg = sys.argv[1]
    raw_data[3:7] = [int(i, 16) for i in arg]

    writer.write(raw_data)
    writer.close()
    time.sleep(0.5)
