import re
from datetime import datetime
def check_log(log):
    try:
        match = re.match(r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2})\s+([0-9]+\.?[0-9]*C)$', log.strip())
        if match:
            data_str, temp_str = match.groups()
            temp = float(temp_str[:-1])
            if temp <= 0:
                return True
        else:
            return True
    except:
        return True