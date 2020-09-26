from colorama import Fore, Style                            #for styling and coloring
import socket                                               #for communication
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     #TCP socket initiation
server = input('Server to connect?\n>')
port = 1025                                                 #defining port to connect on
try:
   soc.connect((server, port))                              #connecting to host on defined port
   print('Connected to ', server)
except:
   print('error 404 : server not found')                    #wrong host name
   soc.close()                                              #closing socket after use
while (True):
   rec = soc.recv(1024)                                     #recieving message
   rec = rec.decode()                                       #decoding recieved message
   print(f'{Fore.BLUE}', rec)
   if rec == 'quit':                                        #quiting app on condition
      break
   sen = input(f'{Fore.GREEN}> ')                           #taking message in to send
   sen = sen.encode()                                       #encoding to send
   soc.send(sen)                                            #sending
   if sen.decode() == 'quit':                               #quiting app on condition
      break
soc.close()                                                 #closing socket after use
print(f'{Fore.RED}Chat ended{Style.RESET_ALL}')