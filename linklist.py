#динамический файл
'''array = [43,534,54,576,7,768,32]
print(array[3])
array.append(-1)#предпочтителен по скорости 
array.insert(3,0)
array.remove(7)#число уд
array.pop(2)#индекс уд
print(array)


#Задание 1
#Пользователь вводит с клавиатуры набор чисел. Полученные числа необходимо сохранить в односвязный
#список. После чего нужно показать меню, в котором
#предложить пользователю набор пунктов:
#1. Добавить элемент в список.+
#2. Удалить элемент из списка.+
#3. Показать содержимое списка.+
#4. Проверить есть ли значение в списке.+
#5. Заменить значение в списке.
#В зависимости от выбора пользователя выполняется
#действие, после чего меню отображается снова.

class LinkList:
    lenght = 0
    head =  None
    class Node:
        def __init__(self,value,next_nade = None):
            self.value=value
            self.next_nade=next_nade

    def my_append(self,value):
        if self.head is None:
            self.head = LinkList.Node(value)
        else:
            current_node = self.head
            while current_node.next_nade != None:
                current_node = current_node.next_nade
            current_node.next_nade =  LinkList.Node(value)
        self.lenght += 1 

    def __str__(self):
        result_line = '<$'
        current_node = self.head
        while current_node.next_nade != None:
            result_line += f'{current_node.value},'
            current_node = current_node.next_nade
        result_line += f'{current_node.value}$>'
        return result_line
    
    def search (self,value_from_search):
        current_node = self.head
        while current_node.next_nade !=None:
            if current_node.value == value_from_search:
                return True
            current_node = current_node.next_nade
        if current_node.value == value_from_search:
            return True
        else:
            return False
        
    def my_remove(self,value_from_remove):
        current_node = self.head
        if self.head.value == value_from_remove:
            self.head = current_node.next_nade
            del current_node
            self.lenght -= 1
            return 'элемент удален'
        while current_node.next_nade !=None:
            if current_node.next_nade.value == value_from_remove:
                current_node.next_nade = current_node.next_nade.next_nade 
                del current_node.next_nade
                current_node.next_nade = current_next_node 
                self.lenght -=1
                return 'элемент удален'
            current_node= current_node.next_nade
        return 'элемент для  удаления не найден'
    
    def update (self,old_value,new_value):
        current_node = self.head
        while current_node.next_nade !=None:
            if current_node.value == old_value:
                current_node.value = new_value
                return 'данные обновлены'
            current_node = current_node.next_nade
        if current_node.value ==old_value:
            current_node.value = new_value
            return'данные обновлены'
        else:
            return 'данные не обновлены'

                


#my_array = LinkList()
#my_array.my_append(52)
#my_array.my_append(-5)
#my_array.my_append(0)
#my_array.my_append(5342)
#print (my_array.update(52))
##my_array.head.next_nade = None
#print(my_array)


array = input('введите числа через пробел')
link_list = LinkList()
array = array.split(' ')
for elen in array:
    link_list.my_append(elen)
print(f'ваш массив чисел:{link_list}')
while True:
    choice = input(f'1-добавить\n2-удалить\n3-gjbcr\n4-заменить\n5-выход\0-выход')
    if choice =='1':
        value = input('введите значение для добовдления ')
        link_list.my_append(value)
    elif choice == '2':
        value = input('введите значение для удаления ')
        link_list.my_append(value)       
    elif choice == '3':
        value = input('введите значение для поиска ')
        print(link_list.search(value))
    elif choice == '4':
        old_value = input('lehig ogjueds op;jega')
        new_value = input('ehaig iegju ueaojgf')
        link_list.update(old_value,new_value)
    elif choice == '0 ':
        break
print('программа завершина')
      
class Node:
    def __init__(self,value,next_node = None, prev_node = None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

class DoubleLinkList:
    head = None
    tail = None
    lenght = 0 

    def my_append(self,value):
        if self.head == None:
            self.head = Node(value)
            self.tail = self.head
        else:
            #current_node = self.head
            #while current_node.next_node != None:
            #    current_node = current_node.next_node
            #    current_node.next_node = Node (value,prev_node=current_node)
            #    self.tail = current_node.next_node
            current_node = self.tail
            current_node.next_node = Node(value,prev_node=current_node)
            self.tail = current_node.next_node
        self.lenght += 1

    def __str__(self):
        line = '<<'
        current_node = self.head = self.head
        while current_node.next_node != None:
            line += f'{current_node.value},'
            current_node = current_node.next_node
        line += f'{current_node.value}>>'
        return line
        

Double_Link_List = DoubleLinkList()
Double_Link_List.my_append(52)
Double_Link_List.my_append(25)
print(Double_Link_List)


class Node:
    def __init__(self,value,next_node = None, prev_node = None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

class DoubleLinkList:
    head = None
    tail = None
    lenght = 0 

    def my_append(self,value):
        if self.head == None:
            self.head = Node(value)
            self.tail = self.head
        else:
            #current_node = self.head
            #while current_node.next_node != None:
            #    current_node = current_node.next_node
            #    current_node.next_node = Node (value,prev_node=current_node)
            #    self.tail = current_node.next_node
            current_node = self.tail
            current_node.next_node = Node(value,prev_node=current_node)
            self.tail = current_node.next_node
        self.lenght += 1

    def __str__(self):
        line = '<<'
        current_node = self.head = self.head
        while current_node.next_node != None:
            line += f'{current_node.value},'
            current_node = current_node.next_node
        line += f'{current_node.value}>>'
        return line
        
    def get_value(self,value_from_search):
        current_node = self.head
        while current_node.next_node != None:
            if current_node.value == value_from_search:
                return True
            current_node = current_node.next_node
        if current_node.value == value_from_search:
                return True
        else:
            return False    
        
    def del_value(self,value_from_delente):
        if self.head.value == value_from_delente:
            node_from_delete = self.head
            self.head = self.head.next_node
            self.head.prev_node = None
            del node_from_delete
        elif self.tail.value == value_from_delente:
            node_from_delete = self.tail
            self.tail = self.tail.prev_node
            self.tail.next_node = None
            del node_from_delete

        else:
            current_node = self.head        
        while current_node.next_node != None:
            if current_node.value == value_from_delente:
                node_from_delete = current_node
                current_node.prev_node.next_node = current_node.next_node
                current_node.next_node.prev_node = current_node.prev_node
            current_node = current_node.next_node
        del node_from_delete
        self.lenght -= 1

    def update_value(self,old_value,value_from_update):
        current_node = self.head        
        while current_node.next_node != None:
            if current_node.value == old_value:
                current_node.value = value_from_update
            current_node = current_node.next_node
        if current_node.value == old_value:
                current_node.value = value_from_update
        

                





Double_Link_List = DoubleLinkList()
Double_Link_List.my_append(52)
Double_Link_List.my_append(25)
Double_Link_List.my_append(24)
Double_Link_List.update_value(25,203)
print(Double_Link_List) 


#Задание 3
#Реализуйте класс стека для работы с целыми значениями (стек целых).
#Стек должен иметь фиксированный размер.
#Реализуйте набор операций для работы со стеком:
#■ помещение целого значения в стек;+
#■ выталкивание целого значения из стека;+
#■ подсчет количества целых в стеке;
#■ проверку пустой ли стек;
#■ проверку полный ли стек;
#■ очистку стека;
#■ получение значения без выталкивания верхнего целого в стеке.
#При старте приложения нужно отобразить меню с
#помощью, которого пользователь может выбрать необходимую операцию
class Node:
    def __init__(self,value,next_node = None, prev_node = None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node


class Stack:
    head = None
    tail = None
    length = 0 
    max_length = 5 
    def stack_append(self,value):
        if self.length < self.max_length:
            if self.head == None:
                self.head = Node(value)
                self.tail = self.head
            else:
                current_node = self.tail
                current_node.next_node = Node(value,prev_node=current_node)
                self.tail = current_node.next_node
            self.length += 1
        else:
            print('eguopi')


    def stack_pop(self):
            node_from_delete = self.head
            self.tail = self.tail.prev_node
            self.tail.prev_node = None
            self.length -=1
            del node_from_delete

    def get_lenght(self):
        print(f'элементов в стаке: {self.length}')

    def check_emty(self):
        if self.head is None:
            print('стак пуст')
        else:
            print('стак не пустой ')

    def stack_clear(self):
        current_node = self.head
        while current_node.next_node != None:
            node_from_delete = current_node
            current_node = current_node.next_node
            del node_from_delete
        del current_node
        self.length = 0 
        self.head = None
        self.tail = None

    def get_tail(self):

        print(f'последний элемент: {self.tail.value}') 
my_stack = Stack()
array = input('Введите числа через пробел.')


array = array.split(' ')
for elem in array:
    my_stack.stack_append(elem)

while True:

    choice = input(f'1-добавить\n2-удалить\n3-поиск\n4-заменить\n5-вывод\n0-выход')
    if choice == '1':
        value = input('Введите значение для добавления')
        my_stack.stack_append(value)
    elif choice == '2':
       my_stack.stack_pop()
    elif choice == '3':
        my_stack.get_tail()

    elif choice == '4':
        my_stack.check_emty()
    elif choice == '5':
        my_stack.stack_clear()
    elif choice == '0':
        break
print('Программа завершена')


my_stack.check_emty()
my_stack.stack_append(1)
my_stack.stack_append(2)
my_stack.stack_append(3)
my_stack.check_emty()
my_stack.stack_append(4)
my_stack.stack_append(5)
my_stack.stack_append(6)
my_stack.stack_pop()
#my_stack.stack_clear()
my_stack.get_tail()
my_stack.get_lenght()
#print(my_stack.length,my_stack.tail.value)
        
''' 

