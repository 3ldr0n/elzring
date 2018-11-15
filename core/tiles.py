import pygame

from gamesettings import GameSettings as gs


class Sand(pygame.sprite.Sprite):

    def __init__(self, group, x, y):
        self.group = group
        super().__init__(self.group)
        self.image = pygame.Surface((gs.TILESIZE, gs.TILESIZE)).convert_alpha()
        self.image.fill(gs.SAND_YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.x = x
        self.y = y
        self.rect.x = self.x * gs.TILESIZE
        self.rect.y = self.y * gs.TILESIZE


class Ocean(pygame.sprite.Sprite):

    def __init__(self, group, x, y):
        self.group = group
        super().__init__(self.group)
        self.image = pygame.Surface((gs.TILESIZE, gs.TILESIZE)).convert_alpha()
        self.image.fill(gs.OCEAN_BLUE)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = self.x * gs.TILESIZE
        self.rect.y = self.y * gs.TILESIZE


class Grass(pygame.sprite.Sprite):

    def __init__(self, group, x, y):
        self.group = group
        super().__init__(self.group)
        self.image = pygame.Surface((gs.TILESIZE, gs.TILESIZE))
        self.image.fill(gs.WHITE)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = self.x * gs.TILESIZE
        self.rect.y = self.y * gs.TILESIZE


class Wall(pygame.sprite.Sprite):

    def __init__(self, group, screen, x, y):
        self.group = group
        super().__init__(self.group)
        self.screen = screen
        self.image = pygame.Surface((gs.TILESIZE, gs.TILESIZE))
        self.image.fill(gs.WHITE)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = self.x * gs.TILESIZE
        self.rect.y = self.y * gs.TILESIZE
