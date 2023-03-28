from time_elapse import time_elapse
from check_correct_time import check_correct_time


def report_duration(logs):
    valid_logs = check_correct_time(logs)
    if valid_logs is not None:
        # Report duration
        start_time_string = ''
        end_time_string = ''
        for log in valid_logs:
            log = log.split()[:2]
            if not start_time_string:
                start_time_string = ' '.join(log)
            end_time_string = ' '.join(log)
        return time_elapse(start_time_string, end_time_string)
    else:
        return 0
