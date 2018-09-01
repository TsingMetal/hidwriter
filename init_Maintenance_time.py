import os.path
import sys

from util.cmd_data import INIT_MAINTENANCE_TIME_CMD

from core.hidwriter import main


if __name__ == '__main__':
    try:
        assert len(sys.argv[1]) == 8
    except:
        print('PROVIDE A PROPER DATE!')
        print('e.g.: 20180901')
        sys.exit(-1)

    main(
        cmd=os.path.basename(__file__),
        send_list=INIT_MAINTENANCE_TIME_CMD,
        max_len=8,
        hex_len=8,
        isnum=True
    )
