#Создайте класс очереди для работы с символьными
#значениями. Требуется создать реализации для операций
#над элементами:
#■ IsEmpty —роверка очереди на пустоту.
#■ IsFull — проверка очереди на заполнение.
#■ Enqueue — добавление элемента в очередь.
#■ Dequeue — удаление элемента из очереди.
#■ Show — отображение всех элементов очереди на
#экран.
#При старте приложения нужно отобразить меню
#-
#обходимую операцию
'''
class Node:
    def __init__(self,name,next_node = None,prev_node=None):
        self.name = name
        self.next_node = next_node
        self.prev_node  = prev_node

class Queue :
    length = 0
    max_length = 8
    head = None
    tail = None
    def enqueue(self,name):
        if self.head is None:
            self.head = self.tail = Node(name)
        elif self.length < self.max_length:
            new_node = Node(name,prev_node = self.tail)
            self.length += 1   
            self.tail.next_node = new_node
            self.tail=new_node    
            self.length += 1    
        else:
            print( f'очередь заполнена')
    

    def show(self):
        try:
            num_in_queue = 1
            line = f'очередь:'
            current_node = self.head
            while current_node.next_node != None:
                line += f'{num_in_queue}-{current_node.name}, '
                num_in_queue += 1
                current_node = current_node.next_node
            line += f'{num_in_queue}-{current_node.name}.'
            return line
        except:
            return f'очередь пуста'

    def dequeue(self):
        try:
            if self.head.next_node is None:
                del self.head
            else:
                self.head = self.head.next_node
                self.head.prev_node
            self.length -=1
        except:
            print('удалять  некого! Очередь пуста')

    def is_empty(self):
        if self.length == 0 :
            print('очередь не пуста ')
            return True
        else :
            print('очередь не пуста ')
            return False
    
    def is_full(self):
        if self.length == self.max_length:
            print('очередь заполнена')
            return True
        else:
            print(' очередь не заполнена')
            return False



        




queue_in_market = Queue()
queue_in_market.enqueue('Ivan')
queue_in_market.enqueue('Ivan2')
queue_in_market.enqueue('Ivan3')
queue_in_market.enqueue('Ivan4')
queue_in_market.enqueue('Ivan5')
queue_in_market.dequeue()
queue_in_market.dequeue()
queue_in_market.dequeue()
queue_in_market.dequeue()
queue_in_market.dequeue()
queue_in_market.is_empty()

print(queue_in_market.show())

#Создайте класс очереди с приоритетами для работы
#с символьными значениями.
#Требуется создать реализации для операций над элементами очереди:
#■ IsEmpty — проверка очереди на пустоту.
#■ IsFull — проверка очереди на заполнение.
#1
#■ InsertWithPriority — добавление элемента c приоритетом в очередь.
#■ -
#мым высоким приоритетом из очереди.
#■ Peek — возврат самого большого по приоритету элемента. Обращаем ваше внимание, что элемент не
#удаляется из очереди.
#■ Show — отображение всех элементов очереди на экран.
#При показе элемента также необходимо отображать
#приоритет.
#При старте приложения нужно отобразить меню, с помощью которого пользователь может выбрать
#обходимую операцию

class Node:
    def init(self,task, priority, next_node = None, prev_node = None):
        self.task = task
        self.priority = abs(float(priority))
        self.next_node = next_node
        self.prev_node = prev_node

class PriorityQueue:
    head = None
    length = 0
    max_length = 4

    def show(self):
        if self.head is None:
            print('очередь пуста')
        else:
            line = f'Очередь: \n'
            current_node = self.head
            while current_node.next_node != None:
                line += f'#{current_node.priority} #{current_node.task}'
                current_node = current_node.next_node
            line += f'#{current_node.priority} #{current_node.task}'
            print(line)
            return line
            
    def insert_with_priority(self, task, priority):
        #new_node = Node()
        if self.head is None:
            self.head = Node(task, priority)
            self.length += 1
        elif self.length < self.max_length:
            current_node = self.head
            if priority < current_node.priority:
                current_node.prev_node = Node(task, priority,next_node=current_node)
                self.head = current_node.prev_node
                self.length += 1
                return f'элемент добавлен'
            while current_node.next_node != None:
                if current_node.priority > priority:
                    #current_node.prev_node = Node(task, priority, next_node=current_node, prev_node=current_node)
                    #current_node.prev_node = current_node.prev_node.next_node
                    new_node = Node(task, priority, next_node=current_node, prev_node=current_node.prev_node)
                    current_node.prev_node.next_node = new_node
                    current_node.prev_node = new_node
                    self.length += 1
                    return f'элемент добавлен'
                else:
                    current_node = current_node.next_node

            if priority < current_node.priority:
                current_node.prev_node.next_node =   current_node.prev_node = Node(task, priority,next_node=current_node, prev_node = current_node.prev_node)
            else:
                current_node.next_node = Node(task, priority, prev_node=current_node)
          
            #добавить связь с предидущем

            self.length += 1
            return f'элемент добавлен'
        else:
            return f'добавление не возможно очередь заполнена'
        
    
    def pull_highest_priority_element(self):
        try:
            if self.length>1:
               self.head = self.head.next_node
               del self.head.prev_node
            else:
               del self.head
            self.length -= 1
        except:
            print('hgeuws',self.length)

    def peeck(self):
        if self.length !=0:
            print(f'#{self.head.priority}#{self.head.task}.')
            return f'#{self.head.priority}#{self.head.task}.'
        else:
            print('очередь пуста ')
    


tobo = PriorityQueue()

tobo.insert_with_priority('задание 1', 2)
tobo.insert_with_priority('задание 2', -1)
tobo.insert_with_priority('задание 3', 1.2)
tobo.insert_with_priority('задание 4', 5)
tobo.insert_with_priority('задание 5', 2.2)
tobo.pull_highest_priority_element()
tobo.pull_highest_priority_element()
tobo.pull_highest_priority_element()
tobo.pull_highest_priority_element()
tobo.pull_highest_priority_element()
tobo.show()
'''

#Необходимо разработать приложение, которое позволит сохранять информацию о логинах пользователей и их
#паролях. Каждому пользователю соответствует пара ло-
#■ Добавить нового пользователя
#■ Удалить существующего пользователя
#■ Проверить существует ли пользователь
#■ Изменить логин существующего пользователя
#■ Изменить пароль существующего пользователя
#Для реализации задания обязательно используйте
#одну из структур данных. При выборе руководствуйтесь
#постановкой задачи.

class User():
    def __init__(self, login,password,next_user = None):
         self.login = login
         self.password = password
         self.next_user = next_user

class UserBase:
    head = None
    length = 0 

    def __str__(self):
        line = f'список пользоватей:\n'
        currrent_user = self.head
        for i in range(self.length):
            line += f'Login:{currrent_user.login},password:{currrent_user.password}\n'
            currrent_user = currrent_user.next_user
        return line
    
    def add_user(self,user):
        if self.head is None:
            self.head = user
        else:
            user.next_user = self.head
            self.head = user
        self.length +=1

    def search_of_login(self,login):
        currrent_user = self.head
        prev_user = None
        for index in range(self.length):
            if login == currrent_user.login:
                return currrent_user,prev_user
            else:
                prev_user = currrent_user
                currrent_user = currrent_user.next_user
        else:
            return None
        
    def delete_user(self,login):
        if login == self.head.login:
            currrent_user= self.head
            self.head = self.head.next_user
        else:
            currrent_user,prev_user = self.search_of_login(login)
            prev_user.next_user = currrent_user.next_user
            del currrent_user
        self.length -= 1

    def check_user(self,login):
        if self.search_of_login(login) is None:
            return False
        else:
            return True
        
    def updete_login(self):
        login = input('введите логин, которые нужно заметить ')
        currrent_user,prev_user = self.search_of_login(login)
        if currrent_user is None:
            print('нет такого пользователя ')
        else:
            new_login = input('введите новый логин')
            currrent_user.login = new_login
        

array = UserBase()
user1 = User('suuper_user','123123')
user2 = User('admin','3333333')
user3 = User('mario','2222222')
array.add_user(user1)
array.add_user(user2)
array.add_user(user3)

print (array.updete_login())
print(array)
        