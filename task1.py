from tkinter import *
from tkinter import messagebox
from databases import *
import tkinter as tk
from trucks import TrucksDatabase

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
        # self.trucks = [Gazel(True), Bull(False), Man(False), Fura(False)]
        self.trucks = self.loadTrucks()
        self.main = tk.Tk()
        self.main.geometry('400x300')
        self.main.configure(bg='SkyBlue1')
        self.main.title('ООО "LesyaTrucks"')
        self.loadTrucks()


    def loadTrucks(self):
        db = TrucksDatabase().get_trucks()
        print(db)
        truck_list = []
        for i in db:
            truck_list.append(Truck(i[1], i[2], i[3], i[4], i[5], False))
            ################################################
            # Вот тут последний аргумент - False - это статус грузовика 
            # После того как будешь хранить в базе данных статус - поставь там i[6]
            ################################################
        return truck_list
    

    def renderMainMenu(self):
        # Метод отрисовывает главное меню
        self.menu_frame = tk.Frame(self.main) # Главный фрейм
        self.menu_frame.pack()

        self.menu_label = tk.Label(self.menu_frame, text='Главное меню :', width=30)
        self.menu_label.pack()

        ########################
        # Кнопочки главного меню
        ########################

        button1 = tk.Button(self.menu_frame, text='Просмотреть доступный транспорт', width=30, command=self.renderAvalibleFrame)
        button1.pack()

        button2 = tk.Button(self.menu_frame, text='Создать заявку на перевоз груза', width=30, command=self.renderOrderFrame)
        button2.pack()

        button3 = tk.Button(self.menu_frame, text='Добавить транспорт', width=30, command=self.renderAddingFrame) 
        button3.pack()



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
        try:
            self.weight = int(self.r1.get())
            self.width = int(self.r2.get())
            self.height = int(self.r3.get())
        except:
            messagebox.showerror('Некорректный ввод', 'Проверьте корректность ввода')
        self.av_trucks = []
        for i in self.trucks: 
            if i.weight >= self.weight and i.height >= self.height and i.width >= self.width and not(i.isOrdered): # Проверяем подходит ли каждый грузовик по размерам
                self.av_trucks.append(i)
                self.car = i.name

        self.renderTrucks(self.order_frame, self.av_trucks, 5, True) # Отрисовываем список грузовиков из массива av_trucks

    def backToMenu(self, frame):
        # Метод для кнопки назад
        # Принимает в качестве параметра frame - тот фрейм который нужно удалить (т е текущий, в котором мы были)
        frame.destroy()
        self.renderMainMenu() # Отрисовываем главное меню

    def backToOrder(self, frame):
        frame.destroy()
        self.renderOrderFrame()


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

    def renderAddingFrame(self):
        # Этот метод отрисовывает фрейм добавления машины
        self.menu_frame.destroy()

        self.add_frame = Frame(self.main) # Добавляем фрейм добавления машины
        self.add_frame.pack()
        # Кнопка возвращения в меню
        self.buttonBack = Button(self.add_frame, text='<', command=lambda frame = self.add_frame: self.backToMenu(frame)) # Кнопка для возвращения в главное меню, вызывает функцию backToMenu
        self.buttonBack.grid(row=0, column=0)
        Label(self.add_frame, text='Добавление машины').grid(row=0, column=1)
        self.var = StringVar(value='0')

        Label(self.add_frame, text='Марка грузовика').grid(row=1, column=0)
        self.car1_input = Radiobutton(self.add_frame, text='Газель', variable=self.var, value='Газель').grid(row=1,column=1)
        self.car2_input = Radiobutton(self.add_frame, text='Бычок', variable=self.var, value='Бычок').grid(row=2,column=1)
        self.car3_input = Radiobutton(self.add_frame, text='MAN-10', variable=self.var, value='MAN-10').grid(row=3,column=1)
        self.car4_input = Radiobutton(self.add_frame, text='Фура', variable=self.var, value='Фура').grid(row=4,column=1)

        Label(self.add_frame, text='Грузоподъемность').grid(row=5, column=0)
        self.weight_input = Entry(self.add_frame)
        self.weight_input.grid(row=5, column=1)

        Label(self.add_frame, text='Длина').grid(row=6, column=0)
        self.length_input = Entry(self.add_frame)
        self.length_input.grid(row=6, column=1)
        
        Label(self.add_frame, text='Ширина').grid(row=7, column=0)
        self.width_input = Entry(self.add_frame)
        self.width_input.grid(row=7, column=1)

        Label(self.add_frame, text='Высота').grid(row=8, column=0)
        self.height_input = Entry(self.add_frame)
        self.height_input.grid(row=8, column=1)

        confirm = Button(self.add_frame, text='Подтвердить', command=self.add_truck)
        confirm.grid(row=9, column=1)

    def add_truck(self):
        try:
            self.weight = int(self.weight_input.get())
            self.length = int(self.length_input.get())
            self.width = int(self.width_input.get())
            self.height = int(self.height_input.get())
        except: 
            messagebox.showerror('Некорректный ввод', 'Проверьте корректность ввода') 

        TrucksDatabase().add_truck(self.var.get(), self.weight, self.length, self.width, self.height)
        messagebox.showinfo('ok', 'грузовик добавлен')

    def orderTruck(self, name):
        # Функция которая изменяет статус грузовика на забронированный
        for i in self.trucks:
            if i.name == name: # Находим грузовик в массиве грузовиков по его имени
                i.isOrdered = True # Меняем его статус
                self.renderCustomerFrame()
                break

        
    def renderCustomerFrame(self):
        # Отрисовываем фрейм для оформления заказа
        self.order_frame.destroy()
        
        self.customer_frame = Frame(self.main)
        self.customer_frame.pack()
# <<<<<<< HEAD
# =======

# >>>>>>> 31adb9f3fdd0c5dbe56c8a3399c4a81585b4b7e4
        Button(self.customer_frame, text='<', command=lambda frame = self.order_frame: self.backToOrder(self.customer_frame)).grid(row=0, column=0)
        Label(self.customer_frame, text='Введите свое имя').grid(row=1, column=0)
        self.customer = Entry(self.customer_frame)
        self.customer.grid(row=1, column=1)
# <<<<<<< HEAD
        Button(self.customer_frame, text='Забронировать', command=self.bookTruck).grid(row=2)
    
# =======
        Button(self.customer_frame, text='Забронировать', command=self.bookTruck).grid(row=2, column=1)
        
# >>>>>>> 31adb9f3fdd0c5dbe56c8a3399c4a81585b4b7e4
    def bookTruck(self):
        database = Database()
        database.add_orders(self.customer.get(), self.car, self.weight, self.width, self.height)
        messagebox.showinfo('Успешно', 'Грузовик забронирован')
# <<<<<<< HEAD

# =======
# >>>>>>> 31adb9f3fdd0c5dbe56c8a3399c4a81585b4b7e4

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
        if len(array) == 0:
            messagebox.showerror('Ошибка', 'На данный момент доступных грузовиков \n по данным габаритам нет')
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
        self.trucks = self.loadTrucks()
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

    def start(self):
        self.renderMainMenu()
        self.main.mainloop()

if __name__ == '__main__':
    terminal = Terminal()
    terminal.start()

