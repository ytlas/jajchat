import sys
import zmq

port="5556"
hostname="localhost"

if len(sys.argv)>1:
    port=sys.argv[1]
    int(port)

if len(sys.argv)>2:
    hostname=sys.argv[2]

context=zmq.Context()
socket=context.socket(zmq.SUB)

print "collecting updates from weather server..."
socket.connect("tcp://%s:%s" % (hostname,port))

if len(sys.argv)>2:
    socket.connect("tcp://%s:%s" % (hostname,port))

topicfilter="10001"
socket.setsockopt(zmq.SUBSCRIBE,topicfilter)

total_value=0
while True:
    string=socket.recv()
    topic,messagedata=string.split()
    total_value+=int(messagedata)
    print topic,messagedata

print "Average messagedata value for topic '%s' was %dF" % (topicfilter,total_value / update_nbr)
