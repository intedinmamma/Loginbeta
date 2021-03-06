import sqlite3

_connection = sqlite3.connect('People.db')
_connection.row_factory = lite.Row


def add(nick, rfid):
    cursor = _connection.cursor()
    cursor.execute("INSERT INTO People VALUES (?,?,?,?,?);", (rfid, nick_temp, 1, 0, time.time()))
    return cursor.lastrowid


def logout(rfid):
    cursor = _connection.cursor()
    cursor.execute('UPDATE People SET totalTime=totalTime + (strftime("%s", "now") - lastLogin), isHere=0 WHERE blipId=?', [rfid])


def login(rfid):
    cursor = _connection.cursor()
    cursor.execute('UPDATE People SET lastLogin=strftime("%s", "now"), isHere=1 WHERE blipId=?', [rfid])


def fetch(rfid):
    cursor = _connection.cursor()
    cursor.execute("SELECT * FROM People WHERE blipId = ?", [rfid])
    return cursor.fetchone()


def logged_in():
	cursor = _connection.cursor()
	cursor.execute("SELECT * FROM People WHERE isHere = 1")
	return cursor.fetchall()


def highscore():
	cursor = _connection.cursor()
	cursor.execute("SELECT * FROM People ORDER BY totalTime DESC")
	return cursor.fetchall()


def logout_all():
	cursor = _connection.cursor()
    cursor.execute("UPDATE People SET isHere = 0")
