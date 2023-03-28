from check_log import check_log
from check_time import report_duration
from check_temp import check_temperatures
from longest_overheating import calculate_overheating_period
from overheating_periods import overheating_periods

def generate_report(src):
    invalid_logs = []
    invalid_logs_percentage = '100.0'
    invalid_logs_percentage_float = 0.0
    report_duration = 0
    max_temp_str = None
    min_temp_str = None
    avg_temp_str = None
    longest_overheating_period = 0
    number_of_overheating_periods = 0
    issues = {
        'high_EM_interference_level': False,
        'high_risk_of_engine_damage_due_to_temperature': False
    }

    with open(src, 'r') as file:
        number_of_logs = 0
        number_of_invalid_logs = 0
        valid_logs = []
        for line in file:
            number_of_logs += 1

            if check_log(line):
                invalid_logs.append(line)
                number_of_invalid_logs += 1
            else:
                valid_logs.append(line)

        if number_of_invalid_logs > 0:
            invalid_logs_percentage_float = (number_of_invalid_logs / number_of_logs) * 100
            invalid_logs_percentage_float = round(invalid_logs_percentage_float, 1)
            invalid_logs_percentage = str(invalid_logs_percentage_float)
        if number_of_invalid_logs == 0 and len(valid_logs) > 0:
            invalid_logs_percentage = "0.0"
        for i in range(len(invalid_logs)):
            invalid_logs[i] = invalid_logs[i].strip()

    report_duration = report_duration(valid_logs)

    if len(valid_logs) > 0:
        temperatures = check_temperatures(valid_logs)
        min_temp = temperatures['min_temp']
        max_temp = temperatures['max_temp']
        avg_temp = temperatures['avg_temp']
        min_temp_str = str(min_temp)
        max_temp_str = str(max_temp)
        avg_temp_str = str(avg_temp)
        longest_overheating_period = calculate_overheating_period(valid_logs)
        number_of_overheating_periods = overheating_periods(valid_logs)

    if invalid_logs_percentage_float > 10:
        issues['high_EM_interference_level'] = True

    if longest_overheating_period > 10:
        issues['high_risk_of_engine_damage_due_to_temperature'] = True

    report = {
        "invalid_logs": invalid_logs,
        "invalid_logs_percentage": invalid_logs_percentage,
        "report_duration": report_duration,
        "temperature": {
            "max": max_temp_str,
            "min": min_temp_str,
            "average": avg_temp_str
        },
        "longest_overheating_period": longest_overheating_period,
        "number_of_overheating_periods": number_of_overheating_periods,
        "issues": {
            "high_EM_interference_level": issues['high_EM_interference_level'],
            "high_risk_of_engine_damage_due_to_temperature": issues[
                'high_risk_of_engine_damage_due_to_temperature']
        }
    }

    return report
