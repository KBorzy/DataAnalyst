import pytest
from .. import check_temp as c


def test_sprawdz_temperatury():
    logi = ['2023-01-01 23:00 90C',
            '2023-01-01 23:50 110C',
            '2023-01-02 00:10 95C',
            '2023-01-02 00:20 100.3C',
            '2023-01-02 00:40 115.3C',
            '2023-01-02 00:50 100.1C',
            '2023-01-02 01:00 106C',
            ]
    mapa_temperatur = c.sprawdz_temperatury(logi)

    assert mapa_temperatur["min_temp"] == 90.0
    assert mapa_temperatur["max_temp"] == 115.3
    assert mapa_temperatur["avg_temp"] == 102.4

    logi = ['2023-01-01 23:00 90C']
    mapa_temperatur = c.sprawdz_temperatury(logi)

    assert mapa_temperatur is None
