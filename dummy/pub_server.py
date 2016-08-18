# Imports
import zmq
import random
import sys
import time

# Default port
port="5556"

# Get specified port if user wishes
if len(sys.argv)>1:
    port=sys.argv[1]
    int(port)

# Create context and socket
context=zmq.Context()
socket=context.socket(zmq.PUB)
socket.bind("tcp://*:%s" % port)

# Send messages wether clients are connected or not.
while True:
    topic=random.randrange(9999,10005)
    messagedata=random.randrange(1,215)-80
    print "%d %d" % (topic,messagedata)
    socket.send("%d %d" % (topic,messagedata))
    string=socket.recv()
    print(string)
    time.sleep(1)
