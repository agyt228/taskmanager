#users(id,login,password) tasks(id,title,description,status)
import sqlite3
con = sqlite3.connect('tasks.db')
cursor = con.cursor()
cursor.execute('''
create table if not exists users(
id integer primary key autoincrement,
login text,
password text
)
''')
cursor.execute('''
create table if not exists tasks(
id integer primary key autoincrement,
title text,
description text,
status text
)''')
i = input('введите логин: ')
p = input('введите пороль: ')
sql = 'insert into users(login, password) values("'+i+'", "'+p+'")'

cursor.execute(sql)
con.commit()