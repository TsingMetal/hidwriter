import sys


def int_list_to_int(int_list):
    ''' 
    convert a integer list to a hex string list,
    then convert the hex string list to a integer    
    '''
    # int list to hex string list
    hex_str_list = [hex(i)[2:].zfill(2) for i in int_list]
    # cancat the hex_str_list into a string
    _str = ''.join(hex_str_list)

    return int(_str, 16)


def str_to_int_list(_str, length=8):
    ''' convert a string(user input) to a int_list '''

    if _str.isdigit():
        _int = int(_str)
        # left padded with 0 to the required length
        hex_str = hex(_int)[2:].zfill(length)
        print(hex_str) # fordebug
    else:
        hex_str = _str + '0' * (length - len(_str))

    # each sub group contains 2 character
    hex_str_list = [hex_str[i: i+2] for i in range(0, length, 2)]
    print(hex_str_list) # fordebug

    int_list = [int(i, 16) for i in hex_str_list]
    print(int_list) # for debug

    return int_list


def verify_arg(
        max_len=5, cmd='command', isnum=True
    ):

    help_str = '''
Usage:python %s <param>
e.g.: python %s %s''' 
    help_str = help_str % (cmd, cmd, '8' * max_len)

    if len(sys.argv) != 2 or \
            len(sys.argv[1].lstrip('0')) > max_len \
            or (sys.argv[1].isdigit() != isnum):
        print("FAIL! Proper parameter needed")
        print(help_str)
        sys.exit(-1) # import to exit

    return sys.argv[1]


if __name__ == '__main__':
    # simle test:

    assert int_list_to_int([0, 0, 39, 15]) == 9999

    assert str_to_int_list('9999', length=8) == [0, 0, 39, 15]

    expected = [int('ab', 16), int('cd', 16), 
            int('ef', 16), int('ff',16)] + [0] * 26
    res = str_to_int_list('abcdefff', length=60)
    assert res == expected
