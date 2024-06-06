from datetime import datetime
import time


def calculate_salary(employees_list: list) -> str:
    time.sleep(1)  # imitation working process
    date_time = str(datetime.now())[:-7]
    return f'{date_time} {employees_list} salary calculated successfully'
