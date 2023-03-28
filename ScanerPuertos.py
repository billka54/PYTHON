import pyfiglet 
import sys
import socket
from datetime import datetime

print("-" * 75)
title = pyfiglet.figlet_format("PORT SCANNER", font="slant")
print (title)
print("-" * 75)

#User must introduce an argument, the target IP
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
    
else:
    print ("Invalid Argument")

#Some information of the target
print("-" * 50)
print("Scanning victim: " + target)
print("The scan started at: " + str(datetime.now()))
print("*" * 50)

try:
    for port in range (1,1000):
        s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = s.connect_ex((target, port))
        if result == 0:
            print("Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\n Quiting Program!!!!")
    sys.exit()
except socket.gaierror:
    print("\n Can't resolve Hostname!!")
    sys.exit()
except socket.error:
    print("\n Couldn't find server!!")
    sys.exit
