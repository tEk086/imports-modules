
from application import salary
from application.db import people
from datetime import datetime

date = datetime.today()

if __name__ == '__main__':
    salary.calculate_salary()
    people.get_employees()
    print(f'Today is: {date}')