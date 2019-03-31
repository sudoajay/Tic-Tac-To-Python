import pygame


class Run:
    @staticmethod
    def SecondScreenGUI(pygame, screen):
        # get the size of the fullscreen display
        getX = screen.get_width()
        getY = screen.get_height()
        done = False

        # this is my text
        myfont = pygame.font.SysFont("serif", 40)
        # render text
        label = myfont.render("Welcome To My Game", 1, pygame.Color("RED"))
        screen.blit(label, (getX / 2 - 150, getY / 2 - 200))

        # this is second text (Tic Tac Toe)
        myfont = pygame.font.SysFont("serif", 30)
        # render text
        label = myfont.render("Tic-Tac-Toe", 1, pygame.Color("RED"))
        screen.blit(label, (getX / 2 - 50, getY / 2 - 100))

        # this is second text (Tic Tac Toe)
        myfont = pygame.font.SysFont("serif", 30)
        # render text
        label = myfont.render("Press the Space to start the game", 1, pygame.Color("Green"))
        screen.blit(label, (getX / 2 - 150, getY / 2))
