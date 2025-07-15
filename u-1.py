##упаковка (оператор*)
#var1= 34
#var2='python'
#var3= True
#*my_list, = var1,var2,var3
#print(my_list)
#
##распаковка 
#list = [34,'hello',False] * 2
##a,b,c = list
##a, *b = list
#c, *a,b = list
#print(a,b,c) 
#
#def f(*args):
#    print(args)
#
#f(23,32,6,7,98,34,65,8)

#распаковка **
#
#def f(**kwrags):
#    print(kwrags)
#
#f(param1 = 34, param2 = 'python', param3 = True)
#f(age = 34, nick = 'python', param3 = True)

#распаковка в цепи 
#list_user = [
#    ['joe','byden'],
#    ['donald', 'trump'],
#    ['micky','mouse']
#]

#for name,last_name in list_user:
#    print(f'Name: {name}; Last name:{last_name}\n')
#line = -7,10
#print(line)
#for i in range(*line):
#    print(i)
#
#print(*range(10))  
#
#Есть некоторый словарь, который хранит названия
#стран и столиц. Название страны используется в качестве
#ключа, название столицыв качестве значения. Необходимо
#реализовать: добавление данных, удаление данных, поиск
#данных, редактирование данных, сохранение и загрузку
#данных (используя упаковку и распаковку).

#def add_date(country_dict):
#    data = input('введите страну и столицу через пробел ')
#    country, capital = data.split(' ')
#    if country in country_dict.keys():
#        print('такая страна уже есть')
##        return country_dict
#    else:
#        country_dict[country]= capital
#    return country_dict
#
#def delete_data(country_dict):
#    data = input('введите страну для удаления!')
#    if data in country_dict.keys():
#        del country_dict[data]
#        print(f'страна {data} успешно удалена')
#    else:
#        print('ошибка. такой страны нет')
#    return country_dict
#
#def searche_data(country_dict):
#    data = input('введите название страны или сталицы')
#    for country, capital in country_dict.items():
#        if data == country or data == capital:
#            print(f'результат плиска:\n {country} {capital}')
#            break
#        else:
#            print('ничего не найдено!')
#        return country_dict
#    
#def update_data(country_dict):
#    data = input('введите название страны и новое название страны ')
#    country, capital = data.split(' ')
#    country_dict[country] = capital
#    return country_dict
#
#def sava_data(country_dict):
#    data = ''
#    for key, value in country_dict.items():
#        data += f'{key}:{value}\n'
#    with open ('country_dict.txt','w') as file:
#        file.write(data)
#        return country_dict
#    
#def load_data(country_dict):
#    with open('country_dict.txt','r') as file:
#        for line in file:
#            country,capital = line.split(':')
#            country_dict[country] = capital[:-1]
#    return country_dict
#
#
#
#
#country_dict = {} #{'USSR':'Moscow','PIP':'URU', 'GFG':'FUF'}
#load_data(country_dict)
#while True:
#    print(country_dict)
#    choice = int(input('база стран и столиц\nМеню:\n1-добавить\n2-удалить\n3-поиск\n4-редактировать\n5-сохранение\n6-загрузка\n0-выход'))
#    if choice == 0 :
#        sava_data(country_dict)
#        break
#    elif choice == 1:
#        add_date(country_dict)
#    elif choice == 2: 
#        delete_data(country_dict)
#    elif choice == 3:
#        searche_data(country_dict)
#    elif choice == 4 :
#        update_data(country_dict)
#    elif choice == 5 :
#        sava_data(country_dict)
#    elif choice == 6 :
#        load_data(country_dict)

#Задание 2
#Есть некоторый словарь, который хранит названия
#музыкальных групп(исполнителей) и альбомов. Название группы используется в качестве ключа, название
#альбомов в качестве значения. Необходимо реализовать:
#добавление данных, удаление данных, поиск данных,
#редактирование данных, сохранение и загрузку данных
#(используя упаковку и распаковку).
class Music:
    music_dict = {}

    def add_band(self,add_band):
        band = Band(add_band)
        self.music_dict[band.name] = band.dict_phia

class Band:
    def __init__(self,name):
        self.name = name
        self.dict_phia = []

    def add_album(self,name_album):
        self.dict_phia.append(name_album)

spotify = Music()
spotify.add_band
        