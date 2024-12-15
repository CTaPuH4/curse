from calculate import db_calculate
from create_database import db_create
from input import db_input


def main():
    while True:
        print('Меню')
        print('1. Создать файл базы данных и таблицы')
        print('2. Ввести данные для расчёта')
        print('3. Провести расчёт по данным из таблицы')
        print('4. Выход')
        k = int(input())
        if k == 1:
            db_create()
        elif k == 2:
            print("\033c", end="")
            num = int(input('Введите код для нового расчёта:'))
            db_input(num)
        elif k == 3:
            print("\033c", end="")
            num = int(input('Введите код расчёта:'))
            db_calculate(num)
        else:
            return 0


main()
