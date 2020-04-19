# -*- coding: utf-8 -*-
import sys, random, socket
print ("World of Shamanic ver 2.1")
sock.bind(('', 10101)) # Открываем порт 10101
sock.listen(100) # Максимально 100 клиентов
conn, addr = sock.accept() # Этот сокет используется для приёма/передачи данных
print 'Connected:', addr


while True:
    data = conn.recv(1024) # Получаем данные порциями по 1 КБайту
    if not data:
        break
    conn.send(data.upper())
    
    
    
    
conn.close() # Закрываем соединение