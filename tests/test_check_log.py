import pytest
from .. import check_log as c

valid_log = '2023-01-01 23:00 90C'
invalid_log = '2023-01-01 23:50 10xC'


def test_check_log():
    # test with a valid input
    assert c.check_log("2023-03-22 10:30 95.xC") != None

    # test with a invalid input
    assert c.check_log("2023-03-22 10:30 -3C") != None

    # test with an invalid input that causes an exception
    assert c.check_log("invalid input") != None

    # test with an empty input
    assert c.check_log("") != None

def test_check_log_valid_input():
    assert c.check_log("2023-01-01 23:00 90C") == None