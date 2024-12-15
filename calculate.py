import sqlite3


conn = sqlite3.connect('base.db')
cursor = conn.cursor()


def db_calculate(num):
    cursor.execute('SELECT STAT FROM Сборочная_единица WHERE KSE = ?', (num,))
    values = cursor.fetchall()
    values = [kse[0] for kse in values]
    if values == []:
        print('Расчёт с таким номером не найден')
        return 0
    result = values[0]
    if result == 0:
        print('Результат расчёта = Отрицательный')
    else:
        print('Результат расчёта = Положительный')
