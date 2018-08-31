import os.path

from util.cmd_data import INIT_COUNT_LIMIT_CMD

from core.hidwriter import main


if __name__ == '__main__':
    cmd = os.path.basename(__file__)
    main(cmd, INIT_COUNT_LIMIT_CMD, 8, True)
