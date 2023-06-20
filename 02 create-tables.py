import sqlite3

try:
    dbcon = sqlite3.connect("app_db.sqlite3")
    cur = dbcon.cursor()

    cur.execute('''CREATE TABLE contacts (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL,
	mobile TEXT NOT NULL UNIQUE
	);''')

    cur.close()
    dbcon.commit()
    print("Table created")

except sqlite3.Error as error:
    print("APP Error: ", error)

finally:
    if dbcon:
        print("Total changes since the db connection is open: ", dbcon.total_changes)
        dbcon.close()
        print('DB connection is closed')
