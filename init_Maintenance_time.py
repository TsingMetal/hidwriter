import os.path

from util.cmd_data import INIT_MAINTENANCE_TIME_CMD

from core.hidwriter import main


if __name__ == '__main__':
    main(
        cmd=os.path.basename(__file__),
        send_list=INIT_MAINTENANCE_TIME_CMD,
        max_len=8,
        hex_len=8,
        isnum=True
    )
