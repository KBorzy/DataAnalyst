# https://github.com/KBorzy/ProjektZaliczeniowy
# Krzysztof Borzyszkowski

from check_log import check_log
from check_time import czas_trwania
from check_temp import sprawdz_temperatury
from longest_overheating import time_overheating
from overheating_periods import overheating_periods
import json


def generuj_raport(src):
    wadliwe_logi = []
    procent_wadliwych_logow = '100.0'
    procent_wadliwych_logow_float = 0.0
    czas_trwania_raportu = 0
    temperatura_max_str = None
    temperatura_min_str = None
    temperatura_avg_str = None
    najdluzszy_czas_przegrzania = 0
    liczba_okresow_przegrzania = 0
    problemy = {
        'wysoki_poziom_zaklocen_EM': False,
        'wysokie_ryzyko_uszkodzenia_silnika_z_powodu_temperatury': False
    }

    with open(src, 'r') as plik:
        liczba_logow = 0
        liczba_wadliwych_logow = 0
        poprawne_logi = []
        for linia in plik:
            liczba_logow += 1

            if check_log(linia):
                wadliwe_logi.append(linia)
                liczba_wadliwych_logow += 1
            else:
                poprawne_logi.append(linia)

        if liczba_wadliwych_logow > 0:
            procent_wadliwych_logow_float = (liczba_wadliwych_logow / liczba_logow) * 100
            procent_wadliwych_logow_float = round(procent_wadliwych_logow_float,1)
            procent_wadliwych_logow = str(procent_wadliwych_logow_float)
        if liczba_wadliwych_logow == 0 and len(poprawne_logi) > 0:
            procent_wadliwych_logow = "0.0"
        for i in range(len(wadliwe_logi)):
            wadliwe_logi[i] = wadliwe_logi[i].strip()

    czas_trwania_raportu = czas_trwania(poprawne_logi)

    if len(poprawne_logi) > 0:
        temperatury = sprawdz_temperatury(poprawne_logi)
        temperatura_min = temperatury['min_temp']
        temperatura_max = temperatury['max_temp']
        temperatura_avg = temperatury['avg_temp']
        temperatura_min_str = str(temperatura_min)
        temperatura_max_str = str(temperatura_max)
        temperatura_avg_str = str(temperatura_avg)
        najdluzszy_czas_przegrzania = time_overheating(poprawne_logi)
        liczba_okresow_przegrzania = overheating_periods(poprawne_logi)

    if procent_wadliwych_logow_float > 10:
        problemy['wysoki_poziom_zaklocen_EM'] = True

    if najdluzszy_czas_przegrzania > 10:
        problemy['wysokie_ryzyko_uszkodzenia_silnika_z_powodu_temperatury'] = True

    raport = {
        "wadliwe_logi": wadliwe_logi,
        "procent_wadliwych_logow": procent_wadliwych_logow,
        "czas_trwania_raportu": czas_trwania_raportu,
        "temperatura": {
            "max": temperatura_max_str,
            "min": temperatura_min_str,
            "srednia": temperatura_avg_str
        },
        "najdluzszy_czas_przegrzania": najdluzszy_czas_przegrzania,
        "liczba_okresow_przegrzania": liczba_okresow_przegrzania,
        "problemy": {
            "wysoki_poziom_zaklocen_EM": problemy['wysoki_poziom_zaklocen_EM'],
            "wysokie_ryzyko_uszkodzenia_silnika_z_powodu_temperatury": problemy[
                'wysokie_ryzyko_uszkodzenia_silnika_z_powodu_temperatury']
        }
    }

    return raport
