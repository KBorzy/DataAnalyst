import re
from datetime import datetime
def check_log(linia):
    try:
        match = re.match(r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2})\s+([0-9]+\.?[0-9]*C)$', linia.strip())
        if match:
            data_str, temp_str = match.groups()
            data = datetime.strptime(data_str, "%Y-%m-%d %H:%M")
            temp = float(temp_str[:-1])
            if temp <= 0:
                return True
        else:
            return True
    except:
        return True