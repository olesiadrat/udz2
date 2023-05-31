from tkinter import *
import tkinter as tk

class Truck(): # класс родителя, содержащий информацию по умолчанию о каждом грузовике
    def __init__(self, name, weight, length, width, height, isOrdered):
        self.name = name
        self.weight = weight
        self.length = length
        self.width = width
        self.height = height
        self.isOrdered = isOrdered  # Поле которое отвечает за статус брони True - забронировано, False - свободно
    
    def get_weight(self):
        return self.weight
    
    def get_length(self):
        return self.length
    
    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height

class Gazel(Truck):
    def __init__(self, status):
        name = 'Газель'
        weight = 2
        length = 3
        width = 2
        height = 2.2
        isOrdered = status
        super().__init__(name, weight, length, width, height, isOrdered)

class Bull(Truck):
    def __init__(self, status):
        name = 'Бычок'
        weight = 3
        length = 5
        width = 2.2
        height = 2.4
        isOrdered = status
        super().__init__(name, weight, length, width, height, isOrdered)

class Man(Truck):
    def __init__(self, status):
        name = 'MAN-10'
        weight = 10
        length = 8
        width = 2.45
        height = 2.7
        isOrdered = status
        super().__init__(name, weight, length, width, height, isOrdered)

class Fura(Truck):
    def __init__(self, status):
        name = 'Фура'
        weight = 20
        length = 13.6
        width = 2.46
        height = 2.7
        isOrdered = status
        super().__init__(name, weight, length, width, height, isOrdered)

class Terminal():
    def __init__(self):
        self.order = []
        self.trucks = [Gazel(True), Bull(False), Man(False), Fura(False)]
        self.main = tk.Tk()
        self.main.geometry('500x500')
        self.main.configure(bg='SkyBlue1')
        self.main.title('ООО "LesyaTrucks"')
    

    def renderMainMenu(self):
        # Метод отрисовывает главное меню
        self.menu_frame = tk.Frame(self.main) # Главный фрейм
        self.menu_frame.pack()

        self.menu_label = tk.Label(self.menu_frame, text='Главное меню :', width=300, bg='#B3E5FC')
        self.menu_label.pack()

        ########################
        # Кнопочки главного меню
        ########################

        button1 = tk.Button(self.menu_frame, text='Просмотреть доступный транспорт', width=30, command=self.renderAvalibleFrame)
        button1.pack()

        button2 = tk.Button(self.menu_frame, text='Создать заявку на перевоз груза', width=30, command=self.renderOrderFrame)
        button2.pack()

        


    def renderOrderFrame(self):
        # Этот метод отрисовывает экран заказа

        self.menu_frame.destroy() # удаляем экран с главным меню 

        self.order_frame = Frame(self.main) # Создаем фрейм заказа внутри главного фрейма

        self.buttonBack = Button(self.order_frame, text='<', command=lambda frame = self.order_frame: self.backToMenu(frame)) # Кнопка для возвращения в главное меню, вызывает функцию backToMenu
        self.buttonBack.grid(row=0, column=0)
        Label(self.order_frame, text='Оформление заказа').grid(row=0, column=1)

        ########################
        # Поля ввода параметров
        ########################

        self.label1 = Label(self.order_frame, text='Вес груза').grid(row=1, column=0)
        self.r1 = Entry(self.order_frame)
        self.r1.grid(row=1, column=1)
        
        self.label2 = Label(self.order_frame, text='Длина груза').grid(row=2, column=0)
        self.r2 = Entry(self.order_frame)
        self.r2.grid(row=2, column=1)

        self.label3 = Label(self.order_frame, text='Высота груза').grid(row=3, column=0)
        self.r3 = Entry(self.order_frame)
        self.r3.grid(row=3, column=1)

        self.orderButton = Button(self.order_frame, text='Подобрать', command=self.orderb) # Кнопка подобрать вызывает при клике функцию orderb
        self.orderButton.grid(row=4, column=0, columnspan=3)

        self.order_frame.pack()
    
    def orderb(self):
        # Подбирает грузовики под параметр 
        # Нужно реализовать проверку корректности параметров
        weight = int(self.r1.get())
        width = int(self.r2.get())
        height = int(self.r3.get())
        """f = 0
        if self.checkInput(self.r1.get()): weight = int(self.r1.get())
        else:
            f = 1
            self.labelError = Label(self.order_frame, text='Некорректный ввод. Введите габариты груза цифрами')
            self.labelError.pack()
        if self.checkInput(self.r2.get()): width = int(self.r2.get())
        else:
            f = 1
            self.labelError = Label(self.order_frame, text='Некорректный ввод. Введите габариты груза цифрами')
            self.labelError.pack()
        if self.checkInput(self.r1.get()): height = int(self.r3.get())
        else:
            f = 1
            self.labelError = Label(self.order_frame, text='Некорректный ввод. Введите габариты груза цифрами')
            self.labelError.pack()"""
        self.av_trucks = []

        for i in self.trucks: 
            if i.weight >= weight and i.height >= height and i.width >= width and not(i.isOrdered): # Проверяем подходит ли каждый грузовик по размерам
                self.av_trucks.append(i)
        self.renderTrucks(self.order_frame, self.av_trucks, 5, True) # Отрисовываем список грузовиков из массива av_trucks
        """else:
            self.labelError = Label(self.order_frame, text='Свободных грузовиков нет')
            self.labelError.pack()"""

    def backToMenu(self, frame):
        # Метод для кнопки назад
        # Принимает в качестве параметра frame - тот фрейм который нужно удалить (т е текущий, в котором мы были)
        frame.destroy()
        self.renderMainMenu() # Отрисовываем главное меню


    def changeSort(self):
        # Функция меняет направление сортировки по весу
        self.renderTruckList = self.renderTruckList[::-1]
        if self.filterButton['text'] == '↑': # Меняем текст кнопочек
            self.filterButton.config(text='↓')
        else:
            self.filterButton.config(text='↑')
        self.trucks_frame.destroy() # Удаляем то что было 
        self.renderTrucks(self.available_frame, self.renderTruckList, 1) # И рендерим новый список грузовиков


    def sortByWeight(self):
        # Сортируем массив со словарями по весу
        # Обычная сортировка пузырьком
        swapped = False
        arr = self.renderTruckList

        for n in range(len(arr)-1, 0, -1):
            for i in range(n):
                if arr[i].weight > arr[i + 1].weight:
                    swapped = True
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]       
            if not swapped: return

    def orderTruck(self, name):
        self.renderCustomerFrame()
        # Функция которая изменяет статус грузовика на забронированный
        for i in self.trucks:
            if i.name == name: # Находим грузовик в массиве грузовиков по его имени
                i.isOrdered = True # Меняем его статус
                break
        
    def renderCustomerFrame(self):
        # Отрисовываем фрейм для оформления заказа
        self.order_frame.destroy()

        self.customer_frame = Frame(self.main)
        self.entry = Label(self.customer_frame, text='Введите свое имя').grid(row=0, column=0)
        self.customer = Entry(self.customer_frame)
        self.customer.grid(row=0, column=1)


    def renderTrucks(self, parent_frame, array,r, orderMode=False):
        # На вход функция получает:
        # parent_frame - фрейм в который мы поместим список с грузовиками. Используется в order_frame и в avalible_frame
        # array - массив с грузовиками которые нам нужно отрисовать 
        # r - строка в grid в родительском фрейме
        # orderMode - True/False - добавляет кнопку брони при True (для order_frame)
        try: self.trucks_frame.destroy() # Пробуем удалить фрейм с грузовиками если он уже есть 
        except: pass
        self.trucks_frame = Frame(parent_frame) # Создаем фрейм в родительском фрейме
        for i in range(len(array)):    
            Label(self.trucks_frame, text=array[i].name).grid(row=i, column=1)
            Label(self.trucks_frame, text=array[i].weight).grid(row=i, column=2)
            if orderMode: # Если orderMode == True => рисуем кнопку забронировать 
                Button(self.trucks_frame, text='Забронировать', command=lambda name = array[i].name: self.orderTruck(name)).grid(row=i, column=3) # Кнопка забронировать, вызывает функцию orderTruck при клике с параметром name
        self.trucks_frame.grid(row=r, columnspan=3)


    def fitlerTrucks(self, arr, ordered=None): 
        # Функция создает массив и отбирает туда машины в зависимости от режима фильтрации 
        # Режимы фильтрации 
        # ordered = None - показать все машины 
        # ordered = True - показать занятые машины
        # ordered = False - показать свободные машины
        self.renderTruckList = [] # Создаем новый массив и помещаем туда отобранные машины
        if ordered==None:
            self.renderTruckList = self.trucks
        for i in arr:
            if ordered:
                if i.isOrdered:
                    self.renderTruckList.append(i)
            else:
                if not(i.isOrdered):
                    self.renderTruckList.append(i)
        return self.renderTruckList
    
    def filterByStatus(self):
        # Отображаем машины в зависимости от статуса фильрации
        # 0 - показать все машины
        # 1 - показать занятые машины 
        # 2 - показать свободные машины 
        # статус фильтрации - остаток от деления на 3
        self.filterMode+=1
        print(self.filterMode)
        if self.filterMode%3==0:
            self.filterStatusButton.config(text='Все') # Меняем текст кнопочки 
            self.sortByWeight()
            self.renderTruckList = self.trucks # Отображаемый массив - все машины
            self.renderTrucks(self.available_frame, self.trucks, 1) # Отрисовываем все машины
        elif self.filterMode%3==1:
            self.filterStatusButton.config(text='Занятые')
            self.sortByWeight() 
            self.renderTrucks(self.available_frame, self.fitlerTrucks(self.trucks, True), 1)
        else:
            self.filterStatusButton.config(text='Свободные')
            self.sortByWeight()
            self.renderTrucks(self.available_frame, self.fitlerTrucks(self.trucks, False), 1)

 
    def renderAvalibleFrame(self): 
        # Отрисовываем экран доступных машин
        self.menu_frame.destroy() # Удаляем экран главного меню
        self.available_frame = Frame(self.main)

        self.filterMode = -1 # Режим фильтрации (по умолчанию -1 тк при начальном запуске функции будет 0)
        self.renderTruckList = self.trucks # Список грузовиков которые мы отображаем (по умолчанию все грузовики)


        ########################
        # Ниже рисуем кнопочки и надписи
        ########################

        self.buttonBack = Button(self.available_frame, text='<', command=lambda frame = self.available_frame:self.backToMenu(frame))
        self.buttonBack.grid(row=0, column=0)
        self.label1 = Label(self.available_frame, text='Тип грузовика').grid(row=0, column=1)
        self.label2 = Label(self.available_frame, text='Грузоподъемность').grid(row=0, column=2)
        self.filterButton = Button(self.available_frame, text='↑', command=self.changeSort)
        self.filterButton.grid(row=0, column=3)
        self.filterStatusButton = Button(self.available_frame, text='Свободные', command=self.filterByStatus)
        self.filterStatusButton.grid(row=0, column=4)
        
        self.filterByStatus() # Запускаем фильтр (по умолчанию показывает все грузовики) и эта функция вызывает потом renderTrucks => отрисовываем грузовики
        self.available_frame.pack()

    def checkInput(self, text):
        for i in text:
            if i.isdigit() == False:
                return False
        return True
    
    def start(self):
        self.renderMainMenu()
        self.main.mainloop()

if __name__ == '__main__':
    terminal = Terminal()
    terminal.start()

