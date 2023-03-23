import pytest
from .. import time_elapse as te


def test_time_elapse():
    start = "2022-01-01 00:00"
    end = "2022-01-01 01:30"
    assert te.time_elapse(start, end) == 90

    start = "2022-03-01 10:15"
    end = "2022-03-02 12:30"
    assert te.time_elapse(start, end) == 1575

    start = "2022-04-01 09:00"
    end = "2022-04-01 10:59"
    assert te.time_elapse(start, end) == 119

    start = "2022-05-01 00:00"
    end = "2022-05-01 00:00"
    assert te.time_elapse(start, end) == 0

    start = "2022-06-01 12:00"
    end = "2022-05-01 12:00"
    assert te.time_elapse(start,end) == 0