'''class Designe:
    def get_designe():
        return f'результат дейтельности отдела дизайна '
    
class Programmer:
    def get_programmer():
        return f'результат дейтельности разработчика'
    
class Tester:
    def get_tester():
        return f'результат дейтельности отдела тестирования'
    
class WebStudio:
    def __init__(self,name):
        self.name = name

    def get_designe(self):
        return Designe.get_designe

web_studio = WebStudio('студия цифровых продуктов')

print(web_studio.get_designe)

class WalletRub:
    def __init__(self,cashe):
        self.cashe = cashe

    def cashe_balance(self):
        print (f'{self.cashe} RUB')

class WalletTng:
    def __init__(self,cashe):
        self.cashe = cashe

    def cashe_balance(self):
        print (f'{self.cashe} TNG')

class AdapterRubToTng:
    def __init__(self,cashe):
        self.cashe = cashe * 6.26

    def cashe_balance(self):
        print (f'{self.cashe} TNG')

my_wallet_ru = WalletRub(100)
my_wallet_ru.cashe_balance()

kzt_freund_wallet_tng = WalletRub(12)
kzt_freund_wallet_tng.cashe_balance()

my_wallet_kzt = AdapterRubToTng(my_wallet_ru.cashe)
my_wallet_kzt.cashe_balance()

class USer:
    def __init__(self):
        pass

    def start(self, strategy):
       print(strategy)

class StrategyA:
    list_product = ['площадь 20кв.м','площадь 230 кв.м']
    def strategy():
        return StrategyA.list_product

class StrategyB:
    list_product = ['площадь 2400кв.м','площадь 3000 кв.м']
    def strategy():
        return StrategyA.list_product
    
uSer = USer()
uSer.start(StrategyA.strategy())
print('2 hours later')
uSer.start(StrategyB.strategy())

#iterator позволяет итерировать (перебирать) элементы объекта класса сохраняя все принципы инкапсуляции
#Есть список (каталог) товаров, создать класс и метод вывода каталога товаров

class Market:
    def __init__(self,list_product):
        self.list_product = list_product
        self.index = 0  

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.list_product):
            product = self.list_product[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
        
productc = ['чокопай','яшкино','тук',]
wb = Market(productc)
for product in wb:
    print(productc)
    '''

class Student:
    def __init__(self,name,sge):
        self.name =name
        self.sge =sge

    def update(self):
        menu = input('обновить\n1-имя \n2-возраст')
        new_info = input('введите новое значение')
        if menu == '1':
            self.name = new_info
        else:
            self.age = int(new_info)

class Group:
    def __init__(self,name):
        self.name = name 
        self.list_studens = []
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.list_studens):
            product = self.list_studens[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
        
    def add_studens(self,name,sge):
        self.list_studens.append(Student(name, sge))

    def delent_studens(self,name_studens):
        for index_studens in range(len(self.list_studens)):
            if self.list_studens[index_studens].name == name_studens:
                studens = self.list_studens[index_studens]
                self.list_studens.pop(index_studens)
                del studens
                return self.list_studens
            
    def update(self,new_name):
        self.name = new_name
        return self
    
    def render_group(self):
        print(f'group"{self.name}"')
        num = 1
        for studens in self.list_studens:
            print(f'{num}. {studens.name}, sge {studens.sge}')
            num+=1
        
class Academy:
    def __init__(self,name):
        self.name = name 
        self.list_group = []
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        if self.index < len(self.list_group):
            product = self.list_group[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
        
    def add_group(self,name):
        self.list_group.append(Group(name))

    def delete_group(self,name_group):
        for index_group in range(len(self.list_group)):
            if self.list_group[index_group].name == name_group:
                group = self.list_group[index_group]
                self.list_group.pop(index_group)
                del group
                return self.list_group
            
    def add_student(self,name_group,name_studens,sge_studens):
        for group in self.list_group:
            if name_group == group.name:
                group.add_studens(name_studens,sge_studens)

academy = Academy('TOP')

while True:
    print('МЕНЮ')
    menu = input('1-добавить группу\n2-добавить студента в группу\n3-вывод групп\n4-вывод списка групп\n5-удалить группу\n6-удалить студента\n7-изменить инфо группы\n8-изменить инфо студентов\n0-выход')
    if menu == '1':
        name_group = input('введите название группы')
        academy.add_group(name_group)
    elif menu == '2':
        info = input('введите название группы.имя студента.возрас через запятую')
        name_group,name_studens,sge_studens = info.split(',')
        academy.add_student(name_group,name_studens,sge_studens)
    elif menu == '3':
        print('академия {academy.name}')
        for group in academy:
            print(group.name)
    elif menu == '4':
        name_group = input('введите название группы')
        for group in academy:
            if group.name == name_group:
                group.render_group()
                break
            else:
             print('такой группы нет')
    elif menu == '5':
        name_group = input('введите название группы')
        academy.delete_group(name_group)
    elif menu == '6':
        name_group,name_studens = input('введите через запятую название группы и имя студента').split(',')
        for group in academy:
            if group.name == name_group:
                group.delete_studens(name_studens)
                break
        else:
            print('группа не найдена ')

    elif menu == '7':
        name_group = input('введите название группы')
        new_name_group = input('введите новое назваание группы')
        for group in academy:
            if group.name == name_group:
                group.update(new_name_group)

    elif menu == '8':
        name_group,name_studens = input('введите через зяпятую название группы и имя студента ').split(',')
        for group in academy:
            if group.name == name_group:
                for studens in group:
                    if name_studens == studens.name:
                        studens.update()
                        

#std1,std2,std3 = Student('Joe',15),Student('leo',18),Student('max',19)
#top = Academy('top')
#top.add_group('Python42')
#top.add_group('WEB42')
#top.add_group('Designe2')
##top.delete_group('WEB42')
#top.add_student('Python42','Joe',15)
#top.add_student('Python42','leo',19)
#top.add_student('WEB42','max',15)
#top.add_student('WEB42','anna',16)
#top.add_student('Designe2','olga',26)
#top.add_student('Designe2','poly',23)
#for group in top:
#    print(group.name)
#    group.render_group()
#print(std1.__dict__,std2.__dict__,std3.__dict__)
#group1 = Group('Python42')
#group1.add_studens(std1)
#group1.add_studens(std2) 
#group1.add_studens(std3)  
#group1.delent_studens('leo')
#print('группа',group1.name)
#group1.update('Python43')
#group1.render_group()
#for studens in group1:
#    print(studens.name,studens.sge)

        


