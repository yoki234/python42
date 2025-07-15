import sqlite3 as s
from generator import hospital_info
with s.connect('SQLite/Hospital.db') as db:
    cursor = db.cursor()
#    cursor.execute('''
#CREATE TABLE IF NOT EXISTS Departments(
#    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#    building INTEGER NOT NULL CHECK(building >=1 and building <= 5),
#    name TEXT NOT NULL UNIQUE)
#''')
#    cursor.execute('''
#CREATE TABLE IF NOT EXISTS Doctors(
#    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#    phone INTEGER NOT NULL,
#    name TEXT NOT NULL,
#    salary REAL NOT NULL)
#''')
#    cursor.execute('''
#CREATE TABLE IF NOT EXISTS Wards(
#    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#    building INTEGER NOT NULL CHECK(building >=1 and building <= 5),
#    floor INTEGER NOT NULL CHECK(floor >= 1),
#    number INTEGER NOT NULL
#    )
#''')
#
#    cursor.execute('''
#CREATE TABLE IF NOT EXISTS Balance(
#    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#    amount REAL NOT NULL ,
#    id_department INTEGER NOT NULL ,
#    data INTEGER NOT NULL,
#    FOREIGN KEY id_department REFERENCE Department(id))               
#''')
#    
#    cursor.execute('''
#CREATE TABLE IF NOT EXISTS Vacations(
#    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,     
#    id_doctor INTEGER NOT NULL,
#    start_vacation TEXT NOT,
#    length_time INTEGER, NOT NULL CHECK(length_time <= 28)                    
#    FOREIGN KEY id_doctor REFERENCE Doctor (id))  
#''')

#    for i in hospital_info[0]:
#        cursor.execute('''
#    INSERT INTO Departments(building, name) VALUES (?, ?)
#''', (*i,))
#        
#    for i in hospital_info[1]:
#        cursor.execute('''
#    INSERT INTO Doctors(name, phone, salary) VALUES (?, ?, ?)
#''', (*i,))
#    
#    for i in hospital_info[2]:
#        cursor.execute('''
#    INSERT INTO Wards(building, floor, number) VALUES (?, ?, ?)
#''', (*i,))
#        
#    for i in hospital_info[3]:
#        cursor.execute('''
#    INSERT INTO Balance(amount, id_departament, date) VALUES (?, ?, ?)
#''', (*i,))
#    for i in hospital_info[4]:
#        cursor.execute('''
#    INSERT INTO Vacations(id_doctor,start_vacation, length_time) VALUES (?, ?, ?)
#''', (*i,))

#    cursor.execute('''
#SELECT name, salary FROM Doctors
#                ''')
#    date = cursor.fetchall()
#    for line in date:
#        print(f'имя: {line[0]},его зарплата:{line[1]}руб.')

#    cursor.execute('''
#SELECT id, amount,data 	FROM Balance WERE date LIKE '25%'
#                ''')
#    date = cursor.fetchall()
#    for line in date:
#        print(f'имя: {line[0]},его зарплата:{line[1]}руб.') 
#
#
#    cursor.execute('''
#SELECT id, amount,data 	FROM Balance WERE date LIKE '25%'
#                ''')
#    date = cursor.fetchall()
#    for line in date:
#        print(f'имя: {line[0]},его зарплата:{line[1]}руб.') 


#    cursor.execute('''
#SELECT dOCTOR.NAME , dOCTOR.SALARY , VARH . START _VACATION
#FROM dOCTOR ,VACANCION 
#Wehee Valcom
#                
#''')
#    date = cursor.fetchall()
#    for line in date:
#        print(f'имя: {line[0]},его зарплата:{line[1]}руб.') 
#
#
#    cursor.execute('''
#SELECT Depart5t .name,avg {balaction.anmectr}
#FROM der4ement ,bactoion
#where id = 9 
#GROUP
#''')
#    date = cursor.fetchall()
#    for line in date:
#        print(f'имя: {line[0]},его зарплата:{line[1]}руб.') 
