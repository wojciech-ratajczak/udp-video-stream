
import socket   

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    #wybrałem sock_Dgram bo UDP wysyła datagramy. deafultowe sock_stream to TCP?

sock.bind(("0.0.0.0", 5000))   #bind mowi oddaj programowi co przyjdzie na: 
#0.0.0.0 oznacza wszystkie interfejsy tego pc, 5000 to port

while True:
    dane, adres = sock.recvfrom(1024)   #recv/recvfrom = "Receive data from the socket."
    print ("Dane: ", dane)
    print ("Adres: ",adres)



