import pygame

'''
    Конфигурационные переменные для игры.
    Хранит в себе параметры игры, нейронки,
    функций, текстур и так далее
'''
# Функция выгрузки изображений текстур(?) фото для объектов
def LoadCarTexture(filename: str, size: tuple, angle: int):
        image = pygame.image.load(filename)
        image = pygame.transform.scale(image, size)
        image = pygame.transform.rotate(image, angle)
        return image


SCREEN_SIZE = (500, 800)
SCREEN_TITLE = 'AI Traffic racer'
FONT_SIZE = 20
FPS = 60

# Тайминги спавна
ROAD_TIMING = pygame.USEREVENT
TRAFFIC_TIMING = pygame.USEREVENT + 1
CAPTURE_TIMING = pygame.USEREVENT + 2

# Текстура игрока
AI_TEXTURE = LoadCarTexture('src/images/player_car.png', (90, 65), -90)

# Текстура дороги
ROAD_TEXTURE = pygame.image.load('src/images/road.png')
ROAD_TEXTURE = pygame.transform.scale(ROAD_TEXTURE, (500, 800))

# Диапазон скоростей трафика
TRAFFIC_SPEED = 3

# Текстуры трафика 
TRAFFIC_TEXTURES = [
    LoadCarTexture('src/images/orange_car.png', (90, 65), -90),
    LoadCarTexture('src/images/aqua_car.png', (90, 65), -90),
    LoadCarTexture('src/images/yellow_car.png', (90, 65), 90),
]
