import random
import pygame

class RandomTrackPlayer:
    def __init__(self, track_list):
        if not track_list:
            raise ValueError("Track list cannot be empty")
        
        self.track_list = track_list
        pygame.mixer.init()

    def play_random_track(self):
        #Plays a random track from the given list
        track = random.choice(self.track_list)
        pygame.mixer.music.load("photon_tracks/"+track)
        pygame.mixer.music.play()
        print(f"Now playing: {track}")

    def stop_track(self): #stop
        pygame.mixer.music.stop()
        print("Playback stopped.")
