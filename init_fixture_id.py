import os.path

from util.cmd_data import INIT_FIXTURE_ID_CMD

from init_count import main


if __name__ == '__main__':
    cmd = os.path.basename(__file__)
    main(cmd, INIT_FIXTURE_ID_CMD, 60, False)
