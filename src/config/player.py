import pygame.key
import pygame

from src.config.raycast import Raycast
from src.config.ai import *

class Player:
    def __init__(self, position, image, traffic):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.game_status = 'game'
        self.fps = 60
        self.score = 0
        self.traffic = traffic

    def raycast(self, screen):
        raycast_group = pygame.sprite.Group()
        raycast = Raycast(self.rect.center)
        raycast.Check_Collide(self.traffic, screen)

        raycast_group.add(raycast)
        raycast_group.draw(screen)

        network = OurNeuralNetwork()

        if raycast.Check_Collide(self.traffic, screen):
            x = np.array([self.rect[0], raycast.Check_Collide(self.traffic, screen)])
            print(network.feedforward(x))
            if network.feedforward(x) > 0.8807970779778823: self.rect.x -= 4
            elif network.feedforward(x) < 0.8807970779778823: self.rect.x += 4
            self.border()

    def border(self):
        if self.rect.right > 500:
            self.rect.right = 500
        if self.rect.left < 0:
            self.rect.left = 0


    def move(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_a]:
            self.rect.x -= 4
        elif key[pygame.K_d]:
            self.rect.x += 4
            
        self.border()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def crash(self, traffic_cars):
        for car in traffic_cars:
            if car.rect.colliderect(self.rect):
                self.game_status = 'game_over'
                traffic_cars.empty()

    

        