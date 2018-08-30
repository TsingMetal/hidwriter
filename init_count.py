import sys
import time

from util.cmd_data import INIT_COUNT_CMD
from util.utils import str_to_int_list
from core.hidwriter import HIDWriter

def main():
    help_str = '''
Usage: python init_count.py <num> (0-9999)
e.g.: python init_count.py 8888'''

    raw_data = INIT_COUNT_CMD
    writer = HIDWriter()

    arg = sys.argv[1]
    if len(sys.argv) != 2 or len(arg) > 5 or (not arg.isnumeric()):
        print('PLEASE INPUT PROPER ARGUEMENT!')
        print(help_str)
        return

    # convert the arg to a list of integer 
    arg_list = str_to_int_list(arg, 8)
        
    raw_data[3:7] = arg_list

    result = writer.write(raw_data)
    if result:
        print('write OK')
    time.sleep(0.5)
    writer.close()


if __name__ == '__main__':
    main()
