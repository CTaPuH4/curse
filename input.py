import sqlite3
import math


conn = sqlite3.connect('base.db')
cursor = conn.cursor()

table3 = {
    1: 1,
    2: 1.01,
    3: 1.03,
    4: 1.06,
    5: 1.1,
    6: 1.13,
    7: 1.15,
    8: 1.2,
}

table5 = {
    1: [800, 6],
    2: [800, 6],
    3: [900, 8],
    4: [1000, 10],
    5: [1100, 12],
    6: [1150, 12],
    7: [600, 1],
    8: [600, 1],
}

table10 = {
    1: [5, 1.76],
    2: [10, 1.74],
    3: [15, 1.71],
    4: [20, 1.67],
    5: [25, 1.62],
    6: [30, 1.56],
    7: [35, 1.50],
    8: [40, 1.42],
}

table11_1 = {
    5: 1,
    6: 1.01,
    7: 1.03,
    8: 1.05,
    9: 1.13,
}

table11_2 = {
    5: 1,
    6: 1.02,
    7: 1.05,
    8: 1.09,
    9: 1.16,
}

table11_3 = {
    5: 1.01,
    6: 1.03,
    7: 1.07,
    8: 1.13,
    9: 1.19,
}

table12 = {
    1: 0.014,
    2: 0.01,
    3: 0.004,
}

table13_1 = {
    5: 28,
    6: 38,
    7: 47,
    8: 56,
    9: 73,
}

table13_2 = {
    5: 31,
    6: 42,
    7: 53,
    8: 61,
    9: 82,
}

table13_3 = {
    5: 37,
    6: 48,
    7: 64,
    8: 73,
    9: 100,
}


def db_input(num):
    cursor.execute('SELECT KSE FROM Сборочная_единица')
    kse_values = cursor.fetchall()
    kse_values = [kse[0] for kse in kse_values]
    if num in kse_values:
        print('Ошибка. Такой номер расчёта уже существует')
        return 0

    print("\033c", end="")
    print('Выберите материал колеса:')
    print('1. Сталь 45')
    print('2. Сталь 50Г')
    print('3. Сталь 40Х')
    print('4. Сталь 40ХН')
    print('5. Сталь 20Х')
    print('6. Сталь 18ХГТ')
    print('7. Высокопрочный чугун')
    print('8. Стальное литьё')
    k = int(input())
    sigmalHP, N_H0 = table5[k]
    if k == 7:
        Z_M = 234
    else:
        Z_M = 274

    print("\033c", end="")
    print('Выберите вид зубьев:')
    print('1. Прямые без модификации')
    print('2. Прямые с модификацией')
    print('3. Косые')
    k1 = int(input())
    deltaH = table12[k1]
    if k1 != 3:
        K_Halpha = 1

    print("\033c", end="")
    print('Выберите угол наклона линии зуба beta, град:')
    print('1. 5')
    print('2. 10')
    print('3. 15')
    print('4. 20')
    print('5. 25')
    print('6. 30')
    print('7. 35')
    print('8. 40')
    beta, Z_H = table10[int(input())]

    print("\033c", end="")
    aW = int(input('Введите Межосевое расстояние aW, мм: '))

    print("\033c", end="")
    m = float(input('Введите Модуль зубчатого колеса m: '))

    print("\033c", end="")
    t = int(input('Введите Полное число часов работы передачи t-ч, часов: '))

    print("\033c", end="")
    pl = int(input('Введите норму плавности (от 5 до 9): '))
    if m < 3.5:
        g0 = table13_1[pl]
    elif m > 10:
        g0 = table13_3[pl]
    else:
        g0 = table13_2[pl]

    print("\033c", end="")
    z1 = int(input('Введите Число зубъев первого колеса z1: '))

    print("\033c", end="")
    z2 = int(input('Введите Число зубъев первого колеса z2: '))

    print("\033c", end="")
    print('Выберите Окружную скорость V: ')
    print('1. 2.5')
    print('2. 5')
    print('3. 10')
    k = int(input())
    if k == 1:
        V = 2.5
    elif k == 2:
        V = 5
    else:
        V = 10
    if k1 == 3:
        if k == 1:
            K_Halpha = table11_1[pl]
        elif k == 2:
            K_Halpha = table11_2[pl]
        else:
            K_Halpha = table11_3[pl]

    print("\033c", end="")
    u = int(input('Введите Передаточное число u: '))

    print("\033c", end="")
    n = int(input('Введите Частоту вращения n: '))

    print("\033c", end="")
    T1 = int(input('Крутящий момент на валу ведущего колеса T1: '))

    b_w = 1
    epsilon_beta = (b_w * math.sin(math.radians(beta)) / (3.14 * m))
    while epsilon_beta < 1.1:
        b_w += 1
        epsilon_beta = (b_w * math.sin(math.radians(beta)) / (3.14 * m))

    d_w1 = m * z1

    otn = b_w / d_w1
    if otn > 1.6:
        print('Слишком высокая относительная ширина колеса.'
              + '(Слишком маленькие модуль колеса и/или количество зубьев z2)')
        return 0
    elif otn < 0.2:
        print('Слишком низкая относительная ширина колеса.'
              + '(Слишком большие модуль колеса и/или количество зубьев z1)')
        return 0
    else:
        temp = int(otn // 0.2)
        K_Hbeta = table3[temp]

    epsilon_alpha = (1.88 - 3.2 * (1 / z1 + 1 / z2)
                     * math.cos(math.radians(beta)))
    Z_epsilon = math.sqrt(1 / epsilon_alpha)

    Ft = 2000 * T1 / d_w1
    W_HV = deltaH * g0 * V * math.sqrt(aW/u)
    K_HV = 1 + W_HV * b_w / (Ft * K_Halpha * K_Hbeta)
    W_HT = (Ft / b_w) * K_Halpha * K_Hbeta * K_HV

    sigmaH = Z_H * Z_M * Z_epsilon * math.sqrt(W_HT * (u + 1) / (d_w1 * u))

    N_HE = 60 * t * n
    K_HL = (N_H0 / N_HE) ** (1 / 6)

    sigmaHP = sigmalHP * K_HL

    delta = sigmaHP - sigmaH

    print("\033c", end="")
    if delta >= 0:
        stat = 1
    else:
        stat = 0

    cursor.execute('''
        INSERT INTO Деталь(KD, deltaH, K_HL, Z_M, b_w, beta, m, z1, z2, d_w1, g0, K_Halpha, K_Hbeta, KSE)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (num, deltaH, K_HL, Z_M, b_w, beta, m, z1, z2, d_w1, g0, K_Halpha, K_Hbeta, num))
    cursor.execute('''
        INSERT INTO Сборочная_единица(KSE, stat, delta, Z_H, N_HE, N_H0, Z_Epsilon, aW, t, epsilon_alpha, epsilon_beta, V, U, n, SigmaH, W_Ht, Ft, K_HV, W_HV, sigmaHP, sigma_HP, T1)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (num, stat, delta, Z_H, N_HE, N_H0, Z_epsilon, aW, t, epsilon_alpha, epsilon_beta, V, u, n, sigmaH, W_HT, Ft, K_HV, W_HV, sigmaHP, sigmalHP, T1))
    conn.commit()
