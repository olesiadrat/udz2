from tkinter import *
import tkinter as tk

class Truck(): # класс родителя, содержащий информацию по умолчанию о каждом грузовике
    def __init__(self, name, weight, length, width, height):
        self.name = name
        self.weight = weight
        self.length = length
        self.width = width
        self.height = height
    
    def get_weight(self):
        return self.weight
    
    def get_length(self):
        return self.length
    
    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height

class Gazel(Truck):
    def __init__(self):
        name = 'Газель'
        weight = 2
        length = 3
        width = 2
        height = 2.2
        super().__init__(name, weight, length, width, height)

class Bull(Truck):
    def __init__(self):
        name = 'Бычок'
        weight = 3
        length = 5
        width = 2.2
        height = 2.4
        super().__init__(name, weight, length, width, height)

class Man(Truck):
    def __init__(self):
        name = 'MAN-10'
        weight = 10
        length = 8
        width = 2.45
        height = 2.7
        super().__init__(name, weight, length, width, height)

class Fura(Truck):

    def __init__(self):
        name = 'Фура'
        weight = 20
        length = 13.6
        width = 2.46
        height = 2.7
        super().__init__(name, weight, length, width, height)

class Terminal():
    def __init__(self):
        self.order = []
        self.trucks = [Gazel(), Bull(), Man(), Fura()]

        self.main = tk.Tk()
        self.main.geometry('300x300')
        self.main.configure(bg='SkyBlue1')
        self.main.title('ООО "LesyaTrucks"')
        # с помощью функции label() делаем метку главного меню
        self.menu_label = tk.Label(self.main, text='Главное меню :', width=300, bg='#B3E5FC')
        self.menu_label.pack()

        self.menu_frame = tk.Frame(self.main)
        self.menu_frame.pack()

        button1 = tk.Button(self.menu_frame, text='Просмотреть доступный транспорт', width=30, command=self.available)
        button1.pack()

        button2 = tk.Button(self.menu_frame, text='Создать заявку на перевоз груза', width=30, command=self.order)
        button2.pack()

        button3 = tk.Button(self.menu_frame, text='Просмотреть транспорт \n по грузоподъемности', width=30)
        button3.pack()

        button4 = tk.Button(self.menu_frame, text='Подобрать и забронировать транспорт', width=30)
        button4.pack()

        button5 = tk.Button(self.menu_frame, text='Посмотреть занятый транспорт', width=30)
        button5.pack()
    def order(self):

        self.label1 = tk.Label(text='Вес груза')
        self.r1 = Entry()
        self.r1.pack()
        self.label1.pack()

        self.label2 = tk.Label(text='Длина груза')
        self.r2 = Entry()
        self.r2.pack()
        self.label2.pack()

        self.label3 = tk.Label(text='Высота груза')
        self.r3 = Entry()
        self.r3.pack()
        self.label3.pack()

    def available(self):

        self.label1 = tk.Label(text='Тип грузовика')
        # self.label1.place_configure(x=100,y=50)
        self.label1.pack() 

        self.label2 = tk.Label(text='Грузоподъемность')
        self.label2.pack()
        for obj in self.trucks:
            self.label = tk.Label(self.menu_frame, text=obj.name)
            self.label.pack()
          
        
    def start(self):
        self.main.mainloop()
    """def menu(self):
        while True:
            choice = input('Выберите, что требуется сделать: \n'
                           '1 - Просмотр грузовиков по грузоподъемности \n'
                           '2 - Просмотр доступного транспорта \n'
                           '0 - Выйти из меню'
                           )
            if choice == '0':
                break
            elif choice == '1':
                for obj in self.trucks:
                    print(f'Тип грузовика: {obj.name}, грузоподъемность(тонн): {obj.weight}')
            elif choice == '2':
                for obj in self.trucks:
                    print('На данный момент есть несколько доступных грузовиков: \n' )
"""
        
if __name__ == '__main__':
    terminal = Terminal()
    terminal.start()

