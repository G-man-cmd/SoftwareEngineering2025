import sys
import socket
import threading
import time
import sys

data = None




#init listening socket
recv_addr = "0.0.0.0"
recv_port = 7501
changed_recv_port = int(input("Set Receiving port\nEnter 0 for default port\n(Default is 7501): "))
if changed_recv_port and (changed_recv_port > 1024 and changed_recv_port < 65000):
    recv_port = changed_recv_port
    print('Using new port of ',recv_port,"\n")
else:
    print('Using default port of ',recv_port,"\n")
    
recv_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
recv_socket.bind((recv_addr,recv_port))

#init broadcast socket
bcast_addr = "255.255.255.255"
bcast_port = 7500

changed_bcast_port = int(input("Set Broadcast port\nEnter 0 for default port\n(Default is 7500): "))
if changed_bcast_port and (changed_recv_port > 1024 and changed_recv_port < 65000 and changed_bcast_port != recv_port):
    bcast_port = changed_bcast_port
    print('Using new port of ',bcast_port,"\n")
else:
    print('Using default port of ',bcast_port,"\n")

bcast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bcast_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)


def listen():
    while True:
        global data
        data, client_address = recv_socket.recvfrom(32)
        if len(data) != 0:
            data = data.decode('utf-8')
            data = data.strip('\n')

            if ":" in data:
                data = data.split(':')
                print('eq id {} has hit eqid {}\n'.format(data[0],data[1]))
                print("shutting down eqid {} for 10 seconds\n".format(data[1]))
                broadcast_code(data[1]) #shutdown player who has been hit
            else:
                if data == "53":
                    print("Red base has been scored")
                    print(" +100 points to the green team\n")

                if data == "43":
                    print("Green base has been scored")
                    print(" +100 points to the red team\n")

            #print(data)
            data = None

def broadcast_code(code):
    if bcast_socket.sendto(code.encode("utf-8"), (bcast_addr, bcast_port)):
        return True
    else:
        return False


'''

to be used when the GUI is done
for a clean exit of thread and the main prog


def exit():
    #code to close the GUI
    bcast_socket.close()
    recv_socket.close()
    sys.exit()

'''

#start a seprate async thread for listening
t1=threading.Thread(target=listen)
t1.start()


while True: #represents the GUI for now
    time.sleep(1)
    print("*")
    print("returned val:",data)
