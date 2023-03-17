from check_log import check_log
from check_time import czas_trwania

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
