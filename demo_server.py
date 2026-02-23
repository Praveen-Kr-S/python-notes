# Server side

import socket
s = socket.socket()
port = 7565
host = socket.gethostname()
s.bind((host, port))
s.listen(3)

while True:
    conn, addr = s.accept()
    print(addr)
    conn.send(b"Hello Pradeepa, I am Sahana..")
    conn.close()