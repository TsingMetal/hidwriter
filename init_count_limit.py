import os.path

from core.hidwriter import write


if __name__ == '__main__':
    INIT_COUNT_LIMIT_CMD = 0x25
    write(
        filename=os.path.basename(__file__),
        cmd=INIT_COUNT_LIMIT_CMD,
    )
