import zmq
import random
import sys
import time

port = sys.argv[1]
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://*:%s" % port)

while True:
    socket.send("Server message to client3")
    time.sleep(1)
    print "ss"
    #msg = socket.recv()
    #print msg
