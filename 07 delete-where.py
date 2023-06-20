import sqlite3

try:
    dbcon = sqlite3.connect("app_db.sqlite3")
    cur = dbcon.cursor()

    cur.execute('''DELETE FROM contacts WHERE id=4;''')
    cur.close()

    dbcon.commit()
    print(cur.rowcount, ' records deleted')

except sqlite3.Error as error:
    print("APP Error: ", error)

finally:
    if dbcon:
        print("Total changes since the db connection is open: ", dbcon.total_changes)
        dbcon.close()
        print('DB connection is closed')
