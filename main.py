from check_log import check_log
from check_time import czas_trwania
from check_temp import sprawdz_temperatury


def generuj_raport(src):
    wadliwe_logi = []
    procent_wadliwych_logow = 100.0
    czas_trwania_raportu = 0
    temperatura_max = None
    temperatura_min = None
    temperatura_avg = 0.0
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
    temperatury = sprawdz_temperatury(poprawne_logi)
    temperatura_min = temperatury['min_temp']
    temperatura_max = temperatury['max_temp']
    temperatura_avg = temperatury['avg_temp']


generuj_raport("./przyklady/przyklad3.txt")
