import sqlite3

def progress(status, remaining, total):
    print(f'Copied {total - remaining} of {total} pages...')

try:
    dbcon = sqlite3.connect('app_db.sqlite3')
    dbcon_bkp = sqlite3.connect('app_db_bak.sqlite3')
    with dbcon_bkp:
        dbcon.backup(dbcon_bkp, pages=1, progress=progress)
    print("Backup Successful")

except sqlite3.Error as error:
    print("APP Error: ", error)

finally:
    if dbcon_bkp:
        dbcon_bkp.close()
        dbcon.close()
        print('DB connection is closed')