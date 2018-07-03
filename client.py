#!/usr/bin/python2
import socket,sys

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

ip = "192.168.43.13"

port = 8888

try:
	while True:
		#adrr = s.accept()
		#print "connection established", adrr 
		message = raw_input("ClientS: ")
		s.sendto(message,(ip,port))
		t = s.recvfrom(1000)
		print "server message: " +t[0]
		
		user=raw_input("Do you want to quit: Y/N")
		if user == 'Y':
			s.sendto("Client has quit : please exit",(ip,port))
			exit()

except:
	print "Timeout"		


