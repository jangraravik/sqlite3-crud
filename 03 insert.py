import sqlite3

try:
    dbcon = sqlite3.connect("app_db.sqlite3")
    cur = dbcon.cursor()

    cur.execute('''
    INSERT INTO contacts VALUES 
    (1,'Ravi', 9876543211),
    (2,'Tom', 9876543212),
    (3,'John', 9876543213),
    (4,'Harry', 9876543214);
    ''')
    cur.close()

    dbcon.commit()
    print(cur.rowcount, ' records inserted')

except sqlite3.Error as error:
    print("APP Error: ", error)

finally:
    if dbcon:
        print("Total changes since the db connection is open: ", dbcon.total_changes)
        dbcon.close()
        print('DB connection is closed')