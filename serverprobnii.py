# соединение - 1 отправляет 1
#
# import socket

# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.bind(('', 8888))
# sock.listen(2)
# conn, add = sock.accept()
#
# while True:
#     result = conn.recv(1024)
#     if result =='':
#         continue
#     else:
#         print('Сообщение от клиента:', result.decode('utf-8'))
#
#
#     sms = input('Введите собщение клиенту: ')
#     data2 = str.encode(sms)
#     conn.send(data2)
#
# sock.close()
#

'''
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 8888))

massiv_clientov =[] # массив с адресами клиентов


while 1:
    data, add = sock.recvfrom(1024)
    print (add[0], add[1])
    if add not in massiv_clientov:
        massiv_clientov.append(add) #добавляем клиента если его нет в массиве

    for clients in massiv_clientov:
        if clients == add:
            continue  #не отправляем данные клиенту, который их прислал

        print('Сообщение от клиента:', data.decode('utf-8'))

        sms = input('Введите собщение клиенту: ')
        data = str.encode(sms)
        sock.sendto(data,clients)
'''

import os, socket


host="192.168.0.128"
port=8888
s=socket.socket() #создаем сокет
s.bind((host, port)) #привязываем сокет к адресу и порту
s.listen(10) #прослушиваем запросы на соединение

def handle_client(s, addr, i):
    while True:
        data=s.recv(1024) #получаем данные от клиента
        decoded_data=data.decode("utf-8") #декодируем данные
        if not decoded_data:

            print("\nсоединение с клиентом  " + str(i) + " разорвано\n")
            break
        print(" КЛИЕНТ " + str(i) + " -> " + decoded_data)
        msg = str(input("\n СЕРВЕР -> "))
        encoded_msg = bytes(msg, "utf-8")
        s.send(encoded_msg)

def server():
    i=1
    while i<=10:
        c, addr=s.accept() # принимаем запрос клиента на установление соединения
        child_pid=os.fork() #создание копии процесса (создание дочернего процесса)
        if child_pid==0: #если процесс дочерний
            print("\nуспешное соединение с клиентом  " + str(i) + str(addr) + "\n")
            handle_client(c, addr, i)
            break
        else:
            i+=1

server()







