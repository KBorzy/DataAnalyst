from time_elapse import time_elapse
from check_correct_time import check_correct_time


def czas_trwania(logi):
    valid_logs = check_correct_time(logi)
    if valid_logs is not None:
        # czas trwania raportu
        start_time_str = ''
        end_time_str = ''
        for log in valid_logs:
            log = log.split()[:2]
            if not start_time_str:
                start_time_str = ' '.join(log)
            end_time_str = ' '.join(log)
        return time_elapse(start_time_str, end_time_str)
    else:
        return 0
