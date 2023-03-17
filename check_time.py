from datetime import datetime, time, date, timedelta

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