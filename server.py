# -*- coding: utf-8 -*-
from socket import *
import time, sys, random, math

import pygame # TMP
import pygame.freetype

world = []

mapa = sys.argv[1]
gamers = sys.argv[2]
positive = sys.argv[3]
negative = sys.argv[4]
bots = sys.argv[5]

x = 0
y = 0

sc = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) # Полноэкранный режим
pygame.display.set_caption("World of Shamanic")
clock = pygame.time.Clock()
pygame.init()

#pygame.draw.circle(sc, (0,255,0), (200, 100), 0, 0)

def main():
  print ("Server Shamanica ver 0.1") 
  print ('Map:', sys.argv[1]) # Первый аргумент
  print ('Gamers:', sys.argv[2]) # Второй
  print ('Positive ivents:', sys.argv[3]) # третий
  print ('Negative ivents:', sys.argv[4]) # четвёртый 
  print ('Bots:', sys.argv[5]) # пятый
  createWorld(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
  
def createWorld(ma, ga, po, ne, bo):
    global world, x ,y
    world.clear()
    print ("Creating...")
    ma = int(ma)
    ga = int(ga)
    po = int(po)
    ne = int(ne)
    bo = int(bo)
    
    tmp = int(math.sqrt(ma)) + 1
    ma = (tmp * tmp)
    
    if ma >= 5000 and ma <= 100000: # если задан верный размер карты тогда генерируем её
        ma = int(ma)
        for n in range(ma):
            world.append(n)
            world[n] = 0        
    else: 
        print("Размер карты выходит за диапазон 5000-100000 клеток")
        raise SystemExit(1)
    
    midle = ma / 2
    ma = int(math.sqrt(ma)) # Грань карты x = y = ma
    otklonenie = int(random.random()*2500)
    midle = int((midle) + otklonenie) 
    midleKord = int(math.sqrt(midle)/2) # Координата центра материка x = y = midleKord
    print(midleKord)
    poluostrov = int(random.random()*20) # Колличество полуостровов
    radiusKord = int(int(random.random()*(ma/6))+ (ma/5)) # Радиус материка
        
    for m in range(ma):
        for n in range(ma):
            if x <= midleKord + radiusKord and x >= midleKord - radiusKord and y <= midleKord + radiusKord and y >= midleKord - radiusKord:
                pygame.draw.circle(sc, (0,255,0), (x, y), 0, 0)
            else:
                pygame.draw.circle(sc, (0,0,255), (x, y), 0, 0)  
            x += 1                
        y += 1
        x = 0
    
    
if __name__ == '__main__':
  main()

pygame.display.update()
while True:
    clock.tick(60)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
        elif i.type == pygame.KEYDOWN:    
            if i.key == pygame.K_ESCAPE: #ESC
                pygame.quit()  
                
# Объекты ландшафта:
# 0 - вода, 1 - земля, 2 - гора, 3 - дерево
#
#
#
#


# Аргументы: 
# 1 - размер мира 5000-100000 клеток
# 2 - Колличество игроков 1-5
# 3 - Частота выпадения положительных ивентов 0 - 5
# 4 - Частота выпадения негативных ивентов 0 - 5
# 5 - Колличество поселений ботов 0-5
#
#