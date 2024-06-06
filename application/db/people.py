import time


def get_employees(database: dict) -> list:
    time.sleep(3)  # imitation working process
    employees_list = []
    for value in database.values():
        if not type(value) == list:
            employees_list.append(value)
        else:
            for i in value:
                employees_list.append(i)
    return employees_list
