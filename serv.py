#!/usr/bin/python2
import socket,sys

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


ip="192.168.43.13"
port= 8888

s.bind((ip,port))

try:
	s.listen(5)
	print "listening: ......"

except:
	print "error in connecting"

try :
	
	while True :
	#yaha listen function error show kar raha hai
		#adrr = s.accept()
		#print "connection established", adrr 
		r = s.recvfrom(1000)
		print "receive from client : " + r[0]
		print r[1]
		reply = raw_input('server : ')
		client_address = r[1]
		s.sendto(reply, client_address)
except:
	print "timeout or no server running"	
