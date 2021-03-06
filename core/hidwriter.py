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
    print('read complete')
    print('saving...')
    open('counter.ini', 'w').write(basc_data.strip())
    print('saved')
    mywriter.close()

def write(
        filename='',          # commands, i.e. file name
        cmd=0x11,
        max_len=6,          # max length of argument allowed
        isnum=True          # whether only numeric allowed
    ):

    print('verifying argument...')
    arg = \
        verify_arg(
                max_len=max_len,
                filename=filename,
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
    arg_list = [cmd] + str_to_int_list(
            arg, isnum=isnum)
    mywriter.write(arg_list)

    mywriter.close()


if __name__ == '__main__':
    '''
    import os.path
    from util.cmd_data import INIT_COUNT_CMD

    mywriter = writer()

    cmd = os.path.basename(__file__)
    mywriter.write(cmd, INIT_COUNT_CMD, 6, 8, True)
    '''
