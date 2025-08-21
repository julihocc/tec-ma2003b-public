import logging
from utils import setup_logger


def test_setup_logger_stream(tmp_path, capsys):
    logger = setup_logger("test_logger", level=logging.DEBUG)
    logger.debug("debug-message")
    captured = capsys.readouterr()
    # StreamHandler writes to stderr by default; check both streams
    assert "debug-message" in (captured.out + captured.err)


def test_setup_logger_file(tmp_path):
    logfile = tmp_path / "test.log"
    logger = setup_logger("test_file_logger", level=logging.INFO, logfile=str(logfile))
    logger.info("info-file")
    logger.handlers[0].flush()
    with open(logfile, "r") as fh:
        content = fh.read()
    assert "info-file" in content
