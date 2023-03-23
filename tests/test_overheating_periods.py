import pytest
from .. import overheating_periods as op


def test_overheating_periods():
    logi = ['2023-01-01 23:00 90C',
            '2023-01-01 23:50 110C',
            '2023-01-02 00:10 95C',
            '2023-01-02 00:20 100.3C',
            '2023-01-02 00:40 115.3C',
            '2023-01-02 00:50 100.1C',
            '2023-01-02 01:00 106C',
            ]

    assert op.overheating_periods(logi) == 2
    assert op.overheating_periods([]) == 0

    logi = ['2023-01-01 23:00 105C']

    assert op.overheating_periods(logi) == 1
