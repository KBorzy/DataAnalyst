import pytest
from .. import check_temp as c


def test_check_temperatures():
    logs = ['2023-01-01 23:00 90C',
            '2023-01-01 23:50 110C',
            '2023-01-02 00:10 95C',
            '2023-01-02 00:20 100.3C',
            '2023-01-02 00:40 115.3C',
            '2023-01-02 00:50 100.1C',
            '2023-01-02 01:00 106C',
            ]
    temperature_map = c.check_temperatures(logs)

    assert temperature_map["min_temp"] == 90.0
    assert temperature_map["max_temp"] == 115.3
    assert temperature_map["avg_temp"] == 102.4

    logs = ['2023-01-01 23:00 90C']
    temperature_map = c.check_temperatures(logs)

    expected = {'avg_temp': '90C', 'max_temp': '90C', 'min_temp': '90C'}
    assert temperature_map == expected
