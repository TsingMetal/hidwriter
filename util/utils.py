import sys


def int_list_to_int_str(int_list):
    ''' 
    convert a integer list to a hex string list,
    then convert the hex string list to a int string    
    '''
    # int list to hex string list
    hex_str_list = [hex(i)[2:].zfill(2) for i in int_list]
    # concat the hex_str_list into a string
    _str = ''.join(hex_str_list)

    return str(int(_str, 16))

def int_list_to_str(int_list):
    '''
    convert a list of ints a string
    '''
    if len(int_list) < 8:
        return int_list_to_int_str(int_list)

    str_list = [chr(i) for i in int_list]
    _str = ''.join(str_list)
    return _str.strip('\x00')

def str_to_int_list(_str, isnum=True):
    ''' convert a string(user input) to a int_list '''

    if isnum:
        _int = int(_str)
        # left padded with 0 to the required length
        hex_str = hex(_int)[2:].zfill(8)
        # each sub group contains 2 character
        hex_str_list = [hex_str[i: i+2] for i in range(0, 8, 2)]
        int_list = [int(i, 16) for i in hex_str_list]
    else:
        int_list = [ord(i) for i in _str]

    return int_list


def verify_arg(max_len=6, filename='command', isnum=True):

    help_str = '''
Usage: python %s <%s>
e.g.:  python %s %s
    ''' 
    if isnum:
        _range = '0~' + '9' * max_len
        eg = '8' * max_len
    else:
        _range = '0' * 30 + '~' +  'z' * 30
        eg = '0123456789abcdef'

    help_str = help_str % (cmd, _range, cmd, eg)

    if len(sys.argv) != 2:
        print('ONE ARGUMENT NEEDED!')
        print(help_str)
    elif len(sys.argv[1].lstrip('0')) > max_len:
        print('ARGUMENT TOO LONG!')
        print(help_str)
    elif isnum == True and not sys.argv[1].isdigit():
        print('ONLY NUMBERS ALLOWED!')
        print(help_str)
    else:
        return sys.argv[1]


if __name__ == '__main__':
    # simle tests:

    assert int_list_to_int_str([0, 0, 39, 15]) == 9999

    assert str_to_int_list('9999', length=8) == [0, 0, 39, 15]

    expected = [int('ab', 16), int('cd', 16), 
            int('ef', 16), int('ff',16)] + [0] * 26
    res = str_to_int_list('abcdefff', hex_len=60)
    assert res == expected
