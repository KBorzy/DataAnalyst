def sprawdz_temperatury(logi):
    if len(logi) > 1:
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
    elif len(logi) == 1:
        temperatury = []

        log = logi[0]
        log = log.split()
        temperatura = log[2].rstrip("C")
        temperatury.append(float(temperatura))

        min_temp = log[2]
        max_temp = log[2]
        avg_temp = log[2]

        mapa_temperatur = dict()
        mapa_temperatur["min_temp"] = min_temp
        mapa_temperatur["max_temp"] = max_temp
        mapa_temperatur["avg_temp"] = avg_temp

        return mapa_temperatur
    else:
        return None
