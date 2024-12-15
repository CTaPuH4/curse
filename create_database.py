import sqlite3


def db_create():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()

    cursor.execute('PRAGMA foreign_keys = ON;')

    # Создание таблицы "Сборочная единица"
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Сборочная_единица (
            KSE INTEGER PRIMARY KEY,
            stat FLOAT,
            delta FLOAT,
            Z_H FLOAT,
            N_HE FLOAT,
            N_H0 FLOAT,
            Z_epsilon FLOAT,
            aW FLOAT,
            t FLOAT,
            epsilon_alpha FLOAT,
            epsilon_beta FLOAT,
            V FLOAT,
            U FLOAT,
            n FLOAT,
            SigmaH FLOAT,
            W_Ht FLOAT,
            Ft FLOAT,
            K_HV FLOAT,
            W_HV FLOAT,
            sigmaHP FLOAT,
            sigma_HP FLOAT,
            T1 FLOAT
        )
    ''')

    # Создание таблицы "Деталь" с внешним ключом
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Деталь (
            KD INTEGER PRIMARY KEY,
            deltaH FLOAT,
            K_HL FLOAT,
            Z_M FLOAT,
            b_w FLOAT,
            beta FLOAT,
            m FLOAT,
            z1 FLOAT,
            z2 FLOAT,
            d_w1 FLOAT,
            g0 FLOAT,
            K_Halpha FLOAT,
            K_Hbeta FLOAT,
            KSE INTEGER,
            FOREIGN KEY (KSE) REFERENCES Сборочная_единица (KSE)
        )
    ''')

    # Подтверждение изменений и закрытие соединения
    conn.commit()
    conn.close()

    print("Таблицы успешно созданы.")
