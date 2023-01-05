import sqlite3


def login(log, password, signal) -> bool:
    con = sqlite3.connect('handler/users.db')
    cur = con.cursor()

    cur.execute(f'SELECT * FROM users WHERE login="{log}";')
    value = cur.fetchall()

    if value and value[0][2] == password:
        signal.emit("Успешная авторизация!")
        cur.close()
        con.close()
        return True
    else:
        signal.emit('Проверьте правильность ввода данных!')
        cur.close()
        con.close()
        return False


def register(log, password, signal) -> bool:
    con = sqlite3.connect('handler/users.db')
    cur = con.cursor()

    cur.execute(f'SELECT * FROM users WHERE login="{log}";')
    value = cur.fetchall()

    if value:
        signal.emit('Пользователь под таким никнеймом уже существует!')
        cur.close()
        con.close()
        return True
    else:
        cur.execute(f"INSERT INTO users (login, password) VALUES ('{log}', '{password}');")
        signal.emit('Успешная регистрация!')
        con.commit()
        cur.close()
        con.close()
        return False
