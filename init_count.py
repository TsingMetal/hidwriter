import sys

from cmd_data import INIT_COUNT_CMD
from hidwriter import HIDWriter

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

    int_arg = int(arg) # convert arg to int
    # convert int to hex str and left fill with zero
    hex_arg = hex(int_arg)[2:].zfill(8) 
    arg_list = []

    # divide the hex_arg into 4 sub strings and convent each to int 
    # and add each int to a list 
    # and put the list into the raw data to send
    for i in range(0, 8, 2):
        substr = hex_arg[i : i+ 2]
        arg_list.append(int(substr, 16))
    raw_data[3:7] = arg_list
    print(raw_data) # fordebug

    writer.write(raw_data)
    writer.close()


if __name__ == '__main__':
    main()
