import zmq
import random
import sys
import time
from multiprocessing import Process

port = sys.argv[1] 

context = zmq.Context()
socket = context.socket(zmq.PAIR)
#socket.connect("tcp://leafscript.net:%s" % port)
socket.connect("tcp://localhost:%s" % port)

def send(ins):
    socket.send(ins)


def recieve():
    print "aasd"
    r_context = zmq.Context()
    r_socket = r_context.socket(zmq.PAIR)
    r_socket.connect("tcp://localhost:%s" % port)
    while True: 
        print "fittja"
        msg=r_socket.recv()
        print "fittja"
        print msg

recieve_p = Process(target=recieve, args=())
recieve_p.start()

while True:
    msg=raw_input("Send a message please.")
    #send_p = Process(target=send, args=(msg,))
    #send_p.start()
    print msg
    send(msg)


