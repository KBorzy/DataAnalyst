from time_elapse import time_elapse


def czas_trwania(logi):
    if len(logi)>1:
        # czas trwania raportu
        start_time_str = ''
        end_time_str = ''
        for log in logi:
            log = log.split()[:2]
            if not start_time_str:
                start_time_str = ' '.join(log)
            end_time_str = ' '.join(log)
        return time_elapse(start_time_str, end_time_str)
    else:
        return 0
