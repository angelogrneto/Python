import pygame
pygame.init()
pygame.mixer.music.load('Twenty One Pilots - Stressed Out (dimasacd.mp3).mp3')
pygame.mixer.music.play()


while True: 
      
    print("Press 'p' to pause, 'r' to resume") 
    print("Press 'e' to exit the program") 
    query = input("  ") 
      
    if query == 'p': 
        pygame.mixer.music.pause()      
    elif query == 'r': 
        pygame.mixer.music.unpause() 
    elif query == 'e': 
        pygame.mixer.music.stop() 
        break