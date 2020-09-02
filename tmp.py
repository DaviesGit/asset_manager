import socket
import threading
import json
import re


def link_handle(conn, addr):
    print(addr)
    while 1:
        with open('a.txt', 'r')as file:
            result =file.read()
        result = result.encode()
        conn.send(result)
        x = conn.recv(100).decode()
        print(x)
        if x == '$9991':
            with open('a.txt', 'w+')as file:
                file.write("$9991")
        else:
            with open('a.txt', 'w+')as file:
                file.write("$9990")


if __name__ == "__main__":
    s = socket.socket()
    hp = ("0.0.0.0", 8080)
    s.bind(hp)
    s.listen(5)
    while True:
        conn, addr = s.accept()
        threading.Thread(target=link_handle, args=(conn, addr)).start()
