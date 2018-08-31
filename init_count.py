'''
import os.path
import sys
import time

from util.cmd_data import INIT_COUNT_CMD
from util.utils import str_to_int_list, verify_arg
from core.hidwriter import HIDWriter

def main(
        cmd='cmd',
        raw_data=None, max_len=8,
        isnum=True
    ):
    writer = HIDWriter()

    arg = \
        verify_arg(
                max_len=max_len//2, 
                cmd=cmd, 
                isnum=isnum
        )

    # convert the arg to a list of integers 
    arg_list = str_to_int_list(arg, length=max_len)
        
    raw_data[3: (max_len // 2) + 3] = arg_list
    print(raw_data) # fordebug

    result = writer.write(raw_data)
    if result:
        print('write OK')
        time.sleep(0.5)
    else:
        print('FAILED')

    writer.close()


if __name__ == '__main__':
    cmd = os.path.basename(__file__)
    main(cmd, INIT_COUNT_CMD, 12, True)
'''

from core.hidwriter import main

from util.cmd_data import INIT_COUNT_CMD

main('cmd', INIT_COUNT_CMD, 8, True)
