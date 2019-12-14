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
        
        if i.type == pygame.MOUSEMOTION: # Движение мышью
            x,y= i.pos
        
        elif i.type == pygame.MOUSEBUTTONDOWN: # Нажатия кнопок мыши event.button = 1 - ЛКМ 2 - Средняя 3 - правая кнопка 4 - скролл вверх 5 - скролл вниз
            if i.button == 1:  #  левая кнопка мыши
                x,y = i.pos
            if i.button == 3:  # правая кнопка мыши
                x,y = i.pos       
    
        elif i.type == pygame.KEYDOWN: # Если клавиша нажата
            if i.key == pygame.K_w: # Клавиша W
                pygame.draw.circle(sc, (0,0,0), (x, y), 50)
                y -= 10
            elif i.key == pygame.K_a:  # Клавиша A    
                pygame.draw.circle(sc, (0,0,0), (x, y), 50)
                x -= 10
            elif i.key == pygame.K_s:  # Клавиша S     
                pygame.draw.circle(sc, (0,0,0), (x, y), 50)
                y += 10
            elif i.key == pygame.K_d: # Клавиша D     
                pygame.draw.circle(sc, (0,0,0), (x, y), 50)
                x += 10       
    
    clock.tick(60) # FPS - 60 кадров/сек
    pygame.display.update() # Обновление экрана внутри цикла