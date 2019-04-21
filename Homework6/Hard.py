# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла
import os


class Worker:
    def __init__(self, name, surname, salary, position, norm_hours):
        self.name = name
        self.surname = surname
        self._salary = int(salary)
        self.position = position
        self.norm_hours = int(norm_hours)
        self.work_hours = 0

    def read_work_hours(self):
        with open(f'{cur_dir()}/data/hours_of', 'r', encoding='UTF-8') as f:
            for i in f.readlines():
                if i.split()[0] == self.name and i.split()[1] == self.surname:
                    self.work_hours = int(i.split()[2])
                    break
                else:
                    continue

    def calculate(self):
        h_pay = int(self._salary / self.norm_hours)

        if self.work_hours == self.norm_hours:
            calc_salary = f'{self._salary}'
        elif self.work_hours > self.norm_hours:
            calc_salary = f'{self._salary + (self.work_hours - self.norm_hours) * h_pay * 2}'
        else:
            calc_salary = f'{h_pay * self.work_hours}'
        return calc_salary

    def write_salary(self):
        with open(f'{cur_dir()}/data/all_salary', 'a', encoding='UTF-8') as f:
            f.write(f"{self.name:<15}{self.surname:<15}{self.calculate():<15}\n")
            f.write('\n')


def cur_dir():
    return os.path.dirname(os.path.abspath(__file__))


def file_handle(file):
    with open(file, 'r', encoding='UTF-8') as f:
        for i in f.readlines():
            if i.count('Имя') == 1:
                continue
            else:
                name, surname, salary, position, norm_hours = i.split()
                worker = Worker(name, surname, salary, position, norm_hours)
                worker.read_work_hours()
                worker.write_salary()


file_handle(f'{cur_dir()}/data/workers')
