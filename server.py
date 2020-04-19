# -*- coding: utf-8 -*-
from socket import *
import time, sys, random, math

world = []

mapa = sys.argv[1]
gamers = sys.argv[2]
positive = sys.argv[3]
negative = sys.argv[4]
bots = sys.argv[5]

def main():
  print ("Server Shamanica ver 0.1") 
  print ('Map:', sys.argv[1]) # Первый аргумент
  print ('Gamers:', sys.argv[2]) # Второй
  print ('Positive ivents:', sys.argv[3]) # третий
  print ('Negative ivents:', sys.argv[4]) # четвёртый 
  print ('Bots:', sys.argv[5]) # пятый
  createWorld(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
  
def createWorld(ma, ga, po, ne, bo):
    global world
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
    otklonenie = int(random.random()*1500)
    midle = int((midle-750) + otklonenie) # Координата центра материка
    midleKord = int(math.sqrt(midle)/2)
    poluostrov = int(random.random()*20) # Колличество полуостровов
    radius = int(int(random.random()*(ma/3))+ (ma/2)) # Радиус материка
    
if __name__ == '__main__':
  main()


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