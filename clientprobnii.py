'''
# соединение - 1 отправляет 1

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('', 8888))

while True:

       sms = input('Введите собщение серверу: ')
       data2 = str.encode(sms)
       sock.send(data2)

       result = sock.recv(1024)
       if result == '':
              continue
       else:
              print('Сообщение от клиента:', result.decode('utf-8'))


sock.close()

       # connection, server = sock.accept()
       # data = sock.recv(1024)
       #
       # print('Сообщение от сервера::', data.decode('utf-8'))


import socket
import threading

def mess_from_serv():
    while 1:
        data = socket_client.recv(1024)
        print('Сообщение от сервера:', data.decode('utf-8'))

user_name = input("введите ваше имя:  ")
server = '', 8888
s = '', 0

socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


socket_client.bind(s)
socket_client.sendto((user_name+ ' подсоединился к серверу').encode('utf-8'),server)

potok = threading.Thread(target=mess_from_serv)
potok.start()

while 1:
    sms = input('введите что-то: ')
    socket_client.sendto(('[user_name]' +sms).encode('utf-8'), server)


# хороший вариант

import socket

def client():
    host="127.0.0.1"
    port=7000
    s=socket.socket()
    s.connect((host, port))
    msg=str(input("\n -> "))
    encoded_msg=bytes(msg, "utf-8")
    while msg!='q':
        s.send(encoded_msg)
        msg=str(input("\n -> "))
        encoded_msg=bytes(msg, "utf-8")

client()
'''


import socket

def client():
    host="192.168.0.128"
    port=8888
    s=socket.socket()
    s.connect((host, port))
    msg=str(input("\n КЛИЕНТ -> "))
    encoded_msg=bytes(msg, "utf-8")
    while msg!='q':
        s.send(encoded_msg)
        msg=str(input("\n КЛИЕНТ -> "))
        encoded_msg = bytes(msg, "utf-8")

        data = s.recv(1024)  # получаем данные от клиента
        decoded_data = data.decode("utf-8")  # декодируем данные
        if not decoded_data:
            break
        print(" СЕРВЕР -> " + decoded_data)

client()
