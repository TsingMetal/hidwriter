import os.path
import sys
import time

from util.cmd_data import INIT_COUNT_CMD
from util.utils import str_to_int_list, verify_arg
from core.hidwriter import HIDWriter

def main():
    raw_data = INIT_COUNT_CMD
    writer = HIDWriter()

    arg = sys.argv[1]
    verify_arg(
            arg, max_len=5, 
            cmd=os.path.basename(__file__), 
            isnum=True
    )

    # convert the arg to a list of integers 
    arg_list = str_to_int_list(arg, length=8)
        
    raw_data[3:7] = arg_list

    result = writer.write(raw_data)
    if result:
        print('write OK')
    time.sleep(0.5)
    writer.close()


if __name__ == '__main__':
    main()
