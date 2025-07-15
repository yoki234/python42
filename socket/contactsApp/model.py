import sqlite3 as s

class Abonent:
    def __init__(self,name,surname,sex,dob,phone,address):
        self.name=name
        self.surname=surname
        self.sex=sex
        self.dob=dob
        self.phone=phone
        self.address=address

class PhoneBook:

    def __init__(self):
            self.phone_book = []

    def add_abonent(self):
        name= input('введите имя ')
        surname= input('введиите фамилию')
        sex= input('введите пол')
        dob= input('введите дату рождения')
        phone= input('введите номер телефона')
        address= input('введите адрес')
        abonent=Abonent(name,surname,sex,dob,phone,address)
        return abonent 
    

    def del_abonent(self):
        delete_id = input('введите id для удаления абонента')
        return delete_id
        
    def update(self):
        try:
            update_id = input('укажите id для изменени я')
            update_row = int(input (f'введите номер в поле для изменения:\n1-имя\n2-фамилия\n3-пол\n4-др\n5-номере телефона\n6-адрес'))
            update_row = [None,'name','surname','sex','dob','phone','address'][update_row]
            update_valeu = input('введите новое значение')
            result = (update_id,update_row,update_valeu)
            return reversed
        except:
             print('ошибка метода ')

        
class Loader :
    def __init__(self):
        self.path = 'contactsApp/PhoneBase.db'
     
    def create_datd_bose(self):
        with s.connect('self.path') as file:
            cursor = file.cursor()
            cursor.execute('''
CREATE TABLE phone_book(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT
name TEXT NOT NULL,
surname TEXT NOT NULL,
sex TEXT NOT NULL,
dob TEXT NOT NULL,
phone TEXT NOT NULL,
address TEXT NOT NULL)
''')
            
    def create_datd_bose(self):
        with s.connect('self.path') as file:
            cursor = file.cursor()
            cursor.execute('''
                            SELECT * FROM phone_book

                            ''')
            
    def print_abonent(self):
        try:
            with s.connect('self.path') as file:
                cursor = file.cursor()
                cursor.execute('''
                            SELECT * FROM phone_book

                            ''')
                date = cursor.fetchall()
                for i in date:
                    print(i)
        except:
            print('проблемя с базой данных')


    def add_abonent(self,abonent):
         with s.connect('contactsApp/PhoneBase.db') as file:
            cursor = file.cursor()
            cursor.execute('''
INSERT INFO Phone_Book (name,surname,sex,dob,phone,address) VALUES (?,?,?,?,?,?,?)
                           ''',(abonent.name,abonent.surname,abonent.sex,abonent.dob,abonent.phone,abonent.address))       

    def create_datd_bose(self,delete_id):



        try:
            with s.connect('contactsApp/PhoneBase.db') as file:
               cursor = file.cursor()
               cursor.execute('''
DELETE FROM Phone_Book WHERE id=?
                        ''',(delete_id,))
        except:
            print('проблема с базой данных')

    def updete_abonent(self,result):
        print(result)
        try:
            with s.connect('contactsApp/PhoneBase.db') as file:
               cursor = file.cursor()
               cursor.execute('''
UPDATE Phone_Book SET ? = ? WHERE id = ?''',(result[2],result[0]))
        except:
            print('проблема с базой данных')

class Menu:
    def __init__(self):
        self.phone_book = PhoneBook
        
    def main(self,loader):
        #loader.create_datd_bose()    
        while True:
            menu = input('1-ввывести список абонентов\n2-добавить абонента\n3-удалить абонента\n4-редактировать\n0-выход  ')
            if menu=='1':
                loader.print_abonent()
            elif menu == '2':
                loader.add_abonent(self.phone_book.add_abonent())
            elif menu == '3':
                loader.add_abonent(self.phone_book.del_abonent())
            elif menu == '4':
                loader.add_abonent(self.phone_book.update())

 

menu = Menu()
loader = Loader()
menu.main(loader) 