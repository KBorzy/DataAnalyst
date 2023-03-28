import pytest
from .. import check_time as c
from .. import time_elapse

logs = ['2023-01-01 23:00 90C',
        '2023-01-01 23:50 100C',
        '2023-01-01 00:45 102C',
        '2023-01-01 01:00 105C'
        ]


def test_report_duration():
    assert c.report_duration([]) == 0
    assert c.report_duration(['2023-01-01 23:00 90C']) == 0


def tast_valid_report_duration():
    assert c.report_duration(logs) == time_elapse.time_elapse('2023-01-01 23:00', '2023-01-01 01:00')
