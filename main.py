from application import salary
from application.db import people
from application.db import database
import PySimpleGUI as sg
import time


def main():
    employees_list = people.get_employees(database.database)

    progress_frame = [[sg.ProgressBar(100, orientation='h', size=(50, 10), key='progressbar')]]
    output_frame = [[sg.Output(size=(76, 20))]]

    layout = [
        [sg.Frame('Progress', layout=progress_frame)],
        [sg.Frame('Output', layout=output_frame)],
        [sg.Submit('Start'), sg.Cancel()]
    ]

    window = sg.Window('Домашнее задание к лекции 1. «Import. Module. Package»', layout)
    progressbar = window['progressbar']

    while True:
        event, values = window.read(timeout=10)
        if event == 'Cancel' or event is None:
            break
        elif event == 'Start':
            start = time.time()
            incr = round(100 / len(employees_list))
            for i, item in enumerate(employees_list):
                print(salary.calculate_salary(item))
                progressbar.UpdateBar(incr + i * incr)
            end = time.time()
            print(f'All works done. Elapsed time: {(end - start):.7f}')

    window.close()


if __name__ == '__main__':
    main()






