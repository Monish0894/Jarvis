import sqlite3

conn = sqlite3.connect("igris.db")
cursor = conn.cursor()

query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)

query = "INSERT INTO sweb_command VALUES (null,'google','https://www.google.com/')"
cursor.execute(query)
conn.commit()

query = "CREATE TABLE IF NOT EXISTS sweb_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)

 