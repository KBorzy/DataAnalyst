from check_correct_time import check_correct_time

def overheating_periods(logs):
    if len(logs) > 0:
        logs = check_correct_time(logs)

        periods = 0
        current_period = False
        if logs is not None:
            for i in range(1, len(logs)):
                temp1 = float(logs[i - 1].split()[2][:-1])
                temp2 = float(logs[i].split()[2][:-1])

                if temp1 <= 100 and temp2 > 100:
                    current_period = True
                    periods += 1
                elif temp1 > 100 and temp2 <= 100:
                    current_period = False

            return periods
        else:
            return 0
    else:
        return 0
