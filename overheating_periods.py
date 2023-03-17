def overheating_periods(logs):
    dates = []
    count = 0
    for log in logs:
        date_time = ' '.join(log.split()[0:2])
        temperature = log.split()[2]
        if float(temperature[:-1]) > 100:
            date = date_time.split()[0]
            if date not in dates:
                dates.append(date)
                count = count + 1
    return count