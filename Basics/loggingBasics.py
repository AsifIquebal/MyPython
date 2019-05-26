import logging

logging.basicConfig(filename="test.log", level=logging.DEBUG, format='(%ascitime)s:%(levelname)s')

def test_01():
    logging.debug("Debug level")


def test_02():
    logging.info("Info level")
