import logging
from pathlib import Path

from jvm import ClassFileReader, parse_class_file


def test_class_file_reader():
    with Path("data/Hello.class").open("rb") as f:
        reader = ClassFileReader(f)
        assert reader.next_u4() == int("0xCAFEBABE", 0)


def test_parse(caplog):
    caplog.set_level(logging.DEBUG)

    with Path("data/Hello.class").open("rb") as f:
        result = parse_class_file(f)
        assert result.magic == int("0xCAFEBABE", 0)
        assert len(result.constant_pool) == result.constant_pool_count - 1
