import pytest
from .. import longest_overheating as lo


def test_calculate_overheating_period():
    logs = ['2023-01-01 23:00 90C',
            '2023-01-01 23:50 110C',
            '2023-01-02 00:10 95C',
            '2023-01-02 00:20 100.3C',
            '2023-01-02 00:40 115.3C',
            '2023-01-02 00:50 100.1C',
            '2023-01-02 01:00 106C']

    expected_result = 40

    assert lo.calculate_overheating_period(logs) == expected_result

    logs = ['2023-01-01 23:00 102C']

    assert lo.calculate_overheating_period(logs) == 0

    logs = ['2023-01-01 23:00 102C',
            '2023-01-01 23:30 105C']

    assert lo.calculate_overheating_period(logs) == 30

    assert lo.calculate_overheating_period([]) == 0
