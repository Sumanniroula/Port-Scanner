#import modules
import socket
import subprocess
from datetime import datetime
import sys

subprocess.call('clear',shell=True) #clear

address_name = raw_input("Enter the website address you want to scan: ") #ask user input
IPaddress = socket.gethostbyname(address_name) #get IP address

print "Scanning the remote address name...", address_name,IPaddress

start_time = datetime.now() #initiate start time

try:
    for port in range(1,1025): #scan ports from 0 to 1024
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creates a stream socket
        result = sock.connect_ex((IPaddress, port))
        if result == 0: #outputs zero if success
            print "Port {}  is open".format(port) #print open ports
        sock.close()

except KeyboardInterrupt: #for keyboard input error
    print "User pressed CTRL+C"
    sys.exit()

except socket.gaierror: #for unresolved host name
    print "Host name couldn't be resolved"
    sys.exit()

except socket.error: #for any socket errors
    print "Couldn't connect to server"
    sys.exit()

end_time = datetime.now() #finished time

total_time = end_time - start_time #calculate total time needed to scan

print "Scan completed in: ", total_time