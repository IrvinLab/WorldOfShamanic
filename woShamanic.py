# -*- coding: utf-8 -*-
import pygame, sys, socket
from playsound import playsound
import pygame.freetype
import threading
import random
import ctypes

setup = 1 # При старте игры равно 1, если выбрано любое меню меняется на ноль
newGame = 0 # Если начата локальная игра = 1
netGame = 0 # Если начата сетевая игра = 1
settings = 0 # Если пользователь в меню настройки = 1
pause = 0 # Если нажата пауза = 1
inputText = 0 # Равна 1 если юзер вводит текст
thisText = 0 # Определяем куда вводим текст 1-поле IP, 2 - племя
chatText = "" # Любой текст, который вводит пользователь
ip = "" # IP/домен сервера
fraction = "" # Имя племени
xText = 0 # X,Y любого вводимого пользователем текста
yText = 0
worldLog = [" "," "," "," "," "," "] # Лог игры
yLog = 0


jiteli = 0 # Число племянных жителей
konfessia = 0 # Конфессия

user32 = ctypes.windll.user32 # Здесь определяем разрешение экрана 
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1) # разрешение экрана дома = (1360, 768)
print(screensize)

sc = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) # Полноэкранный режим
pygame.display.set_caption("World of Shamanic")
clock = pygame.time.Clock()

pygame.init()
pygame.font.init()   

textMainMenu = pygame.font.SysFont('Tahoma', 30) # Текст для кнопок главного меню
textRightMenu = pygame.font.SysFont('Tahoma', 20) # Текст для правого меню

def printMainMenu(myScreen, variant):
    # Переменная variant:
    # 0 - Первый запуск игры
    # 1 - Новая Игра
    # 2 - Сетевая Игра (сразу после нажатия на кнопку)
    if myScreen == (1360, 768): # Устанавливаем параметры отбражения для разных элементов игры
        if variant == 0:
            pygame.draw.rect(sc, (255, 255, 255), (0, 0, 900, 600))
            # Рисуем кнопки меню
            pix = pygame.image.load('Images/menuButton.png') 
            x_len = pix.get_width()
            y_len = pix.get_height() 
            sc.blit(pix, (980,100))
            pix = pygame.image.load('Images/menuButton.png') 
            x_len = pix.get_width()
            y_len = pix.get_height() 
            sc.blit(pix, (980,202))
            pix = pygame.image.load('Images/menuButton.png') 
            x_len = pix.get_width()
            y_len = pix.get_height() 
            sc.blit(pix, (980,304))
            pix = pygame.image.load('Images/menuButton.png') 
            x_len = pix.get_width()
            y_len = pix.get_height() 
            sc.blit(pix, (980,406))
            varMainMenu = u"Новая Игра"
            mainMemuObj = textMainMenu.render(varMainMenu, False, (255, 255, 255))
            sc.blit(mainMemuObj,(1055, 130))
            varMainMenu = u"Сетевая Игра"
            mainMemuObj = textMainMenu.render(varMainMenu, False, (255, 255, 255))
            sc.blit(mainMemuObj,(1037, 232))
            varMainMenu = u"Настройки"
            mainMemuObj = textMainMenu.render(varMainMenu, False, (255, 255, 255))
            sc.blit(mainMemuObj,(1057, 334))
            varMainMenu = u"Выход"
            mainMemuObj = textMainMenu.render(varMainMenu, False, (255, 255, 255))
            sc.blit(mainMemuObj,(1084, 436))

        if variant == 2:
            pygame.draw.rect(sc, (0, 0, 0), (901, 0, 1400, 800)) # Убираем все кнопки
            pygame.draw.rect(sc, (225, 225, 225), (950, 155, 250, 45), 2) # Поле для IP
            pygame.draw.rect(sc, (225, 225, 225), (950, 225, 250, 45), 2) # Поле для имени племени
            varMainMenu = u"Сетевая Игра"
            mainMemuObj = textMainMenu.render(varMainMenu, False, (255, 255, 255))
            sc.blit(mainMemuObj,(1040, 90)) 
            varRightMenu = u"Введите IP или доменное имя сервера"
            rightMenuObj = textRightMenu.render(varRightMenu, False, (255, 255, 255))
            sc.blit(rightMenuObj,(950, 130))
            varRightMenu = u"Введите имя племени"
            rightMenuObj = textRightMenu.render(varRightMenu, False, (255, 255, 255))
            sc.blit(rightMenuObj,(950, 200))
            varRightMenu = u"Выберите количество племенных жителей"
            rightMenuObj = textRightMenu.render(varRightMenu, False, (255, 255, 255))
            sc.blit(rightMenuObj,(950, 270)) 
            pygame.draw.rect(sc, (225, 225, 225), (950, 300, 64, 64), 2)  # 1  житель
            pygame.draw.rect(sc, (225, 225, 225), (1018, 300, 64, 64), 2) # 3  жителя
            pygame.draw.rect(sc, (225, 225, 225), (1086, 300, 64, 64), 2) # 5  жителей
            pygame.draw.rect(sc, (225, 225, 225), (1154, 300, 64, 64), 2) # 7  жителей
            pygame.draw.rect(sc, (225, 225, 225), (1222, 300, 64, 64), 2) # 10 жителей
            varRightMenu = u"1          3         5          7        10" # 1 3 5 7 10
            rightMenuObj = textRightMenu.render(varRightMenu, False, (255, 255, 255))
            sc.blit(rightMenuObj,(977, 317))
            varRightMenu = u"Выберите конфессию Вашего племени"
            rightMenuObj = textRightMenu.render(varRightMenu, False, (255, 255, 255))
            sc.blit(rightMenuObj,(950, 370))
            pygame.draw.rect(sc, (225, 225, 225), (950, 400, 64, 64), 2) # Это
            pygame.draw.rect(sc, (225, 225, 225), (1018, 400, 64, 64), 2) # Пять
            pygame.draw.rect(sc, (225, 225, 225), (1086, 400, 64, 64), 2) # Конфессий
            pygame.draw.rect(sc, (225, 225, 225), (1154, 400, 64, 64), 2) # Доступных
            pygame.draw.rect(sc, (225, 225, 225), (1222, 400, 64, 64), 2) # Пользователю
            pix = pygame.image.load('Images/menuButton.png') 
            x_len = pix.get_width()
            y_len = pix.get_height() 
            sc.blit(pix, (980,500))
            varMainMenu = u"Старт"
            mainMemuObj = textMainMenu.render(varMainMenu, False, (255, 255, 255))
            sc.blit(mainMemuObj,(1090, 527))            
            
            pygame.display.update() #Обновляем экран в конце функции
            
    
    
    
printMainMenu(screensize, 0)

def printLog(stroka): # Выводим лог игры вниз
    global worldLog
    if stroka != 0:
        pygame.draw.rect(sc, (0, 0, 0), (16, 610, 888, 300))
        tmp1 = worldLog[1]
        tmp2 = worldLog[2]
        tmp3 = worldLog[3]
        tmp4 = worldLog[4]
        tmp5 = worldLog[5]
        worldLog=[tmp1,tmp2,tmp3,tmp4,tmp5,stroka]
        yLog = 610
        for n in range(6):
            varRightMenu = worldLog[n]
            rightMenuObj = textRightMenu.render(varRightMenu, False, (0, 255, 0))
            sc.blit(rightMenuObj,(16, yLog))
            yLog += 17
        pygame.display.update() 

def netGaming():
    printMainMenu(screensize, 2)
    
def pressAnyKey(sumbol, textLocation):
    global inputText, chatText, ip, fraction, xText, yText
    if sumbol != '' and inputText == 1:
        if sumbol == "back": 
            chatText = ""
            sumbol = ""
            if textLocation == 1: pygame.draw.rect(sc, (0, 0, 0), (952, 157, 248, 43))
            if textLocation == 2: pygame.draw.rect(sc, (0, 0, 0), (952, 227, 248, 43))
        if sumbol != "enter": chatText += sumbol # Если не введён Enter
        
        if textLocation == 1 and sumbol != "enter" and sumbol != "back": # Юзер вводит IP/домен
            ip = chatText
            xText = 955
            yText = 160
        if textLocation == 2 and sumbol != "enter" and sumbol != "back": # Юзер вводит имя племени
            fraction = chatText
            xText = 955
            yText = 230
        
        print(chatText)
        if sumbol == "enter": print("= ", chatText)
        varRightMenu = chatText
        rightMenuObj = textRightMenu.render(varRightMenu, False, (0, 255, 0))
        sc.blit(rightMenuObj,(xText, yText))
        pygame.display.update() #Обновляем экран в конце функции        
    
pygame.display.update()
while True:
    clock.tick(60)
    if inputText == 0: xText = 0; yText = 0
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
        elif i.type == pygame.KEYDOWN:    
            if i.key == pygame.K_ESCAPE: #ESC
                pygame.quit()    
            elif i.key == pygame.K_1:
                pressAnyKey("1", thisText)
            elif i.key == pygame.K_2:
                pressAnyKey("2", thisText)
            elif i.key == pygame.K_3:
                pressAnyKey("3", thisText)
            elif i.key == pygame.K_4:
                pressAnyKey("4", thisText)
            elif i.key == pygame.K_5:
                pressAnyKey("5", thisText)
            elif i.key == pygame.K_6:
                pressAnyKey("6", thisText)
            elif i.key == pygame.K_7:
                pressAnyKey("7", thisText)
            elif i.key == pygame.K_8:
                pressAnyKey("8", thisText)
            elif i.key == pygame.K_9:
                pressAnyKey("9", thisText)
            elif i.key == pygame.K_0:
                pressAnyKey("0", thisText)
            elif i.key == pygame.K_q:
                pressAnyKey("q", thisText)
            elif i.key == pygame.K_w:
                pressAnyKey("w", thisText)
            elif i.key == pygame.K_e:
                pressAnyKey("e", thisText)
            elif i.key == pygame.K_r:
                pressAnyKey("r", thisText)
            elif i.key == pygame.K_t:
                pressAnyKey("t", thisText)
            elif i.key == pygame.K_y:
                pressAnyKey("y", thisText)
            elif i.key == pygame.K_u:
                pressAnyKey("u", thisText)
            elif i.key == pygame.K_i:
                pressAnyKey("i", thisText)
            elif i.key == pygame.K_o:
                pressAnyKey("o", thisText)
            elif i.key == pygame.K_p:
                pressAnyKey("p", thisText) 
            elif i.key == pygame.K_a:
                pressAnyKey("a", thisText)
            elif i.key == pygame.K_s:
                pressAnyKey("s", thisText)
            elif i.key == pygame.K_d:
                pressAnyKey("d", thisText)
            elif i.key == pygame.K_f:
                pressAnyKey("f", thisText)
            elif i.key == pygame.K_g:
                pressAnyKey("g", thisText)
            elif i.key == pygame.K_h:
                pressAnyKey("h", thisText)
            elif i.key == pygame.K_j:
                pressAnyKey("j", thisText)
            elif i.key == pygame.K_k:
                pressAnyKey("k", thisText)
            elif i.key == pygame.K_l:
                pressAnyKey("l", thisText)
            elif i.key == pygame.K_z:
                pressAnyKey("z", thisText)
            elif i.key == pygame.K_x:
                pressAnyKey("x", thisText)
            elif i.key == pygame.K_c:
                pressAnyKey("c", thisText)
            elif i.key == pygame.K_v:
                pressAnyKey("v", thisText)
            elif i.key == pygame.K_b:
                pressAnyKey("b", thisText)
            elif i.key == pygame.K_n:
                pressAnyKey("n", thisText)
            elif i.key == pygame.K_m:
                pressAnyKey("m", thisText)
            elif i.key == pygame.K_PERIOD:
                pressAnyKey(".", thisText)
            elif i.key == pygame.K_BACKSPACE:
                pressAnyKey("back", thisText)                
            elif i.key == pygame.K_RETURN:
                pressAnyKey("enter", thisText)
                thisText = 0
                print("Enter")
    
    mos_x, mos_y = pygame.mouse.get_pos() # Тут мы берём координаты мыши
    
    if mos_x>980 and (mos_x<1280): x_inside = True # Новая Игра
    else: x_inside = False
    if mos_y>100 and (mos_y<200): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN and newGame == 0 and netGame == 0 and setup == 1:
            if i.button == 1: playsound('Sounds/select.wav')
            if i.button == 3: pass 
    
    if mos_x>980 and (mos_x<1280): x_inside = True # Сетевая Игра
    else: x_inside = False
    if mos_y>202 and (mos_y<302): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN and newGame == 0 and netGame == 0 and setup == 1:
            if i.button == 1: netGame = 1; netGaming(); playsound('Sounds/select.wav')
            if i.button == 3: pass

    if mos_x>980 and (mos_x<1280): x_inside = True # Настройки
    else: x_inside = False
    if mos_y>304 and (mos_y<404): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN and newGame == 0 and netGame == 0 and setup == 1:
            if i.button == 1: playsound('Sounds/select.wav')
            if i.button == 3: pass
    
    if mos_x>980 and (mos_x<1280): x_inside = True # Выход
    else: x_inside = False
    if mos_y>406 and (mos_y<506): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN and newGame == 0 and netGame == 0 and setup == 1:
            playsound('Sounds/select.wav')
            pygame.quit()

    if mos_x>950 and (mos_x<1200): x_inside = True # Ввод IP
    else: x_inside = False
    if mos_y>155 and (mos_y<200): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN and netGame == 1 and setup == 1:
            if i.button == 1: inputText = 1; thisText = 1; chatText = ""
            if i.button == 3: inputText = 1; thisText = 1; chatText = ""

    if mos_x>950 and (mos_x<1200): x_inside = True # Ввод имени племени
    else: x_inside = False
    if mos_y>225 and (mos_y<270): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN and netGame == 1 and setup == 1:
            if i.button == 1: inputText = 1; thisText = 2; chatText = ""
            if i.button == 3: inputText = 1; thisText = 2; chatText = "" 
#================================================================================================================    
    if mos_x>950 and (mos_x<1014): x_inside = True # Выбираем 1 колониста
    else: x_inside = False
    if mos_y>300 and (mos_y<364): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN and netGame == 1 and setup == 1:
            if i.button == 1: printLog("Число племенных жителей = 1"); jiteli = 1; playsound('Sounds/select.wav')
            if i.button == 3: pass

    if mos_x>1018 and (mos_x<1082): x_inside = True # Выбираем 3 колониста
    else: x_inside = False
    if mos_y>300 and (mos_y<364): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN and netGame == 1 and setup == 1:
            if i.button == 1: printLog("Число племенных жителей = 3"); jiteli = 3; playsound('Sounds/select.wav')
            if i.button == 3: pass  

    if mos_x>1086 and (mos_x<1150): x_inside = True # Выбираем 5 колониста
    else: x_inside = False
    if mos_y>300 and (mos_y<364): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN and netGame == 1 and setup == 1:
            if i.button == 1: printLog("Число племенных жителей = 5"); jiteli = 5; playsound('Sounds/select.wav')
            if i.button == 3: pass  

    if mos_x>1154 and (mos_x<1218): x_inside = True # Выбираем 7 колониста
    else: x_inside = False
    if mos_y>300 and (mos_y<364): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN and netGame == 1 and setup == 1:
            if i.button == 1: printLog("Число племенных жителей = 7"); jiteli = 7; playsound('Sounds/select.wav')
            if i.button == 3: pass  

    if mos_x>1222 and (mos_x<1286): x_inside = True # Выбираем 10 колониста
    else: x_inside = False
    if mos_y>300 and (mos_y<364): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN and netGame == 1 and setup == 1:
            if i.button == 1: printLog("Число племенных жителей = 10"); jiteli = 10; playsound('Sounds/select.wav')
            if i.button == 3: pass             
#====================================================================================================================

    if mos_x>950 and (mos_x<1014): x_inside = True # Атеисты
    else: x_inside = False
    if mos_y>400 and (mos_y<464): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN and netGame == 1 and setup == 1:
            if i.button == 1: 
                printLog("Атеизм - миролюбивое течение, ориентированное на развитие технологий и исследование ")
                printLog("материального мира. Атеисты получают +3 к интеллекту, +1 к психической устойчивости")
                printLog("Не получают баф к настроению за посещение любых храмов. За посещение ритуала")
                printLog("возможен баф к настроению +1 и +2 развлечение. Дебафы -5 поток энергии, -1 общение")
                printLog("Случайным образом могут получить дебаф к настроению -2 Меланхолия и ленность")
                printLog("Отношение к существам с другим мировозрением - нейтральное")
                konfessia = 1
                playsound('Sounds/select.wav')
            if i.button == 3: pass

    if mos_x>1018 and (mos_x<1082): x_inside = True # Слуги Хаоса
    else: x_inside = False
    if mos_y>400 and (mos_y<464): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN and netGame == 1 and setup == 1:
            if i.button == 1:
                printLog("Слуги Хаоса - агрессивное религиозное течение, главной целью которого - истребление")
                printLog("всего живого во славу Великого Экзостианеса. Слуги Хаоса получают +3 к ближнему бою")
                printLog("-2 к психической устойчивости, -2 к общению. Если ежемесечно совершать жертвоприношение")
                printLog("на специальном алтаре, Слуги Хаоса получают +5 к настроению, в противном случае -5.")
                printLog("За посещение Храма Крови получают баф к настроению +1 и совершение доп. обрядов")
                printLog("Негативное отношение ко всем остальным конфессиям и их приверженцам")
                konfessia = 2
                playsound('Sounds/select.wav')
            if i.button == 3: pass  

    if mos_x>1086 and (mos_x<1150): x_inside = True # Димиургионизм
    else: x_inside = False
    if mos_y>400 and (mos_y<464): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN and netGame == 1 and setup == 1:
            if i.button == 1: 
                printLog("Димиугионизм - миролюбивое религиозное течение, суть которого сеять красоту и гармонию")
                printLog("во круг себя во Имя бога красоты и симметрии - Димиурга.")
                printLog("Бафы +3 к креативу +1 инженерное дело, -1 к ближнему и дальнему бою, +2 общение")
                printLog("За убийство любого существо получают дебаф к настроению -1, который может суммироваться")
                printLog("до -20 в зависимости от количества и способа убийств.")
                printLog("Положительно относятся к Шаманам и Тофорианцам, негативно к Слугам Хаоса")
                konfessia = 3
                playsound('Sounds/select.wav')
            if i.button == 3: pass  

    if mos_x>1154 and (mos_x<1218): x_inside = True # Шаманизм
    else: x_inside = False
    if mos_y>400 and (mos_y<464): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN and netGame == 1 and setup == 1:
            if i.button == 1: 
                printLog("Шаманизм - система учений и практик ориентированное на целительство. Шаман, общаясь")
                printLog("с духами способен получать знания из далёких миров, совершая особый ежегодный ритуал.")
                printLog("Бафы +3 к потоку энергии, +2 к медицине, +2 к интеллекту. Дебафы -4 психической")
                printLog("устойчивости, -1 ближный бой, может впасть в транс на случайное колличество времени.")
                printLog("При виде тотема или идола получают баф +1 к настроению.")
                printLog("Положительно относятся к Атеистам и негативно к Слугам Хаоса")
                konfessia = 4
                playsound('Sounds/select.wav')
            if i.button == 3: pass  

    if mos_x>1222 and (mos_x<1286): x_inside = True # Тофорианизм
    else: x_inside = False
    if mos_y>400 and (mos_y<464): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN and netGame == 1 and setup == 1:
            if i.button == 1: 
                printLog("Тофорианизм - миролюбивиое религиозное течение, суть которого - восхваление Тофо.")
                printLog("Божества, несущего добро, любовь и порядок. Бафы +1 к настроению, +2 Общение")
                printLog("+1 психическая устойчивость, +1 поток энергии, в бою способны получить +10 к")
                printLog("здоровью с вероятностью 5%. Баф к настроению +2 за ритуалы и праздники")
                printLog("Дебафы -1 дальний и ближний бой, -2 интеллект,  -2 мана")
                printLog("Положительно относятся к Димиургионистам и негативно к Слугам Хаоса и Шаманам")
                konfessia = 5
                playsound('Sounds/select.wav')
            if i.button == 3: pass
#===========================================================================================================================================

    if mos_x>980 and (mos_x<1280): x_inside = True # Старт сетевой игры
    else: x_inside = False
    if mos_y>500 and (mos_y<600): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN and netGame == 1 and setup == 1:
            if i.button == 1: print(ip, fraction); playsound('Sounds/start.wav')
            if i.button == 3: pass             