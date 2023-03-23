from datetime import datetime
from time_elapse import time_elapse


def time_overheating(logs):
    # tworzymy słownik z okresami przegrzania
    okresy = {}

    # pobranie godziny rozpoczęcia przegrzania
    czas_start = ''
    # przechodzimy po wszystkich logach
    for log in logs:
        # rozbijamy log na poszczególne elementy
        data, godzina, temperatura = log.split()
        data_godzina = datetime.strptime(data + ' ' + godzina, '%Y-%d-%m %H:%M')
        czas = data_godzina.strftime('%Y-%d-%m %H:%M')
        # jeżeli temperatura jest powyżej 100C to zapamiętujemy godzinę rozpoczęcia przegrzania
        if float(temperatura[:-1]) > 100:
            if not czas_start:
                czas_start = czas
        # jeżeli temperatura jest równa lub poniżej 100C, to zapisujemy okres w słowniku
        else:
            if czas_start:
                czas_trwania = time_elapse(czas_start, czas)
                okresy[f"okres{len(okresy) + 1}"] = czas_trwania
                czas_start = ''

        # jeżeli mamy ostatni okres przegrzania, który nie został dodany do słownika, to dodajemy go
        if czas_start:
            okresy[f"okres{len(okresy) + 1}"] = time_elapse(czas_start, czas)
    # zwracamy największą wartość z słownika
    result = max(okresy.values(), default=0)
    return result
