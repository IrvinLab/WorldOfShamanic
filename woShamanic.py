# -*- coding: utf-8 -*-
import pygame, sys, random
import pygame.freetype
import threading
import random
import ctypes

setup = 1 # При старте игры равно 1, если выбрано любое меню меняется на ноль
newGame = 0 # Если начата локальная игра = 1
netGame = 0 # Если начата сетевая игра = 1
settings = 0 # Если пользователь в меню настройки = 1
pause = 0 # Если нажата пауза = 1

user32 = ctypes.windll.user32 # Здесь определяем разрешение экрана 
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1) # разрешение экрана дома = (1360, 768)
print(screensize)

sc = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) # Полноэкранный режим
pygame.display.set_caption("World of Shamanic")
clock = pygame.time.Clock()

pygame.init()
pygame.font.init()   

textMainMenu = pygame.font.SysFont('Tahoma', 30) # Текст для кнопок меню

if screensize == (1360, 768):
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

pygame.display.update()
while True:
    clock.tick(60)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
        elif i.type == pygame.KEYDOWN:    
            if i.key == pygame.K_ESCAPE: #ESC
                pygame.quit()    
            elif i.key == pygame.K_1:
                pass
            elif i.key == pygame.K_2:
                pass
            elif i.key == pygame.K_3:
                pass
            elif i.key == pygame.K_4:
                pass
            elif i.key == pygame.K_5:
                pass
            elif i.key == pygame.K_6:
                pass
            elif i.key == pygame.K_7:
                pass
            elif i.key == pygame.K_8:
                pass
            elif i.key == pygame.K_9:
                pass
            elif i.key == pygame.K_0:
                pass
            elif i.key == pygame.K_w:
                pass
            elif i.key == pygame.K_a:
                pass
            elif i.key == pygame.K_s:
                pass
            elif i.key == pygame.K_d:
                pass
            elif i.key == pygame.K_RETURN :
                pass
                print("Enter")
    
    mos_x, mos_y = pygame.mouse.get_pos() # Тут мы берём координаты мыши
    
    if mos_x>980 and (mos_x<1280): x_inside = True # Новая Игра
    else: x_inside = False
    if mos_y>100 and (mos_y<200): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: pass
            if i.button == 3: pass 
    
    if mos_x>980 and (mos_x<1280): x_inside = True # Сетевая Игра
    else: x_inside = False
    if mos_y>202 and (mos_y<302): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: pass
            if i.button == 3: pass

    if mos_x>980 and (mos_x<1280): x_inside = True # Настройки
    else: x_inside = False
    if mos_y>304 and (mos_y<404): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: pass
            if i.button == 3: pass
    
    if mos_x>980 and (mos_x<1280): x_inside = True # Выход
    else: x_inside = False
    if mos_y>406 and (mos_y<506): y_inside = True
    else: y_inside = False
    if x_inside and y_inside: 
        if i.type == pygame.MOUSEBUTTONDOWN and newGame == 0 and netGame == 0 and setup == 1:
            pygame.quit()     