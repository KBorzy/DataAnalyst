
def check_temperatures(logs):
    if len(logs) > 1:
        temperatures = []
        for log in logs:
            log = log.split()
            temperature = log[2].rstrip("C")
            temperatures.append(float(temperature))

        min_temp = min(temperatures)
        max_temp = max(temperatures)
        avg_temp = round(sum(temperatures) / len(temperatures), 1)

        temperature_map = dict()
        temperature_map["min_temp"] = min_temp
        temperature_map["max_temp"] = max_temp
        temperature_map["avg_temp"] = avg_temp

        return temperature_map
    elif len(logs) == 1:
        temperatures = []

        log = logs[0]
        log = log.split()
        temperature = log[2].rstrip("C")
        temperatures.append(float(temperature))

        min_temp = log[2]
        max_temp = log[2]
        avg_temp = log[2]

        temperature_map = dict()
        temperature_map["min_temp"] = min_temp
        temperature_map["max_temp"] = max_temp
        temperature_map["avg_temp"] = avg_temp

        return temperature_map
    else:
        return None
