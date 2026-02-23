# clinet side

import socket
s = socket.socket()
port = 7565
host = socket.gethostname()
s.connect((host, port))
msg = s.recv(1024)


print(msg)
s.close()

