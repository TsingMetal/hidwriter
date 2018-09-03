import os.path

from core.hidwriter import write

from util.cmd_data import INIT_COUNT_CMD


if __name__ == '__main__':
    write(
        cmd=os.path.basename(__file__),
        send_list=INIT_COUNT_CMD
    )
