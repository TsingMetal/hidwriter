import os.path

from util.cmd_data import INIT_MAINTENANCE_TIME_CMD

from init_count import main

if __name__ == '__main__':
    cmd = os.path.basename(__file__)
    main(cmd, INIT_MAINTENANCE_TIME_CMD, 16, True)