import os

from enum import Enum

import pygame

from gamesettings import GameSettings as gs


class Rooms(Enum):
    FIRST_ROOM = 0
    SECOND_ROOM = 1
    THIRD_ROOM = 2
    FOURTH_ROOM = 3


class Room(pygame.sprite.Sprite):

    def __init__(self, north, south, east, west):
        super().__init__()
        self.north = north
        self.south = south
        self.east = east
        self.west = west


class OpeningRoom(Room):

    def __init__(self):
        super().__init__(Rooms.FIRST_ROOM, Rooms.SECOND_ROOM,
                         Rooms.THIRD_ROOM, Rooms.FOURTH_ROOM)
        self.image = os.path.join(gs.ASSETS, "environment/wood_tileset.png")
        self.image.set_clip(pygame.Rect(0, 0, 85, 95))
        self.image = self.image.subsurface(self.image.get_clip())
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
