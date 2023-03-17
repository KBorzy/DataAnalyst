from datetime import datetime, timedelta

def time_elapse(start, end):
    start_datetime = datetime.strptime(start, "%Y-%m-%d %H:%M")
    end_datetime = datetime.strptime(end, "%Y-%m-%d %H:%M")
    timedelta = end_datetime - start_datetime
    total_minutes = timedelta.total_seconds() / 60
    return int(total_minutes)