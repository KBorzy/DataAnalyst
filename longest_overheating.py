from time_elapse import time_elapse


def time_overheating(logs):
    overheat_dict = {}
    for log in logs:
        date_time = ' '.join(log.split()[0:2])
        temperature = log.split()[2]
        if float(temperature[:-1]) > 100:
            date = date_time.split()[0]
            time = date_time.split()[1]
            if date not in overheat_dict:
                overheat_dict[date] = [time, time]
            else:
                if time < overheat_dict[date][0]:
                    overheat_dict[date][0] = time
                elif time > overheat_dict[date][1]:
                    overheat_dict[date][1] = time

    time_elapsed = 0
    for date in overheat_dict:
        start_time_str = date + ' ' + overheat_dict[date][0]
        end_time_str = date + ' ' + overheat_dict[date][1]
        time_elapsed += time_elapse(start_time_str, end_time_str)

    return time_elapsed
