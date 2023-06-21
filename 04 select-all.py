import sqlite3

try:
    dbcon = sqlite3.connect("app_db.sqlite3")
    cur = dbcon.cursor()

    cur.execute('''SELECT * FROM contacts ORDER BY id DESC;''')
    #rows = cur.fetchall()
    rows = cur.fetchmany(100)

    print('Total Records:', len(rows))

    for row in rows:
        print(row)


    cur.close()

except sqlite3.Error as error:
    print("APP Error: ", error)

finally:
    if dbcon:
        print("Total changes since the db connection is open: ", dbcon.total_changes)
        dbcon.close()
        print('DB connection is closed')