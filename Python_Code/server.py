import socket
import threading
from datetime import datetime

class Server:
    def __init__(self, recv_addr="0.0.0.0",recv_port = 7501, bcast_addr="255.255.255.255", bcast_port=7500,controller=None):
        self.recv_addr = recv_addr
        self.recv_port = recv_port
        self.bcast_addr = bcast_addr
        self.bcast_port = bcast_port
        self.running = True
        self.controller = controller

        # Initialize listening socket
        self.recv_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.recv_socket.bind((self.recv_addr, self.recv_port))

        # Initialize broadcast socket
        self.bcast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.bcast_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    def update_scores(self):
        this_game = self.controller.this_game

        green_live_tree = self.controller.frames['pregame_screen'].green_live_tree
        
        for item in green_live_tree.get_children():
            row_data = green_live_tree.item(item)["values"]
            player = this_game.get_player_by_hardware_id(str(row_data[1]))
            new_score = player.score
            green_live_tree.item(item, values=(green_live_tree.item(item)['values'][0], 
                                            green_live_tree.item(item)['values'][1], 
                                            new_score))

        red_live_tree = self.controller.frames['pregame_screen'].red_live_tree

        for item in red_live_tree.get_children():
            row_data = red_live_tree.item(item)["values"]
            player = this_game.get_player_by_hardware_id(str(row_data[1]))
            new_score = player.score
            red_live_tree.item(item, values=(red_live_tree.item(item)['values'][0], 
                                            red_live_tree.item(item)['values'][1], 
                                            new_score))

        green_total = self.controller.this_game.total_team_score('G')
        self.controller.frames['pregame_screen'].label_green_total.config(text = f"Total Score:{green_total}")

        red_total = self.controller.this_game.total_team_score('R')
        self.controller.frames['pregame_screen'].label_red_total.config(text = f"Total Score:{red_total}")

        if green_total > red_total:
            self.controller.frames['pregame_screen'].label_green_total.config(fg = 'yellow')
            self.controller.frames['pregame_screen'].label_red_total.config(fg = 'white')
        elif green_total == red_total:
            self.controller.frames['pregame_screen'].label_green_total.config(fg = 'white')
            self.controller.frames['pregame_screen'].label_red_total.config(fg = 'white')
        else:
            self.controller.frames['pregame_screen'].label_red_total.config(fg = 'yellow')
            self.controller.frames['pregame_screen'].label_green_total.config(fg = 'white')


    def listen(self):

        print("Server started. Listening for incoming messages.") 
        print('Listening at', self.recv_addr,':',self.recv_port)
        print('braodcasting from port',str(self.bcast_port))

        while self.running:
            try:
                data, client_address = self.recv_socket.recvfrom(32)
                if data:
                    data = data.decode('utf-8').strip('\n')
                    shooter_id, target_id = data.split(':')

                    shooter = self.controller.this_game.get_player_by_hardware_id(shooter_id)
                    target = self.controller.this_game.get_player_by_hardware_id(target_id)
                    

                    if target_id != "53" and target_id != "43":
                        self.broadcast_code(target_id)  #Shutdown the player whos hit
                        self.controller.frames['pregame_screen'].live_events.add_text(f'[-] {shooter.player_name} hit {target.player_name} | Shutting {target.player_name} down for 10 seconds')
                        shooter.update_score(10)

                    else:
                        if target_id == "53":
                            print("Red base has been scored")
                            print(" +100 points to the Green team")
                            self.controller.frames['pregame_screen'].live_events.add_text("[+] Red base has been scored +100 points to the Green team")
                            shooter.update_score(100)
                            self.broadcast_code(target_id)

                        if target_id == "43":
                            print("Green base has been scored")
                            print(" +100 points to the Red team\n")
                            self.controller.frames['pregame_screen'].live_events.add_text("[+] Green base has been scored. +100 points to the Red team")
                            shooter.update_score(100)
                            self.broadcast_code(target_id)

                self.update_scores()




            except socket.error as e:
                if self.running:
                    print(f"Socket error: {e}")

    def broadcast_code(self, code):
        try:
            self.bcast_socket.sendto(code.encode("utf-8"), (self.bcast_addr, self.bcast_port))
            print("Broadcasted Code: ",code)
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
