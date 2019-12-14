import pygame, sys

pygame.init() # Инициализация движка
 
sc = pygame.display.set_mode((0, 0), pygame.NOFRAME) # Делаем окно во весь экран без фреймов

clock = pygame.time.Clock() # Переменная частоты кадров

#pygame.draw.rect(sc, (255, 255, 255), (20, 20, 100, 75)) #Прямоугольник
#pygame.draw.aaline(sc, (255,255,255), [10, 70], [290, 55]) #Сглаженная линия
#pygame.draw.line(sc, (255,255,255), [10, 30], [290, 15], 3) # Не сглаженная линия с толщиной = 3
x = 95
y = 95
pygame.display.update() # Обновление экрана
while 1: # Основной цикл
    
    pygame.draw.circle(sc, (0,255,0), (x, y), 50)
    
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    
    if pygame.key.get_pressed()[pygame.K_w]: # Если зажата клавиша W
        pygame.draw.circle(sc, (0,0,0), (x, y), 50)
        y -= 1
        pygame.draw.circle(sc, (0,255,0), (x, y), 50)
    if pygame.key.get_pressed()[pygame.K_a]: # Если зажата клавиша A
        pygame.draw.circle(sc, (0,0,0), (x, y), 50)
        x -= 1
        pygame.draw.circle(sc, (0,255,0), (x, y), 50)
    if pygame.key.get_pressed()[pygame.K_s]: # Если зажата клавиша S
        pygame.draw.circle(sc, (0,0,0), (x, y), 50)
        y += 1
        pygame.draw.circle(sc, (0,255,0), (x, y), 50)
    if pygame.key.get_pressed()[pygame.K_d]: # Если зажата клавиша D
        pygame.draw.circle(sc, (0,0,0), (x, y), 50)
        x += 1
        pygame.draw.circle(sc, (0,255,0), (x, y), 50)
                                     
        
    clock.tick(60) # FPS - 60 кадров/сек
    pygame.display.update() # Обновление экрана внутри цикла