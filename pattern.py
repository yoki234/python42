# ПРЕКТИРОВАНИЕЯ 
# ПОРАЖДАЮЩИЕ (singleton,fabric,abstract fabric)
# СТРУКТУРНЫЕ (facade)
# ПОВЕДЕНЧЕСКИЕ (iterator)

#Создайте классическую реализацию паттерна Singleton.
#Протестируйте работу созданного класса.

'''class Singletone :
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super (Singletone,cls).__new__(cls)
        else:
            print('экземпляр-одиночка уже создан')
        return cls._instance 
    
class NotSingletone():
    pass

refery = Singletone()
print(refery)
refery2 = Singletone()
print(refery2)
print(refery is refery2)

obj1 = NotSingletone()
obj2 = NotSingletone()
print(obj1 is obj2,obj1,obj2 )

#pattern Fabric

class Fabric:
    def  __init__(self, name, age, proffesion):
        self.name = name
        self.age = age
        self.proffesion = proffesion

    def get_info(self):
        return f'Name: { self.name},Proffesion {self.proffesion} '
         
class Driver(Fabric):
    def __init__(self, name, age, proffesion):
        super().__init__(name, age, proffesion)

class Pilot(Fabric):
    def __init__(self, name, age, proffesion):
        super().__init__(name, age, proffesion)

user1 = Driver('Dominic Taretto', 45,'Speedster')
user2 = Pilot('Almasheev',76, 'test pilot')
print(user1,user2)
print (issubclass(Fabric,Driver), issubclass(Pilot,Fabric))

#Создайте реализацию паттерна Abstract Factory. Протестируйте работу созданного класса.

from abc import ABC, abstractmethod
class AbstractFactory:
    @abstractmethod
    def create_factory(self,name ):
        if name == 'Lada':
            factory = LadaFactory()
            return factory
        elif name == 'Sukhoi':
            pass
class LadaFactory(AbstractFactory):
    def __init__(self):
        self.name = 'фабрика компании лад'
        
class SukhoiFactory(AbstractFactory):
    def __init__(self):
        self.name = 'фабрика компании сухой'
        def create_factory(self.name  )'''
#Пользователь вводит с клавиатурынабор чисел и путь
#кфайлу для сохранения полученных данных. Необходимо:
#■ Сохранить все полученные числа.
#■ Найти максимум, минимум. Эти значения сохранить
#в том же файле.
#■ Отобразить числа.
#■ Отобразить максимум и минимум.
#■ Создать класс для логгирования операций. При создании объекта класса нужно уточнить куда производится
#логгирование: экран или файл. В программе можно
#создать только один объект класса. Все действия
#объекта этого класса.
class Logger:
    _instance = None
    logger_location = None
    def __new__(cls):
        if cls._instance is None:
            cls.logger_location = input('куда вести запись логирования:\n1-в файл\n2-в термнал')
            cls._instance = super(Logger,cls ).__new__(cls)
        else:
            print('логгер уже создан')
        return cls._instance
    
    def logging(self,message):
        if self.logger_location == '2':
            print(message)
        else:
            with open ('Loggin.txt', 'a', encoding= 'upf - 8') as file:
                file.write(message + '\n')
    
    def log_input_digits(self):
        self.logging('были добавлены числа ')
    
    def log_exterm_digits(self,maxx,minx):
        self.logging (f'выполнен поиск максимального и минимального.Мах {maxx},мин{minx}')

    def log_render(self,list_digits):
        self.logging(f'выполнен рендер массвива {list_digits}, и мах.эл{max(list_digits)}и мин эл.{min(list_digits)}')


class Digits:
    def __init__(self,path='Didgits.txt',logger = None):
        array = input('введите числа через пробел')
        self.path= path
        self.logger = logger
        self.list_digits = list(map(input,array.split(' ')))
        with open(path,'a', encoding= 'utf-8') as file:
            for digit in self.list_digits:
                file.write(str(digit)+'\n')
            logger.log_input_digits()
    
    def get_extrem(self):
        maxx = max(self.list_digits)
        minx = min(self.list_digits)
        with open(self.path, 'a',encoding= 'utf-8') as file:
            file.write(f'максимальный элемент {maxx},минимальный{minx}')
        self.logger.log_exterm_digits(maxx,minx)

    def render(self):
        print(f'массив чисел:{self.list_digits}.\nMax {max(self.list_digits)},min:{min(self.list_digits)}')
        self.logger.log_render(self.list_digits)


logger = Logger()
print(logger)
array = Digits(logger = logger)
array.get_extrem()
array.render()
