import pygame
from LetsBegin import FirstScreen
from LetsBegin import SecondScreen


#  Main Method
def Main():
    pygame.font.init()
    screen = pygame.display.set_mode((1300, 600))
    done = False
    # get the size of the fullscreen display
    FirstScreen.Run.FirstScreenGUI(pygame, screen)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    print(event.unicode)
                elif event.key == pygame.K_BACKSPACE:
                    print(event.unicode)
                elif event.key == pygame.K_SPACE:
                    screen.fill((0, 0, 0))
                    pygame.display.flip()
                    SecondScreen.Run.SecondScreenGUI(pygame, screen)
                    screen.fill((0, 0, 0))
                    pygame.display.flip()
                if event.key == pygame.K_ESCAPE:
                    done = True
        pygame.display.flip()
Main()
