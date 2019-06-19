import os
import socket
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("192.168.0.40", 5000))
while 1:
	data = client_socket.recv(512).decode()
	data = data.encode('ascii')
	if 'go' in data:
		op = 'rosrun knu_ros_lecture turtle_position_move 0 0.00001'
		os.system(op)
		print("Go")
	elif 'wait' in data:
		for _ in range(10):
			op = 'rosrun knu_ros_lecture turtle_position_move 0 0'
			os.system(op)
			time.sleep(0.01)
		print("STOP")
	elif 'come on' in data:
		op = 'roslaunch turtlebot3_bringup turtlebot3_remote.launch'
		os.system(op)
		print("Come on")
	else:
		print("RECEIVED:",data.encode('ascii'))
client_socket.close()
print ("socket colsed... END.")
