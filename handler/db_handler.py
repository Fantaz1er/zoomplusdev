import sqlite3


def login(log: str, password: str, signal) -> bool:
    successful_auth = False
    con = sqlite3.connect('handler/users.db')
    cur = con.cursor()

    cur.execute(f'SELECT * FROM users WHERE login="{log}";')
    value = cur.fetchall()

    if value and value[0][2] == password:
        successful_auth = True
        signal.emit("Успешная авторизация!")
    else:
        signal.emit('Проверьте правильность ввода данных!')

    cur.close()
    con.close()

    return successful_auth


def register(log: str, password: str, signal) -> bool:
    successful_auth = False
    con = sqlite3.connect('handler/users.db')
    cur = con.cursor()

    cur.execute(f'SELECT * FROM users WHERE login="{log}";')
    value = cur.fetchall()

    if value:
        signal.emit('Пользователь под таким никнеймом уже существует!')
    else:
        successful_auth = True
        cur.execute(f"INSERT INTO users (login, password) VALUES ('{log}', '{password}');")
        signal.emit('Успешная регистрация!')
        con.commit()

    cur.close()
    con.close()

    return successful_auth
