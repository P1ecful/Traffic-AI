import pygame.sprite

# Класс контроллера игрока-нейронки
class Player:
    def __init__(self, position, image, traffic):
        self.image = image
        self.traffic = traffic
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.score = 0

    def border(self):
        if self.rect.right > 500:
            self.rect.right = 500
        if self.rect.left < 0:
            self.rect.left = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def crash(self, traffic_cars):
        for car in traffic_cars:
            if car.rect.colliderect(self.rect):
                self.rect.center = (300, 600)
                self.score = 0
                traffic_cars.empty()

# Класс объекта трафика
class Traffic(pygame.sprite.Sprite):
    def __init__(self, image, position, speed, player):
        super().__init__()
        self.speed = speed
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.player = player

    def remove(self):
        if self.rect.top > 800:
            self.kill()
            self.player.score += 1

    def update(self):
        self.rect.y += self.speed
        self.remove()

# Класс объекта дороги
class Road(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = position

    def update(self):
        self.rect.y += 2

# Область захвата трафика
class TrafficCapture(pygame.sprite.Sprite):
    def __init__(self, player_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((1000, 10))
        self.image.set_alpha(0)
        self.rect = self.image.get_rect()
        self.rect.center = (player_pos[0], player_pos[1] - 500)

    def Check_Collide(self, traffic, screen) -> int:
        font = pygame.freetype.Font(None, 20)
        
        for car in traffic:
            if self.rect.colliderect(car.rect):
                car.text = font.render_to(screen, (car.rect[0], car.rect[1]-20), f'х = {car.rect[0]}', (255, 255, 255), (0, 0, 0))
                
                return car.rect[0]