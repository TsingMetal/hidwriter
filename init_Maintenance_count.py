import os.path

from util.cmd_data import INIT_MAINTENANCE_COUNT_CMD

from core.hidwriter import write


if __name__ == '__main__':
    INIT_MAINTENANCE_COUNT_CMD = 0x24
    write(
        filename=os.path.basename(__file__),
        cmd=INIT_MAINTENANCE_COUNT_CMD,
    )
