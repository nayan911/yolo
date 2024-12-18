import socket

import capture

import time



server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

machine =socket.gethostbyname(socket.gethostname())

port=2328


print(machine,port)

server.bind(('192.168.0.105',port))

server.listen()



def sender():

    print(f"[{machine}] waiting for the connection from the client ")

    while True:

        client,address=server.accept()

        print(" Client connected and sending file now")

        print("Capturing Image")

        capture.capt()

        print("image captured")

        file= open("178.jpg",'rb')

        print("image saved")

        data=file.read(40960000)

        print("Reread image and Sending it to client ")

        while True:

            if data:

                client.send(data)

                data=file.read(40960000)

                print("Image sent Sucessfully")

                break

            else:

                print("failed to send data")

                break





sender()



# for pi 