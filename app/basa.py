import sqlite3
conn = sqlite3.connect("db.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS myresume (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                  name TEXT UNIQUE,phone TEXT UNIQUE,gmail TEXT UNIQUE,telegram TEXT UNIQUE,viber TEXT UNIQUE,
                  geolocation TEXT UNIQUE,skils TEXT UNIQUE)""")
def create_dummy_data():
    cursor.execute("""INSERT INTO myresume VALUES (NULL,?,?,?,?,?,?,?)""",
                ("Max Kusiak", "+380 93 556 9394", "maxkusiak4@gmail.com", "Phone number: +380 93 556 9394, Nickname: @TheDragon_Prince",
                "+380 93 556 9394", "Ruska Polyana", "I know some programming languages: Python, C++, C#, JS."))
    conn.commit()
    # print("+")
# create_dummy_data()
# cursor.execute("""SELECT name FROM myresume""")
# print(cursor.fetchall())