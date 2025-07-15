from generator import list_student
import sqlite3 as sql
print(list_student)
with sql.connect('SQLite/journal.db') as db:
    cursor = db.cursor()
#    cursor.execute('''
#        CREATE TABLE IF NOT EXISTS 'Students'(
#        'id' INTEGER PRIMARY KEY AUTOINCREMENT ,
#        'name' TEXT, 
#        'age' INTEGER, 
#        'city' TEXT ,
#        'country' TEXT,
#        'mail' TEXT,
#        'phone' TEXT,
#        'group' TEXT, 
#        'aver_value' REAL ,
#        'min_theme' TEXT, 
#        'max_theme' TEXT )''')
#    #заполнение таблице
#    for stdnt in list_student:
#        cursor.execute('''
#INSERT INTO 'Students' ('name', 'age', 'city','country' ,'mail' ,'phone' ,'group', 'aver_value' ,'min_theme','max_theme') VALUES(?,?,?,?,?,?,?,?,?,?)''', (*stdnt, ))
#cursor.execute('''
#SELECT name FROM Students WHERE aver_value > 3.5 and aver_value < 4.5
#''')
#stds = cursor.fetchall()
#for std in stds :
#    print(std)

cursor.execute('''
SELECT name FROM Students WHERE aver_value > 3.5 and aver_value < 4.5
''')
stds = cursor.fetchall()
for std in stds :
    print(std)
    
    