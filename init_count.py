import os.path

from core.hidwriter import main

from util.cmd_data import INIT_COUNT_CMD


if __name__ == '__main__':
    cmd = os.path.basename(__file__)
    main('cmd', INIT_COUNT_CMD, 8, True)
