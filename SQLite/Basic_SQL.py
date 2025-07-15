import sqlite3 as sq

with sq.connect('exeaple.db') as db:
    cursor = db.cursor()
#    cursor.execute('''CREATE TABLE IF NOT EXIST first_db(
#                   id INTEGER,
#                   name TEXT)''')
#    cursor.execute('''SELECT * FROM journal''')
#    journal = cursor.fetchall()
#    print(journal)
#    for student in journal:
#        print(f'Name:{student[0]}\nAge : {student[1]}\nAverValue:{student[2]}\n***')

#cursor.execute('SELECT ФИО FROM journal')
#name_list = cursor.fetchall()
#for name in name_list
#print(name)
cursor.execute('SELECT ФИО FROM journal')