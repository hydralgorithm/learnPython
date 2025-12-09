import time
import pygame

def artist_reveal(name):
    if name == "coldplay" or name == "cold play":
        print("YOU ARE CORRECT !")
        pygame.mixer.init()
        pygame.mixer.music.load("G:/D DRIVE/Desktop/Python\/projects/audio/TheScientist.mp3")
        pygame.mixer.music.play(start = 40.0)
        time.sleep(20)
        pygame.mixer.music.stop()
            
    else:
        print("You were WRONG! Its coldplay!")
        pygame.mixer.init()
        pygame.mixer.music.load("G:/D DRIVE/Desktop/Python/projects/audio/Beeper_Call.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(1)



if __name__ == "__main__":
    name = input("AAAaaa fellow user, do you know the artist behind yellow song? (Type artist name): " ).lower()
    artist_reveal(name)