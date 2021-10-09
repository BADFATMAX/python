# запуск через терминал - пример ниже
# python main.py 8

# импортирую модуль
import argparse

# список, который будет содержать все мои ряды
P = []

parser = argparse.ArgumentParser(
    description="Building the Pascal Pyramid")  # добавляю парсер и вкратце описываю его работу
parser.add_argument('numRows', type=int,
                    help="The number of rows")  # при помощи этого метода описываю переменную numRows для кол-ва рядов
args = parser.parse_args()  # метод для парсинга аргументов

num = args.numRows

# цикл для подсчёта нового ряда
for i in range(num):
    row = [1] * (i + 1)  # первый элемент
    for j in range(i + 1):
        if j != 0 and j != i:  # индекс j не соотвецтвует граничным значениям
            row[j] = P[i - 1][j - 1] + P[i - 1][j]  # для неграничного лемента нового ряда беру сумму 2 верних значений
    P.append(row)  # соотвецтвенно добавляю ряд в наш список

""" for i in P:
     print(i) """


# это функция для красивого вывода моей пирамиды
def draw():
    mmax = len(' '.join(map(str, P[-1])))  # последний элемент (в мап первым аргументом передаю функцию как объект)
    for f in P:
        print(' '.join(map(str, f)).center(mmax) + '\n')


print(draw())