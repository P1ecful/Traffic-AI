import pygame.sprite

class Raycast(pygame.sprite.Sprite):
    def __init__(self, player_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((1, 400))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = player_pos