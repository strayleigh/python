#!/usr/bin/python

import socket

t_ip = input("Enter the IP: ")
t_port = input("Enter the port: ")

port = int(t_port)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if s.connect((t_ip, port)):
        print("Port", port, "Close" )
else:
	print("Port", port, "Open")
