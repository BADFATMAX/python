import random

"""Функция для создания матрицы заполненой случайными значениями от -100 до 100,
высота и ширина матрицы зависит от значений в range"""


def creatarray():
    return [[random.randint(-100, 100) for d_ in range(4)] for c_ in range(4)]


"""Класс, который объединяет общую работу для Пупы и Лупы"""


class Worker:
    def __init__(self, type_w=None):
        self.__type_w = type_w
        self.__sum = -9999999999999

    def do_work(self, mat1_name, mat2_name):
        """

        :param mat1_name: путь к фаилу с первой сгенерированой матрицей
        :param mat2_name: путь к фаилу со второй сгенерированой матрицей
        :return: Результат разботы Пупы и Лупы, а имеено сложение или разность матриц
        """
        with open(mat1_name, 'r') as f:
            mat1 = [[int(i) for i in line.strip().split()] for line in f]

        with open(mat2_name, 'r') as f:
            mat2 = [[int(i) for i in line.strip().split()] for line in f]
        for i in range(len(mat1)):
            for j in range(len(mat2[0])):
                if self.__type_w == "Lupa_t":
                    mat1[i][j] = mat1[i][j] - mat2[i][j]
                elif self.__type_w == "Pupa_t":
                    mat1[i][j] = mat1[i][j] + mat2[i][j]
        summa = sum(sum(mat1, []))
        self.__sum = summa
        return mat1

    def get_sum(self):
        """
        :return: Свойство которое возвращает сумму всех значений матрицы
        """
        return self.__sum


class Lupa(Worker):
    def __init__(self, name="Lupa", _salary=0):
        self.__type_w = "Lupa_t"
        super().__init__(self.__type_w)
        self._name = name
        self._salary = _salary

    def take__salary(self, amount):
        self._salary = self._salary + amount

    def name(self):
        return self._name

    def salary(self):
        return self._salary


class Pupa(Worker):
    def __init__(self, name="Pupa", _salary=0):
        self.__type_w = "Pupa_t"
        super().__init__(self.__type_w)
        self._name = name
        self._salary = _salary

    def take__salary(self, amount):
        self._salary = self._salary + amount

    def name(self):
        return self._name

    def salary(self):
        return self._salary


class Accountant:
    def __init__(self, name="BOSS"):
        self._name = name
        self._dollars = 1000

    def __give__salary(self, worker):
        worker.take__salary(self._dollars)

    def good_worker(self, pupa, lupa):
        """
        :param pupa: объект класса Пупа
        :param lupa: объект класса Лупа
        :return: лучшего работника (объект), того кто получил большую сумму при работе с матрицей
        """
        if isinstance(pupa, Pupa):
            if isinstance(lupa, Lupa):
                pupas = pupa.get_sum()
                lupas = lupa.get_sum()
                if pupas > lupas:
                    self.__give__salary(pupa)
                    return pupa
                else:
                    self.__give__salary(lupa)
                    return lupa


matrix1 = creatarray()
matrix2 = creatarray()

with open('input.txt', 'w') as file:
    for row in matrix1:
        file.write(' '.join([str(a) for a in row]) + '\n')

with open('input2.txt', 'w') as file:
    for row in matrix2:
        file.write(' '.join([str(a) for a in row]) + '\n')

mat1 = "input.txt"
mat2 = "input2.txt"
worker1 = Lupa()
worker2 = Pupa()
boss = Accountant()
print(worker2.do_work(mat1, mat2))
print(worker1.do_work(mat1, mat2))
goodworker = boss.good_worker(worker2, worker1)
print(goodworker.get_sum(), goodworker.salary(), goodworker.name())
