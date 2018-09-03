import platform

if 'Windows' in platform.platform():
    from core.winhidwriter import HIDWriter as writer
else: # for linux platform
    from core.linuxhidwriter import HIDWriter as writer

from util.utils import str_to_int_list, verify_arg


def read():
    print('connecting to counter...')
    mywriter = writer()
    print('counter connected')
    basc_data = mywriter.read()
    print('reading...')
    print(basc_data)
    print('read completed')
    print('saving...\n')
    open('counter.ini', 'w').write(basc_data.strip())
    print('saved')
    mywriter.close()

def write(
        cmd='cmd',          # commands, i.e. file name
        send_list=None,     # data sent to hid device
        max_len=6,          # max length of argument allowed
        hex_len=8,          # the length of hex string
        isnum=True          # whether only numeric allowed
    ):

    print('verifying argument...')
    arg = \
        verify_arg(
                max_len=max_len,
                cmd=cmd,
                isnum=isnum
        )
    if arg == None:
        return
    print('verify OK')

    print('connecting to counter...')
    mywriter = writer()
    print('counter connected')

    print('writing...')
    # convert the arg to a list of integers
    arg_list = str_to_int_list(arg, hex_len=hex_len)

    # argument starts from index 2
    send_list[3: (hex_len // 2) + 3] = arg_list

    if 'Linux' in platform.platform():
        send_list = send_list[1:]

    result = mywriter.write(send_list)
    if result:
        print('write OK')
    else:
        print('write FAILED!')

    mywriter.close()



if __name__ == '__main__':
    import os.path
    from util.cmd_data import INIT_COUNT_CMD

    mywriter = writer()

    cmd = os.path.basename(__file__)
    mywriter.write(cmd, INIT_COUNT_CMD, 6, 8, True)
