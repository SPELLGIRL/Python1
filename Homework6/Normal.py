# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.


class Person:
    fullname: str

    def __init__(self, fullname):
        self.fullname = fullname


class Student(Person):
    mother: Person
    father: Person
    __classroom: str

    def __init__(self, fullname, mother=None, father=None):
        super().__init__(fullname)
        self.mother = mother
        self.father = father
        self.__classroom = ''

    @property
    def classroom(self):
        return self.__classroom

    def get_parents(self):
        return f'{self.fullname} --> Мама: {self.mother.fullname if self.mother else "не указана"}, Папа: {self.father.fullname if self.father else "не указан"}'

    def set_classroom(self, classroom, distribution):
        if self in distribution.classroom_student[classroom]:
            self.__classroom = classroom
        else:
            print('Student not fined in distribution')


class Teacher(Person):
    __disciplines: list
    __classrooms: list

    def __init__(self, fullname):
        super().__init__(fullname)
        self.__disciplines = list()
        self.__classrooms = list()

    @property
    def discipline(self):
        return self.__disciplines

    def set_discipline(self, discipline, distribution):
        if distribution.discipline_teacher[discipline] == self:
            self.__disciplines.append(discipline)
        else:
            print('Error discipline')


class Distribution:
    def __init__(self):
        self.discipline_teacher = dict()
        self.classroom_discipline = dict()
        self.classroom_student = dict()

    def add_discipline_teacher(self, discipline, teacher):
        if discipline not in self.discipline_teacher.keys():
            self.discipline_teacher[discipline] = teacher
            teacher.set_discipline(discipline, self)
        else:
            print('Discipline have a teacher')

    def add_classroom_discipline(self, classroom, discipline):
        if classroom not in self.classroom_discipline.keys():
            self.classroom_discipline[classroom] = [discipline]
        elif discipline not in self.classroom_discipline[classroom]:
            self.classroom_discipline[classroom].append(discipline)
        else:
            print('Discipline repeat')

    def add_classroom_student(self, classroom, student):
        try:
            self.classroom_student[student.classroom].remove(student)
        except KeyError:
            pass
        if classroom not in self.classroom_student.keys():
            self.classroom_student[classroom] = [student]

        elif student not in self.classroom_student[classroom]:
            self.classroom_student[classroom].append(student)

        student.set_classroom(classroom, self)

    def get_all_classrooms(self):
        return list(self.classroom_student.keys())

    def get_all_students_in_classroom(self, classroom):
        return [x.fullname for x in self.classroom_student[classroom]]

    def get_student_info(self, student):
        teachers = []
        classroom_student = student.classroom
        disciplines = self.classroom_discipline[classroom_student]
        for x in disciplines:
            teachers.append(f'{self.discipline_teacher[x].fullname}: {x}')
        return f'{student.fullname} --> {classroom_student}', teachers

    def all_teachers_in_classroom(self, classroom):
        return [self.discipline_teacher[x].fullname for x in
                self.classroom_discipline[classroom]]


if __name__ == '__main__':
    dist_2019 = Distribution()
    current_distribution = dist_2019
    vasechkin = Student('Vasechkin V.V.')
    current_distribution.add_classroom_student('7A', vasechkin)
    ivanov = Student('Ivanov I.I.')
    current_distribution.add_classroom_student('7A', ivanov)
    petrov = Student('Petrov P.P.')
    current_distribution.add_classroom_student('7Б', petrov)
    sidorov = Student('Sidorov S.S')
    current_distribution.add_classroom_student('9A', sidorov)
    current_distribution.add_classroom_student('9B', sidorov)
    mr_Doe = Teacher('Doe J.J.')
    current_distribution.add_discipline_teacher('mathematic', mr_Doe)
    current_distribution.add_classroom_discipline('7A', 'mathematic')
    mr_Smith = Teacher('Smith J.J.')
    current_distribution.add_discipline_teacher('physics', mr_Smith)
    current_distribution.add_classroom_discipline('7A', 'physics')
    ivanova = Person('Ivanova I.I.')
    ivanov_f = Person('Ivanov I.I.')
    ivanov.mother = ivanova
    ivanov.father = ivanov_f

    # Выбранная и заполненная данными структура должна решать следующие задачи:
    # 1. Получить полный список всех классов школы
    print(
        f'1. Получить полный список всех классов школы:\n{current_distribution.get_all_classrooms()}\n')

    # 2. Получить список всех учеников в указанном классе
    #  (каждый ученик отображается в формате "Фамилия И.О.")
    print(
        f'2. Получить список всех учеников в указанном классе:\n{current_distribution.get_all_students_in_classroom("7A")}\n')

    # 3. Получить список всех предметов указанного ученика
    #  (Ученик --> Класс --> Учителя --> Предметы)
    print('3. Получить список всех предметов указанного ученика')
    print(*current_distribution.get_student_info(ivanov), sep=' --> ', end='\n\n')

    # 4. Узнать ФИО родителей указанного ученика
    print(f'4. Узнать ФИО родителей указанного ученика:\n{ivanov.get_parents()}\n')

    # 5. Получить список всех Учителей, преподающих в указанном классе
    print(
        f'5. Получить список всех Учителей, преподающих в указанном классе:\n{current_distribution.all_teachers_in_classroom("7A")}')
