import os.path

from util.cmd_data import INIT_MAINTENANCE_COUNT_CMD

from core.hidwriter import write


if __name__ == '__main__':
    write(
        cmd=os.path.basename(__file__),
        send_list=INIT_MAINTENANCE_COUNT_CMD,
    )
