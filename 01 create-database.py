import sqlite3

dbcon = sqlite3.connect("app_db.sqlite3")
cur = dbcon.cursor()

result = cur.execute("SELECT sqlite_version();").fetchone()
print("SQLite Database Version is: ", result)
cur.close()

dbcon.close()