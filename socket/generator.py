from random import  choice,randint
def create_student():
    #name
    list_name = ["Alexei", "Ivan", "Dmitry", "Sergey", "Andrey", "Vladimir", "Mikhail", "Nikolay", "Yuri", "Viktor", "Pavel", "Oleg", "Artem", "Kirill", "Roman", "Egor", "Vasily", "Gennady", "Leonid", "Fedor", "Semyon", "Timur", "Valery", "Yevgeny", "Vladislav", "Gleb", "Ilya",]
    name = choice(list_name)
    #age
    age = randint(17,30)
    #city
    list_city = ["Moscow", "Saint Petersburg", "Novosibirsk", "Yekaterinburg", "Nizhny Novgorod", "Kazan", "Chelyabinsk", "Omsk", "Samara", "Rostov-on-Don", "Ufa", "Krasnoyarsk", "Perm", "Voronezh", "Volgograd", "Krasnodar", "Saratov", "Tolyatti", "Tyumen", "Izhevsk", "Barnaul", "Ulyanovsk", "Irkutsk", "Khabarovsk", "Yaroslavl", "Vladivostok", "Makhachkala", "Tomsk",]
    city = choice(list_city)
    #country
    list_country = ['Russia','Belorussia','Kazahtan','Ukraine']
    country = choice(list_country)
    #mail
    mail = name.lower()+str(age)+'@mail.ru'
    #phone
    phone = '+7'+str(randint(10000,99999))
    #group
    list_group = ['web','Desinge','Test','Python','Computer_science','SMM']
    group = choice(list_group)
    #aver_value
    aver_value = randint(20,50)/10
    #min_theme
    list_theme = ['web desigen','computer_science','Coging','Math','Eng','Startup']
    min_theme = choice(list_theme)
    #max_theme
    max_theme = choice(list_theme)
    return name, age, city ,country,mail ,phone ,group, aver_value ,min_theme, max_theme
list_student = []
for i in range(1000):
    list_student.append(create_student())
print(list_student)
