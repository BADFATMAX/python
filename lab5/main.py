import pandas as pd


def main():
    """ Открытие csv фаилов """
    df1 = pd.read_csv('titanic_with_labels.csv', sep=' ')
    df2 = pd.read_csv('cinema_sessions.csv', sep=' ')

    """ Смена мужского пола на 1, а женского на 0 """
    df1["sex"] = df1["sex"].map(lambda x: 0 if x == "ж" or x == "Ж" or x == "Женщины" else x)
    df1["sex"] = df1["sex"].map(lambda x: 1 if x == "м" or x == "M" or x == "Мужчина" else x)
    df1 = df1.drop(df1[(df1['sex'] == '-') | (df1['sex'] == '"Не указан"')].index)

    """ Изменение NaN в номере ряда на максимальное значение ряда """
    maxValue = df1["row_number"].max()
    df1["row_number"] = df1["row_number"].fillna(maxValue)

    """ Фильтрация выпитой жидкости,
        найдено сроднее значение выпитой жидкости,
        которым заменили слишком большие значения и отрицательные """
    avg_liters = int(df1['liters_drunk'][(df1['liters_drunk'] >= 0) & (df1['liters_drunk'] <= 10)].mean())
    df1['liters_drunk'] = df1['liters_drunk'].apply(lambda x: x if 0 <= x <= 10 else avg_liters)

    """ Добавление 3х столбцов с фильтрацией по возрасту,
        а также удаление изначальное столбца возраста"""
    age_old = df1["age"].apply(lambda x: 1 if x > 50 else 0)
    age_adult = df1["age"].apply(lambda x: 1 if 18 <= x <= 50 else 0)
    age_kid = df1["age"].apply(lambda x: 1 if x < 18 else 0)
    df1.insert(4, 'age_old', age_old)
    df1.insert(4, 'age_adult', age_adult)
    df1.insert(4, 'age_kid', age_kid)
    df1 = df1.drop(["age"], axis=1)

    """ Определение хмельного напитка
        0: не хмельной
        1: хмельной """
    df1["drink"] = df1["drink"].map(lambda x: 0 if x == "Cola" or x == "Water" or x == "Fanta" else 1)

    """ Объединение таблиц по номеру чека в финальную таблицу
        (не через copy, чтобы была возможность менять значение в df1 и df2)
        А также распределение на утренний, вечерний или дневной сеанс
        (по значению, которое стоит на позиции часа) """
    df3 = pd.merge(df1, df2, on="check_number")

    df3["morning"] = df3["session_start"].map(
        lambda x: "Morning session" if x[0] == "0" or (x[0] == "1" and x[1] == "2") else "NaN")
    df3["day"] = df3["session_start"].map(lambda x: "Day session" if x[0] == "1" and "1" < x[1] < "9" else "NaN")
    df3["evening"] = df3["session_start"].map(
        lambda x: "Evening session" if x[0] == "2" or (x[0] == "1" and x[1] > "8") else "NaN")

    df3.to_csv('titanic_final.csv')

    """Раскомментируйте кусок кода нижи,
        чтобы быстро смотреть изменнения по столбцам
        во всём фаиле, не забудьте поменять print
        df(номер таблицы)[столбец]"""

    # with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    #     print(df3["evening"])

if __name__ == "__main__":
    main()