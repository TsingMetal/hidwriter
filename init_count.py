import os.path

from core.hidwriter import write


if __name__ == '__main__':
    init_count_cmd = [0x21]
    write(
        file_name=os.path.basename(__file__),
        cmd=init_count_cmd
    )
