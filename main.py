import re
from datetime import datetime, time, date, timedelta


def check_log(linia):
    try:
        match = re.match(r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2})\s+([0-9]+\.?[0-9]*C)$', linia.strip())
        if match:
            data_str, temp_str = match.groups()
            data = datetime.strptime(data_str, "%Y-%m-%d %H:%M")
            temp = float(temp_str[:-1])
            if temp <= 0:
                return True
        else:
            return True
    except:
        return True

def czas_trwania(logi):
    # czas trwania raportu
    start_time_str = ''
    end_time_str = ''
    for log in logi:
        data, czas, temperatura = log.split()
        if not start_time_str:
            start_time_str = czas
        end_time_str = czas

    start_time = datetime.strptime(start_time_str, "%H:%M").time()
    end_time = datetime.strptime(end_time_str, "%H:%M").time()

    delta_hours = (end_time.hour - start_time.hour) % 24
    delta_minutes = (end_time.minute - start_time.minute) % 60
    total_minutes = abs(delta_hours * 60 + delta_minutes)
    return total_minutes

def generuj_raport(src):
    wadliwe_logi = []
    procent_wadliwych_logow = 100.0
    czas_trwania_raportu = 0
    temperatura_max = None
    temperatura_min = None
    temperatura_suma = 0.0
    liczba_pomiarow_temperatury = 0
    najdluzszy_czas_przegrzania = 0
    liczba_okresow_przegrzania = 0
    wysoki_poziom_zaklocen_EM = False
    wysokie_ryzyko_uszkodzenia_silnika = False

    with open(src, 'r') as plik:
        liczba_logow = 0
        liczba_wadliwych_logow = 0
        poprawne_logi = []
        for linia in plik:
            liczba_logow += 1
            # szukamy wadliwe logi
            if check_log(linia):
                wadliwe_logi.append(linia)
                liczba_wadliwych_logow += 1
            else:
                poprawne_logi.append(linia)

        if liczba_wadliwych_logow > 0:
            procent_wadliwych_logow = (liczba_wadliwych_logow / liczba_logow) * 100

        czas_trwania_raportu = czas_trwania(poprawne_logi)

    print(wadliwe_logi)
    print(procent_wadliwych_logow)
    print(czas_trwania_raportu)


generuj_raport("./przyklady/przyklad3.txt")
