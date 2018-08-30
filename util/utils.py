def int_list_to_int(int_list):
    # e.g: take 'f' from '0xf' and left fill with '0'
    _str = ''.join([hex(i)[2:].zfill(2) for i in int_list])
    return int(_str, 16)



if __name__ == '__main__':
    assert int_list_to_int([39, 15]) == 9999
