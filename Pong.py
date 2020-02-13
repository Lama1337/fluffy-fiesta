##Mitt forsøk på å kode pong##
##05.02.2020##

#requisites
#upgrade pip = py -m pip install --upgrade pip
#install pygame_module = py -m pip install -U pygame --user

#Import av pygamemodul
import pygame
pygame.init()

#Spillvindustuff
gameDisplay = pygame.display.set_mode((1024,768))   #Lager spillvindu = Surfacce, du kan kun ha 1 av denne typen)
pygame.display.set_caption("Pong")
## Få dette til å virke surface = pygame.image.load("Abomb.png").convert() 


#Definering av klokke for og sette fps basically
clock = pygame.time.Clock()

#Dead or Alive
dead = False


while not dead:                                     #Logicloop1 fanger alle events med pygame event get. 
    
    for event in pygame.event.get():                # her sjhjer
        if event.type == pygame.QUIT:               # aså skjer sånn
            dead = True

        gameDisplay.fill(surface)
        

        print(event)

pygame.display.update()                         #Oppdatere vinduet med data
clock.tick(60)                                  #FPS                    

pygame.quit()                                   #Stopper Pygame
quit()                                          #Python quit




#Tegner spillere + ball (more surface code i assume)














#      Til senere utvikling
#-----------------------------------

#Playernames
#Player1 = input("Player1: ")
#Player2 = input("Player2: ")

#Definerer kontrollinput

#Player1.up = "arrow_up"
#Player1.down = #

#Player2.up = "w"
#Player2.down = "s"

