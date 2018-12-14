import os.path

from core.hidwriter import write


if __name__ == '__main__':
    init_fixture_id_cmd = 0x21
    write(
        filename=os.path.basename(__file__),
        cmd=init_fixture_id_cmd,
        max_len=29,
        isnum=False
    )
