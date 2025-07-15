from random import choice,randint
def create_departament():
    list = []
    for i in range(1, 6):
        building = i
        name = ['Хирургия', "Психиатрия", "Морг", "Вирусология", "Педиатрия"][i - 1]
        list.append([building, name])
    return list

def create_doctors():
    list_name = ["Alexei", "Ivan", "Dmitry", "Sergey", "Andrey", "Vladimir", "Mikhail", "Nikolay", "Yuri", "Viktor", "Pavel", "Oleg", "Artem", "Kirill", "Roman", "Egor", "Vasily", "Gennady", "Leonid", "Fedor", "Semyon", "Timur", "Valery", "Yevgeny", "Vladislav", "Gleb", "Ilya"]
    name = choice(list_name)
    phone = '+7' + str(randint(10000, 99999))
    salary = randint(17_500, 300_000)
    return name, phone, salary

def create_wards():
    list = []
    for i in range(1, 6):
        building = i
        for y in range(1, 10):
            floor = y
            for x in range(10):
                number = str(floor) + str(x)
                list.append([building, floor, int(number)])
    return list

def create_balance():
    for date in range(2020 ,2026):
       for department in range(1,6):
           amount = randint(100_000,800_000)
           list.append([amount,department,date])
    return list

def create_vacations(year):
    id_doctor = randint(1,20)
    day = randint(1,28)
    month = randint(1,12)
    start_vacation = f'{day}-{month}-{year}'
    length_time = randint(1,28)
    return[id_doctor,start_vacation,length_time]

def create_artist(list):
    for artist in list:
        with sql.connect('SQLite/Music/music.db') as db:
        cursor = db.cursor()
        cursor.execute('''
"The Weeknd",

"Led Zeppelin",

"Billie Eilish",

"Hans Zimmer",

"Kendrick Lamar",

"Tame Impala",

"Lady Gaga",

"Sigur Rós",

"Andrea Bocelli",

"Skrillex". 
                       
                    ''')
def create_track():
    for artist in list:
        with sql.connect('SQLite/Music/music.db') as db:
        cursor = db.cursor
        cursor.execute('''''')
        date = cursor.fetchall()
    for album in date:
        track = 1
        while track < 10 :
        with sql.connect('SQLite/Music/music.db') as db:
        cursor = db.cursor
        cursor.execute('''name,id_artict,id,id_music_style,length_track VALUES (?,?,?,?,?)''' ,
        (name_track,*album,180))

    
        track += 1



create_track