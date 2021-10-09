import argparse

"""
Эта функция проверяет размерность матрицы и ядра,
где ядро должно быть меньше матрицы
a1: высота матрицы
a2: высота ядра
b1: ширина матрицы
b2: ширина ядра
результат: функция скажет, что значения высоты или ширины ядра больше значений матрицы
"""


# raise формирует объект исключения
def num_status(a1, a2, b1, b2):
    if a2 > a1:
        raise ValueError('The value of the kernel height exceeds the height of the matrix')
    if b2 > b1:
        raise ValueError('The value of the kernel width exceeds the height of the matrix')


"""
Функция разделяет элементы списка на матрицу и ядро, создает значения высоты и ширины матриц
Пустой подсписк - [] - является разделителем для матрицы и ядра.
ln: Список списков значений собраных из фаила
mat1: Пустой список под матрицу
mat2: Пустой список под ядро
результат: Список содержащий значение матрицы и значения ядра
"""


def create_matrices(ln, mat1, mat2):
    flag = 1
    for i in ln:
        if not i:
            flag = 0
            continue
        if not flag:
            mat2.append(i)
        else:
            mat1.append(i)

    return mat1, mat2


"""
Данная функция производ свертку матрицы
hm: Значение высоты матрицы
hk: Значение высоты ядра
wm: Значение ширины матрицы
wk: Значение ширины ядра
mat1: Список значений матрицы
mat2: Список значений ядра
mat3: Результирующая матрица (матрица свертки)
результат: Матрица свертки, ширина матрицы и ядра
"""


def convolution(hm, hk, wm, wk, mat1, mat2, mat3):
    for j in range(0, hm - hk + 1):
        for i in range(0, wm - wk + 1):
            summa = 0
            for k in range(0, wk):
                for m in range(0, hk):
                    summa += mat2[m][k] * mat1[m + j][k + i]
            mat3.append(summa)
    return mat3, wm, wk


def main():
    parser = argparse.ArgumentParser(description="Свёртка матрицы на ядро и выведение произведения свертки")
    parser.add_argument('inp', type=str, help='input path')
    parser.add_argument('out', type=str, help='output path')
    args = parser.parse_args()

    with open(args.inp) as f:
        ln = [[int(i) for i in line.strip().split()] for line in f]

    matrix1, matrix2, matrix3 = [], [], []

    create_matrices(ln, matrix1, matrix2)  # return mat1 mat2
    h1, h2 = len(matrix1), len(matrix2)
    w1, w2 = len(matrix1[0]), len(matrix2[0])
    num_status(h1, h2, w1, w2)

    convolution(h1, h2, w1, w2, matrix1, matrix2, matrix3)  # return mat3

    st = w1 - w2 + 1
    count = 0
    with open(args.out, 'w') as f:
        for i in matrix3:
            f.write(str(i) + " ")
            count += 1
            if count == st:
                f.write('\n')
                count = 0


# шаблон, для защиты пользователя от случайного вызова скрипта
if __name__ == '__main__':  # был ли фаил запущен напрямую
    main()
