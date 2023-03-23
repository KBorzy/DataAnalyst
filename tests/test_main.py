import pytest
from .. import main
import json


def test_generuj_raport():
    src = "./tests/test_input.txt"
    expected_output = {
        "wadliwe_logi": [
            "2023-x1-01 23:5x 10xC",
            "2023-01-02 00:15 -78C",
            "2023-01-02 01:10"
        ],
        "procent_wadliwych_logow": "30.0",
        "czas_trwania_raportu": 120,
        "temperatura": {
            "max": "115.3",
            "min": "90.0",
            "srednia": "102.4"
        },
        "najdluzszy_czas_przegrzania": 40,
        "liczba_okresow_przegrzania": 2,
        "problemy": {
            "wysoki_poziom_zaklocen_EM": True,
            "wysokie_ryzyko_uszkodzenia_silnika_z_powodu_temperatury": True
        }
    }

    assert main.generuj_raport(src) == expected_output


def test_generuj_raport_empty():
    src = "./tests/test_input_empty.txt"
    expected_output = {
        "wadliwe_logi": [],
        "procent_wadliwych_logow": "100.0",
        "czas_trwania_raportu": 0,
        "temperatura": {
            "max": None,
            "min": None,
            "srednia": None
        },
        "najdluzszy_czas_przegrzania": 0,
        "liczba_okresow_przegrzania": 0,
        "problemy": {
            "wysoki_poziom_zaklocen_EM": False,
            "wysokie_ryzyko_uszkodzenia_silnika_z_powodu_temperatury": False
        }
    }

    assert main.generuj_raport(src) == expected_output


def test_generuj_raport_single():
    src = "./tests/test_input_single.txt"
    expected_output = {
        "wadliwe_logi": [],
        "procent_wadliwych_logow": "0.0",
        "czas_trwania_raportu": 0,
        "temperatura": {
            "max": '90C',
            "min": '90C',
            "srednia": '90C'
        },
        "najdluzszy_czas_przegrzania": 0,
        "liczba_okresow_przegrzania": 0,
        "problemy": {
            "wysoki_poziom_zaklocen_EM": False,
            "wysokie_ryzyko_uszkodzenia_silnika_z_powodu_temperatury": False
        }
    }

    assert main.generuj_raport(src) == expected_output


