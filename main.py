import pygame, sys, random

pygame.init() # Инициализация движка 
sc = pygame.display.set_mode((0, 0), pygame.NOFRAME) # Делаем окно во весь экран без фреймов
clock = pygame.time.Clock() # Переменная частоты кадров

#pygame.draw.rect(sc, (255, 255, 255), (20, 20, 100, 75)) #Прямоугольник
#pygame.draw.aaline(sc, (255,255,255), [10, 70], [290, 55]) #Сглаженная линия
#pygame.draw.line(sc, (255,255,255), [10, 30], [290, 15], 3) # Не сглаженная линия с толщиной = 3

#pix = pygame.image.load('Images/man_right.png') # Рисуем человечка
#x_len = pix.get_width()
#y_len = pix.get_height()
#sc.blit(pix, (x,y))    

x = 95
y = 95
world = [] # Массив карты
xTmp = 0 # Временные координаты
yTmp = 0
n = 0 # Переменная-счётчик

#infoText = pygame.font.Font(None, 36)
#text1 = infoText.render('Загрузка', 1, (180, 0, 0))
#sc.blit(text1, (10, 50))

pix = pygame.image.load('Images/man.png')
x_len = pix.get_width()
y_len = pix.get_height()
sc.blit(pix, (x,y))

def worldCreate(): # Массив создания игрового мира
    world.clear() # Очищаем все массивы
    #for n in range(250000): # Генерируем карту
    #    world.append(n)
    #    world[n] = random.randint(0,3)     
    
    xTmp = 0
    yTmp = 0
    lal = 0
    for n in range(36):
        for j in range(40):
            if j == 39: yTmp += 32; xTmp = 0
            lal = random.randint(0,2)
            if lal == 0:
                    pix = pygame.image.load('Images/grass.png')
                    x_len = pix.get_width()
                    y_len = pix.get_height()
                    sc.blit(pix, (xTmp,yTmp))
            elif lal == 1:
                    pix = pygame.image.load('Images/grass3.png')
                    x_len = pix.get_width()
                    y_len = pix.get_height()
                    sc.blit(pix, (xTmp,yTmp))
            if lal == 2:
                    pix = pygame.image.load('Images/grass4.png')
                    x_len = pix.get_width()
                    y_len = pix.get_height()
                    sc.blit(pix, (xTmp,yTmp))     
            xTmp += 32           



worldCreate() # Создаём мир
pygame.display.update() # Обновление экрана
while 1: # Основной цикл
    
    
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    
    if pygame.key.get_pressed()[pygame.K_w]: # Если зажата клавиша W
        pass 
    if pygame.key.get_pressed()[pygame.K_a]: # Если зажата клавиша A
        pass      
    if pygame.key.get_pressed()[pygame.K_s]: # Если зажата клавиша S
        pass    
    if pygame.key.get_pressed()[pygame.K_d]: # Если зажата клавиша D
        pass
        
        
                                     
        
    clock.tick(60) # FPS - 60 кадров/сек
    pygame.display.update() # Обновление экрана внутри цикла