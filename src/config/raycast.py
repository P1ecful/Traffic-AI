import pygame.sprite

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