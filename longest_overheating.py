from datetime import datetime
from time_elapse import time_elapse


def calculate_overheating_period(logs):
    periods = {}
    start_time = ''

    for log in logs:

        date, time, temperature = log.split()
        date_time = datetime.strptime(date + ' ' + time, '%Y-%d-%m %H:%M')
        current_time = date_time.strftime('%Y-%d-%m %H:%M')

        if float(temperature[:-1]) > 100:
            if not start_time:
                start_time = current_time
        else:
            if start_time:
                period_duration = time_elapse(start_time, current_time)
                periods[f"period{len(periods) + 1}"] = period_duration
                start_time = ''

        if start_time:
            periods[f"period{len(periods) + 1}"] = time_elapse(start_time, current_time)

    result = max(periods.values(), default=0)
    return result