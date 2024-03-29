import socket

mysock: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(("data.pr4e.org", 80))
cmd: str = "GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n".encode()
mysock.send(cmd)

while True:
    data: str = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end="")

mysock.close()
