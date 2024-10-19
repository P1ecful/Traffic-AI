import random 
import pygame, pygame.freetype

# !FIXME изменить имена файлов
from src.config import *
from src.objects.player import Player
from src.objects.minor_objects import *

def main():
    # Группы объектов
    road_group = pygame.sprite.Group()
    traffic_group = pygame.sprite.Group()

    # Спавн стартовой дорог
    road_group.add(Road(ROAD_TEXTURE, (250, 400)))
    road_group.add(Road(ROAD_TEXTURE, (250, 0)))

    # Таймеры на спавн дороги и трафика
    pygame.time.set_timer(ROAD_TIMING, 1000)
    pygame.time.set_timer(TRAFFIC_TIMING, 2000)

    # Создаем объект нейронки
    AI = Player((300, 600), AI_TEXTURE, traffic_group)

    RUNNING = True
    while RUNNING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                RUNNING = False

            if event.type == ROAD_TIMING: # Спавн дороги
                road_group.add(Road(ROAD_TEXTURE, (250, -600)))

            if event.type == TRAFFIC_TIMING: # Cпавн трафика
                traffic_group.add(Traffic(
                    random.choice(TRAFFIC_TEXTURES), 
                    (random.randint(40, 460), random.randint(-60, -40)), # Координаты спавна трафика
                    TRAFFIC_SPEED, # Скорость трафика
                    AI
                ))

        # Отрисовка дороги
        road_group.update()
        road_group.draw(screen)

        # Отрисовка трафика
        traffic_group.update()
        traffic_group.draw(screen)
        
        # Отрисовка нейронки
        AI.draw(screen)
        AI.move()
        AI.crash(traffic_group)

        # Надпись Score
        font.render_to(screen, (20, 20), f'Score: {AI.score}', (255, 255, 255), (0, 0, 0))
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(SCREEN_TITLE)
    font = pygame.freetype.Font(None, FONT_SIZE)

    main()