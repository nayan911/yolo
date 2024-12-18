# #!/usr/bin/env python3
# # -- coding: utf-8 --

# import socket

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# port = int(input("Enter the port number as server : "))
# s.connect((socket.gethostbyname('pi') , port)) # here you must past the public external ipaddress of the server machine, not that local address
# def recving():
#     f = open("Captured_image.jpg", "wb")
#     data = None
#     while True:
#         m = s.recv(1024)
#         data = m
#         if m:
#             while m:
#                 m = s.recv(1024)
#                 data += m
#             else:
#                 break
#     f.write(data)
#     f.close()
#     print("Done receiving")

import socket
import cv2
import numpy
client= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# machine=socket.gethostbyname('pi')
# print(machine)
# port=int(input("enter the port"))
port = 2525

client.connect(('192.168.120.145',port))

def reciever():
    print("Receiving the file from server")
    data = b''
    while True:
        chunk = client.recv(4096)
        if not chunk:
            break
        data += chunk
    print("Saving the image")
    with open("Captured_image.jpg", 'wb') as f:
        f.write(data)
    print("File has been received")

reciever()