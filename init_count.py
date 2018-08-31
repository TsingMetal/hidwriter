import os.path

from core.hidwriter import main

from util.cmd_data import INIT_COUNT_CMD


if __name__ == '__main__':
    main(
        cmd=os.path.basename(__file__),
        send_list=INIT_COUNT_CMD,
        max_len=6,
        hex_len=8,
        isnum=True
    )
