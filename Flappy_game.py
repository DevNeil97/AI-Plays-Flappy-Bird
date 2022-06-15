# imports
import pygame
import neat 
import time
import os
import random

# window size
WIDTH = 600
HIGHT = 800

BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load((os.path.join("imgs", "bird1.png")))),
             pygame.transform.scale2x(pygame.image.load((os.path.join("imgs", "bird2.png")))),
             pygame.transform.scale2x(pygame.image.load((os.path.join("imgs", "bird3.png"))))]
PIPE_IMG = pygame.transform.scale2x(pygame.image.load((os.path.join("imgs", "pipe.png"))))
BASE_IMG = pygame.transform.scale2x(pygame.image.load((os.path.join("imgs", "base.png"))))
BG_IMG = pygame.transform.scale2x(pygame.image.load((os.path.join("imgs", "bg.png"))))

class bird:
    IMGS = BIRD_IMGS
    MAX_ROTATION = 25
    ROT_VAL = 20
    ANIMATION_TIME = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.val = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.IMGS[0]

