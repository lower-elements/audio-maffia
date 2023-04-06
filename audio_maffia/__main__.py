import pygame
import os


def main():
    from . import options, audio
    from . import consts, menus
    from .version import version

    pygame.init()
    pygame.display.set_caption(
        f"{consts.TITLE}, version {version.major}.{version.minor}.{version.patch}"
    )
    screen = pygame.display.set_mode((900, 500))
    from .game import Game

    g = Game(screen)
    g.start()
    g.loop()


if __name__ == "__main__":
    main()
