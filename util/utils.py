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

    _int = int(_str)
    # left padded with 0 to the required length
    hex_str = hex(_int)[2:].zfill(length)

    # each sub group contains 2 character
    hex_str_list = [hex_str[i: i+2] for i in range(0, length, 2)]

    int_list = [int(i, 16) for i in hex_str_list]

    return int_list


if __name__ == '__main__':
    # simle test:

    assert int_list_to_int([0, 0, 39, 15]) == 9999

    assert str_to_int_list('9999', length=8) == [0, 0, 39, 15]
