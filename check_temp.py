def sprawdz_temperatury(logi):
    temperatury = []
    for log in logi:
        log = log.split()
        temperatura = log[2].rstrip("C")
        temperatury.append(float(temperatura))

    min_temp = min(temperatury)
    max_temp = max(temperatury)
    avg_temp = round(sum(temperatury) / len(temperatury), 1)

    mapa_temperatur = dict()
    mapa_temperatur["min_temp"] = min_temp
    mapa_temperatur["max_temp"] = max_temp
    mapa_temperatur["avg_temp"] = avg_temp

    return mapa_temperatur
