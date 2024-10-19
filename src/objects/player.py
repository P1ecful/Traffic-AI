import pygame
import pygame.sprite, pygame.key

from src.objects.ai import *

'''
    Написать по новой объект персонажа дял ИИ, рейкаст, 
    оформить формат данных на вход нейронке
'''
class Raycast(pygame.sprite.Sprite):
    def __init__(self, player_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((1000, 10))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (player_pos[0], player_pos[1] - 500)

    def Check_Collide(self, traffic, screen):
        font = pygame.freetype.Font(None, 20)
        
        for car in traffic:
            if self.rect.colliderect(car.rect):
                self.image.fill((255, 0, 0))
                car.text = font.render_to(screen, (car.rect[0], car.rect[1]), f'х = {car.rect[0]}', (255, 255, 255), (0, 0, 0))
                
                return car.rect[0]

class Player:
    def __init__(self, position, image, traffic):
        self.image = image
        self.traffic = traffic
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.fps = 60
        self.score = 0

    def raycast(self, screen):
        raycast_group = pygame.sprite.Group()
        raycast = Raycast(self.rect.center)
        raycast.Check_Collide(self.traffic, screen)

        raycast_group.add(raycast)
        raycast_group.draw(screen)

        # network = OurNeuralNetwork()

        # if raycast.Check_Collide(self.traffic, screen):
        #     x = np.array([self.rect[0], raycast.Check_Collide(self.traffic, screen)])
        #     print(network.feedforward(x))
        #     if network.feedforward(x) > 0.8807970779778823: self.rect.x -= 4
        #     elif network.feedforward(x) < 0.8807970779778823: self.rect.x += 4
        #     self.border()

    def border(self):
        if self.rect.right > 500:
            self.rect.right = 500
        if self.rect.left < 0:
            self.rect.left = 0


    def move(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_a]: self.rect.x -= 4
        elif key[pygame.K_d]: self.rect.x += 4  
        
        self.border()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def crash(self, traffic_cars):
        for car in traffic_cars:
            if car.rect.colliderect(self.rect):
                self.rect.center = (300, 600)
                self.score = 0
                traffic_cars.empty()

    

        