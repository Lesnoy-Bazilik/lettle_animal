from random import *
import time
class Critter:
    day = 1
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
        self.fun = self.hunger + self.boredom
    
    def Specifications(self):
        print("Голод -",self.hunger)
        print("Скука -",self.boredom)
        print("Общее состояние -",self.fun)
        if self.fun >= 2 and self.fun < 4:
            print("Нажмите 'Enter'")
            input()            
            print("Общее состояние - не сказать что хорошо")
            print("Нажмите 'Enter'")
            input()
            self.menu()           
        elif self.fun >= 4 and self.fun < 6:
            print("Нажмите 'Enter'")
            input()            
            print("Общее состояние - Неплохое")
            print("Нажмите 'Enter'")
            input()
            self.menu()        
        elif self. fun >= 6:
            print("Нажмите 'Enter'")
            input()            
            print("Общее состояние - Прекрасное")
            print("Нажмите 'Enter'")
            input()       
            self.menu()
        else:
            print("Нажмите 'Enter'")
            input()            
            print("Общее состояние - Ужасное")
            print("Нажмите 'Enter'")
            input()
            self.menu()
    
    def Eat(self):
        a = randint(1,2)
        print("1 - Дать чу чуть еды")
        print("2 - Покормить нормально")
        print("3 - Дать много еды")
        print("Нажмите 'Enter'")
        input()
        print("Программа рандомным образом определяет выживет или умрет зверюшка")
        print("Нажмите 'Enter'")
        input()
        choice2 = int(input("Ваш выбор: "))
        if choice2 == 1 and a == 1:
            self.hunger += 1
            print("Еда + 1")
            print("Мррр...  Спасибо!")
            Critter.day += 1
            print("Нажмите 'Enter'")
            input()
            self.menu()
        elif choice2 == 1 and a == 2:
            print("Зверюшка умерла от  малого количества еды")
        elif choice2 == 2 and a == 1:
            self.hunger += 1
            print("Еда + 1")
            print("Мррр...  Спасибо!")
            Critter.day += 1
            print("Нажмите 'Enter'")
            input()
            self.menu()             
        elif choice2 == 2 and a == 2:
            print("Зверюшка умерла от  некачественной еды")
        elif choice2 == 3 and a == 1:
            self.hunger += 1
            print("Еда + 1")
            print("Мррр...  Спасибо!")
            Critter.day += 1
            print("Нажмите 'Enter'")
            input()
            self.menu()
        elif choice2 == 3 and choice2 == 2:
            print("Зверюшка умерла от ожирения")
        else:
            print("ОШИБКА!!!")
            print("Нажмите 'Enter'")
            input()
            self.menu()
    
    def game(self):
        b = randint(1,2)
        print("Для вас 1 минута = 1 секунда, 5 минут = 5 секуд, 10 минут = 10 секунд")
        print("1 - Поиграть с зверюшкой 1 мин")
        print("2 - Поиграть с зверюшкой 5 мин")
        print("3 - Поиграть с зверюшкой 10 мин")
        choice3 = int(input("Ваш выбор: "))
        if choice3 == 1 and b == 1:
            print("Играетесь (ждите)")
            time.sleep(1)
            print("Скука += 0.50")
            Critter.day += 1
            self.fun += 0.50
            print("Нажмите 'Enter'")
            input()
            self.menu()
        elif choice3 == 1 and b == 2:
            print("Нажмите 'Enter'")
            input()
            print("Вы не уследили за зверюшкой и ее сбила машина")
        elif choice3 == 2 and b == 1:
            print("Играетесь (ждите)")
            time.sleep(5)
            print("Скука += 0.80")
            Critter.day += 1
            self.fun += 0.80
            print("Нажмите 'Enter'")
            input()
            self.menu
        elif choice3 == 2 and b == 2:
            print("Нажмите 'Enter'")
            input()            
            print("Вы не уследили за зверюшкой. Она провалилась в люк и полетела на небо")
        elif choice3 == 3 and b == 1:
            print("Играетесь (ждите)")
            time.sleep(10)
            print("Скука += 0.50")
            Critter.day += 1
            self.fun += 1
            print("Нажмите 'Enter'")
            input()
            self.menu()
        elif choice3 == 3 and b == 2:
            print("Нажмите 'Enter'")
            input()            
            print("Вы не уследили за зверюшкой и она сбежала")
    
    def process(self):
        choice = int(input("Ваш выбор: "))
        if choice == 0:
            print("Зверюшка будет скучать((")
        elif choice == 1:
            print("Нажмите 'Enter'")
            input()  
            self.Specifications()
        elif choice == 2:
            print("Нажмите 'Enter'")
            input()   
            self.Eat()
        elif choice == 3:
            print("Нажмите 'Enter'")
            input()              
            self.game()

    def menu(self):
        if Critter.day == 10:
            print("Прошло 5 лет и зверюшка умерла")
            if self.fun >= 2 and self.fun < 4:
                print("Зверюшка прожила несчастную жизнь и умерла")
                return 
            elif self.fun >= 4 and self.fun < 6:
                print("Зверюшка прожила обычную жизнь и умерла от старости")
                return 
            elif self. fun >= 6:
                print("Зверюшка прожила ВЕЛИКОЛЕПНУЮ жизнь и умерла от старости(ВЫ ХОРОШИЙ И ВЕЗУЧИЙ ХОЗЯИН)")
                return 
            else:
                print("ЗВЕРЮШКА НЕ ВЫДЕРЖАЛА И УМЕРА")
                return 
        print(Critter.day, "День")
        print(
        (self.name),"""моя зверюшка
        0 - Выйти
        1 - Узнать о самочувствии зверюшки
        2 - Покормить зверюшку
        3 - Поиграть со зверюшкой
        """)
        self.process()
    
    def Explanations(self):
        print("Всего даётся 10 лет для вас 10 дней")
        print("Нажмите 'Enter'")
        input()
        print("Каждый день вы совершаете одно действие либо покормить, либо погулять со зверушкой")
        print("Нажмите 'Enter'")
        input()
        print("Если вы выживаете эти 10 лет и наберете 6 или больше очков(сумируется очки голода и скуки) вы везучий-молодец")
        print("Нажмите 'Enter'")
        input()
        print("В противном случае результат будет хуже")
        print("Нажмите 'Enter'")
        input()
        print("Чем больше число голода и скуки тем лучше самочувствие вашей зверюшки")
        print("Нажмите 'Enter'")
        input()
        print("Вкладка 2. 'Покормить зверюшку' программа вам выдаёт меню где вы можете выбрать как покормить зверюшку")
        print("Рандомным образом программа определяет виживет ли она")   
        print("Если выживет вы получите одно очко голода")
        print("Нажмите 'Enter'")
        input()        
        print("Вкладка 3. 'Играть со зверюшкой' Открываться меню и вы выбираете сколько играть со зверюшкой")
        print("Программа рандомом определит выживет или нет ваша зверюшка")
        print("Если она выжила вы получаете :")
        print("нажали 1 мин результат 0.50 очков")
        print("нажали 5 мин результат 0.80 очков")
        print("нажали 10 мин результат 1 очко")
        self.menu()

def main():
        crit_name = input("Как вы назовете свою зверюшку?: ")
        Crit = Critter(crit_name)
        print("Нажмите 'Enter'")
        input()
        Crit.Explanations()
main()
