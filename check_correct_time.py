from datetime import datetime


def check_correct_time(logi):
    if len(logi) > 1:
        last_time_str = logi[0].split()[0] + ' ' + logi[0].split()[1]
        valid_logs = []
        for log in logi:
            log_time_str = log.split()[0] + ' ' + log.split()[1]
            last_time = datetime.strptime(last_time_str, '%Y-%m-%d %H:%M')
            log_time = datetime.strptime(log_time_str, '%Y-%m-%d %H:%M')
            if last_time_str is None or log_time >= last_time:
                valid_logs.append(log)
                last_time_str = log_time_str
            else:
                continue
        if len(valid_logs) > 1:
            return valid_logs
        else:
            return []

    else:
        return logi
