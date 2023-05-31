from tkinter import *
import tkinter as tk

class Truck(): # класс родителя, содержащий информацию по умолчанию о каждом грузовике
    def __init__(self, name, weight, length, width, height, isOrdered):
        self.name = name
        self.weight = weight
        self.length = length
        self.width = width
        self.height = height
        self.isOrdered = isOrdered 
    
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
        self.menu_frame = tk.Frame(self.main)
        self.menu_frame.pack()

        self.menu_label = tk.Label(self.menu_frame, text='Главное меню :', width=300, bg='#B3E5FC')
        self.menu_label.pack()

        button1 = tk.Button(self.menu_frame, text='Просмотреть доступный транспорт', width=30, command=self.renderAvalibleFrame)
        button1.pack()

        button2 = tk.Button(self.menu_frame, text='Создать заявку на перевоз груза', width=30, command=self.renderOrderFrame)
        button2.pack()

        # button3 = tk.Button(self.menu_frame, text='Просмотреть транспорт \n по грузоподъемности', width=30)
        # button3.pack()

        # button4 = tk.Button(self.menu_frame, text='Подобрать и забронировать транспорт', width=30)
        # button4.pack()

        # button5 = tk.Button(self.menu_frame, text='Посмотреть занятый транспорт', width=30)
        # button5.pack()



    def renderOrderFrame(self):
        # Этот метод отрисовывает экран заказа

        self.menu_frame.destroy() # удаляем экран с главным меню 

        self.order_frame = Frame(self.main)

        self.buttonBack = Button(self.order_frame, text='<', command=lambda frame = self.order_frame: self.backToMenu(frame))
        self.buttonBack.grid(row=0, column=0)
        Label(self.order_frame, text='Оформление заказа').grid(row=0, column=1)

        self.label1 = Label(self.order_frame, text='Вес груза').grid(row=1, column=0)
        self.r1 = Entry(self.order_frame)
        self.r1.grid(row=1, column=1)
        

        self.label2 = Label(self.order_frame, text='Длина груза').grid(row=2, column=0)
        self.r2 = Entry(self.order_frame)
        self.r2.grid(row=2, column=1)
        
        

        self.label3 = Label(self.order_frame, text='Высота груза').grid(row=3, column=0)
        self.r3 = Entry(self.order_frame)
        self.r3.grid(row=3, column=1)

        self.orderButton = Button(self.order_frame, text='Подобрать', command=self.orderb)
        self.orderButton.grid(row=4, column=0, columnspan=3)

        self.order_frame.pack()

    def orderb(self):
        print("!!!")
        weight = int(self.r1.get())
        width = int(self.r2.get())
        height = int(self.r3.get())
        self.av_trucks = []
        for i in self.trucks: 
            if i.weight >= weight and i.height >= height and i.width >= width and not(i.isOrdered):
                self.av_trucks.append(i)
        print(self.av_trucks)
        self.renderTrucks(self.order_frame, self.av_trucks, 5, True)
  
        
        
        


    def backToMenu(self, frame):
        # Метод для кнопки назад
        frame.destroy()
        self.renderMainMenu()


    def changeSort(self):

        self.renderTruckList = self.renderTruckList[::-1]
        if self.filterButton['text'] == '↑':
            self.filterButton.config(text='↓')
        else:
            self.filterButton.config(text='↑')
        self.trucks_frame.destroy()
        self.renderTrucks(self.available_frame, self.renderTruckList, 1)

    def sortByWeight(self):
        swapped = False
        arr = self.renderTruckList

        for n in range(len(arr)-1, 0, -1):
            for i in range(n):
                if arr[i].weight > arr[i + 1].weight:
                    swapped = True
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]       
            if not swapped: return

    def orderTruck(self, name):
        for i in self.trucks:
            if i.name == name:
                i.isOrdered = True 
                break
        


    def renderTrucks(self, parent_frame, array,r, orderMode=False):
        print(array)
        try: self.trucks_frame.destroy()
        except: pass
        self.trucks_frame = Frame(parent_frame)
        for i in range(len(array)):    

            Label(self.trucks_frame, text=array[i].name).grid(row=i, column=1)
            Label(self.trucks_frame, text=array[i].weight).grid(row=i, column=2)
            if orderMode:
                Button(self.trucks_frame, text='Забронировать', command=lambda name = array[i].name: self.orderTruck(name)).grid(row=i, column=3)
        self.trucks_frame.grid(row=r, columnspan=3)


    def fitlerTrucks(self, arr, ordered=None):
        print(self.trucks)
        self.renderTruckList = []
        if ordered==None:
            self.renderTruckList = self.trucks
        for i in arr:
            if ordered:
                if i.isOrdered:
                    self.renderTruckList.append(i)
            else:
                if not(i.isOrdered):
                    self.renderTruckList.append(i)
        # print(a)
        return self.renderTruckList
    
    def filterByStatus(self):
        self.filterMode+=1
        print(self.filterMode)
        if self.filterMode%3==0:
            self.filterStatusButton.config(text='Все')
            print(self.filterMode)
            self.sortByWeight()
            self.renderTruckList = self.trucks
            self.renderTrucks(self.available_frame, self.trucks, 1)
        elif self.filterMode%3==1:
            self.filterStatusButton.config(text='Занятые')
            print(self.filterMode)
            self.sortByWeight()
            self.renderTrucks(self.available_frame, self.fitlerTrucks(self.trucks, True), 1)
        else:
            print(self.filterMode)
            self.filterStatusButton.config(text='Свободные')
            self.sortByWeight()
            self.renderTrucks(self.available_frame, self.fitlerTrucks(self.trucks, False), 1)

        pass 
 
    def renderAvalibleFrame(self):
        self.menu_frame.destroy()
        self.available_frame = Frame(self.main)
        self.buttonBack = Button(self.available_frame, text='<', command=lambda frame = self.available_frame:self.backToMenu(frame))
        self.buttonBack.grid(row=0, column=0)
        self.label1 = Label(self.available_frame, text='Тип грузовика').grid(row=0, column=1)
        self.label2 = Label(self.available_frame, text='Грузоподъемность').grid(row=0, column=2)
        self.filterButton = Button(self.available_frame, text='↑', command=self.changeSort)
        self.filterButton.grid(row=0, column=3)
        self.filterMode = -1
        self.filterStatusButton = Button(self.available_frame, text='Свободные', command=self.filterByStatus)
        self.filterStatusButton.grid(row=0, column=4)
        self.renderTruckList = self.trucks
        self.filterByStatus()
        # self.sortByWeight()
        # self.renderTrucks(self.available_frame, self.trucks, 1)
        
        self.available_frame.pack()
          
        
    def start(self):
        self.renderMainMenu()
        self.main.mainloop()

if __name__ == '__main__':
    terminal = Terminal()
    terminal.start()

