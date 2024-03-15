import sqlite3
con = sqlite3.connect('users.db')
cursor = con.cursor()

#sql - язык запросов
cursor.execute('''
create table if not exists users(
    id integer primary key autoincrement,
    login text,
    password text,
    age integer
)
''')
s = "adfsdfgsdg"
#cursor.execute('insert into users (login, password, age) values ("user10", "1234sgsdgsdg5", 22)')
#con.commit()

#cursor.execute('update users set password="0948572305" where login = "user1"')
#con.commit()

#cursor.execute('delete from users where id=3')
#con.commit()

#cursor.execute('select * from users where id = 4')
#users = cursor.fetchall()
#print(users)