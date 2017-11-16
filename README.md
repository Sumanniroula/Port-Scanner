# Port-Scanner
A port is a place where information goes into and out of a computer. A port scanner is a software application designed to probe a server or host for open ports. This is often used by administrators to verify security policies of their networks and by attackers to identify running services on a host with the view to compromise it.

TCP Scanning

The simplest port scanners use the operating system's network functions and are generally the next option to go to when SYN is not a feasible option

SYN Scanning

SYN scan is another form of TCP scanning. Rather than use the operating system's network functions, the port scanner generates raw IP packets itself, and monitors for responses. 

UDP Scanning

UDP scanning is also possible, although there are technical challenges. UDP is a connectionless protocol so there is no equivalent to a TCP SYN packet. However, if a UDP packet is sent to a port that is not open, the system will respond with an ICMP port unreachable message.

Some Socket Functions:

Before we get started with our sample program, let's see some of the socket
functions we are going to use.

sock = socket.socket (socket_family, socket_type)
Syntax for creating a socket

sock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
Creates a stream socket

AF_INET
Socket Family (here Address Family version 4 or IPv4)

SOCK_STREAM
Socket type TCP connections

SOCK_DGRAM
Socket type UDP connections

gethostbyname("host")
Translate a host name to IPv4 address format

socket.gethostbyname_ex("host")
Translate a host name to IPv4 address format, extended interface

socket.getfqdn("8.8.8.8")
Get the fqdn (fully qualified domain name)

socket.gethostname()
Returns the hostname of the machine..

socket.error
Exception handling
