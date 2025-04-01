import socket
import threading
from datetime import datetime

class Server:
    def __init__(self, recv_addr="0.0.0.0",recv_port = 7501, bcast_addr="255.255.255.255", bcast_port=7500,game_obj=None,scrollframe_obj=None):
        self.recv_addr = recv_addr
        self.recv_port = recv_port
        self.bcast_addr = bcast_addr
        self.bcast_port = bcast_port
        self.game_obj = game_obj
        self.scrollframe_obj = scrollframe_obj
        self.running = True

        # Initialize listening socket
        self.recv_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.recv_socket.bind((self.recv_addr, self.recv_port))

        # Initialize broadcast socket
        self.bcast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.bcast_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    def listen(self):

        print("Server started. Listening for incoming messages.") 
        print('Listening at', self.recv_addr,':',self.recv_port)
        print('braodcasting from port',str(self.bcast_port))

        while self.running:
            try:
                data, client_address = self.recv_socket.recvfrom(32)
                if data:
                    data = data.decode('utf-8').strip('\n')

                    if ":" in data and self.running:
                        shooter_id, target_id = data.split(':')
                        
                        try:
                            results = self.game_obj.get_player_by_hardware_id(shooter_id)
                            results.update_score(points = 10)
                            shooter_name = results.player_name
                            shooter_team = results.team_name
                            shooter_score = results.score
                            shooter_id = results.player_id

                            results = self.game_obj.get_player_by_hardware_id(target_id)
                            target_name = results.player_name
                            target_team = results.team_name
                            target_score = results.score
                            target_id = results.player_id



                            


                        except IndexError as e:
                            pass
                        
                        self.scrollframe_obj.add_text(f'[/] {datetime.now().time()} : {shooter_name} has hit {target_name} | Shutting down {target_name} for 10 seconds')



                        self.broadcast_code(target_id)  #Shutdown the player whos hit
                    else:
                        if data == "53":
                            print("Red base has been scored")
                            print(" +100 points to the Green team")
                            self.scrollframe_obj.add_text("[+] Red base has been scored +100 points to the Green team")

                        if data == "43":
                            print("Green base has been scored")
                            print(" +100 points to the Red team\n")
                            self.scrollframe_obj.add_text("[+] Green base has been scored. +100 points to the Red team")

            except socket.error as e:
                if self.running:
                    print(f"Socket error: {e}")

    def broadcast_code(self, code):
        try:
            self.bcast_socket.sendto(code.encode("utf-8"), (self.bcast_addr, self.bcast_port))
        except socket.error as e:
            print(f"Broadcast error: {e}")

    def start(self):
        self.listener_thread = threading.Thread(target=self.listen, daemon=True)
        self.listener_thread.start()

    def stop(self):
        self.running = False
        self.recv_socket.close()
        self.bcast_socket.close()
        print("Server shut down.")