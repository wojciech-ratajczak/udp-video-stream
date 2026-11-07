import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


sock.sendto(b'hello\n',("192.168.1.38", 5000))  #sendto(bytes, address)
#192.x.x.x to ip w LAN, wczesniej testowalem na loopbacku 127.x.x.x
#tutaj wysylalem sobie na komorke, na telefonie w termux: odbiorca-udp.py
