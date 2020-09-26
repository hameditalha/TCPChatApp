from colorama import Fore, Style                            #for styling and coloring
import socket                                               #for communication
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     #TCP socket initiation
port = 1025                                                 #defining port to connect on
host = socket.gethostname()                                 #getting host name
print('Starting ' + host)
soc.bind((host, port))                                      #biding host to port
print('Waiting for incoming connection')
soc.listen(1)                                               #listening to 1 client
client, address = soc.accept()                              #accepting connection request
print('Connected to ', address[0], 'on', address[1])
while True: 
   recv = client.recv(1024)                                 #recieving message
   recv = recv.decode()                                     #decoding recieved message
   print(f'{Fore.BLUE}', recv)
   if recv == 'quit':                                       #quiting app on condition
      break
   sen = input(f'{Fore.GREEN}> ')                           #taking message in to send
   sen = sen.encode()                                       #encoding to send
   client.send(sen)                                         #sending
   if sen.decode() == 'quit':                               #quiting app on condition
      break
soc.close()                                                 #closing socket after use
print(f'{Fore.RED}Chat ended{Style.RESET_ALL}')