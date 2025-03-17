from typing import Callable
import socket
import time

# Defining constants for transmitting and receiving codes
START_GAME_CODE: int = 202
END_GAME_CODE: int = 221
RED_BASE_SCORED_CODE: int = 53
GREEN_BASE_SCORED_CODE: int = 43
BUFFER_SIZE: int = 1024
GAME_TIME_SECONDS: int = 360  # Seconds
BROADCAST_ADDRESS: str = "127.0.0.1"
RECEIVE_ALL_ADDRESS: str = "0.0.0.0"
TRANSMIT_PORT: int = 7500
RECEIVE_PORT: int = 7501


class Network:
    def __init__(self) -> None:
        self.transmit_socket: socket.socket = None
        self.receive_socket: socket.socket = None

    def set_sockets(self) -> bool:
        # Set up transmit and receive sockets
        try:
            self.transmit_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.receive_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.receive_socket.bind((RECEIVE_ALL_ADDRESS, RECEIVE_PORT))
            return True
        except Exception as e:
            print(f"Error setting up sockets: {e}")
            return False

    def close_sockets(self) -> bool:
        # Close transmit and receive sockets
        try:
            if self.transmit_socket:
                self.transmit_socket.close()
            if self.receive_socket:
                self.receive_socket.close()
            return True
        except Exception as e:
            print(f"Error closing sockets: {e}")
            return False

    def transmit_equipment_code(self, equipment_code: str) -> bool:
        # Transmit provided equipment code to the broadcast address
        try:
            self.transmit_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            self.transmit_socket.sendto(str(equipment_code).encode(), (BROADCAST_ADDRESS, TRANSMIT_PORT))
            return True
        except Exception as e:
            print(f"Error transmitting equipment code: {e}")
            return False


