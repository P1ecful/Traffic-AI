import random
import pygame
import pygame.freetype

from src.config.player import Player
from src.config.road import Road
from src.config.traffic import TrafficCar

def Game():
    pygame.init()
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((500, 800))
    pygame.display.set_caption('AI Traffic racer')
    background_color = (0, 0, 0)
    font = pygame.freetype.Font(None, 20)

    road_group = pygame.sprite.Group()
    spawn_road_time = pygame.USEREVENT
    pygame.time.set_timer(pygame.USEREVENT, 1000)

    traffic_cars_group = pygame.sprite.Group()
    spawn_traffic_time = pygame.USEREVENT + 1
    pygame.time.set_timer(spawn_traffic_time, 2000)

    def get_car_image(filename, size, angle):
        image = pygame.image.load(filename)
        image = pygame.transform.scale(image, size)
        image = pygame.transform.rotate(image, angle)
        return image


    player_image = get_car_image('src/images/player_car.png', (90, 65), -90)
    road_image = pygame.image.load('src/images/road.png')
    road_image = pygame.transform.scale(road_image, (500, 800))

    traffic_car_images = []
    orange_car = get_car_image('src/images/orange_car.png', (90, 65), -90)
    aqua_car = get_car_image('src/images/aqua_car.png', (90, 65), -90)
    yellow_car = get_car_image('src/images/yellow_car.png', (90, 65), 90)
    traffic_car_images.extend((orange_car, aqua_car, yellow_car))

    road = Road(road_image, (250, 400))
    road_group.add(road)
    road = Road(road_image, (250, 0))
    road_group.add(road)

    def spawn_road():
        road_bg = Road(road_image, (250, -600))
        road_group.add(road_bg)

    def spawn_traffic():
        position = (random.randint(40, 460), random.randint(-60, -40))
        speed = random.randint(3, 3)
        traffic_car = TrafficCar(random.choice(traffic_car_images), position, speed, player)
        traffic_cars_group.add(traffic_car)

    def draw_all():
        road_group.update()
        road_group.draw(screen)

        traffic_cars_group.update()
        traffic_cars_group.draw(screen)
        
        player.draw(screen)
        player.raycast(screen)

    player = Player((300, 600), player_image, traffic_cars_group)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == spawn_road_time:
                spawn_road()
            if event.type == spawn_traffic_time:
                spawn_traffic()

        screen.fill(background_color)
        if player.game_status == 'game':
            player.move()
            draw_all()
            player.crash(traffic_cars_group)
        elif player.game_status == 'game_over':
            player.score = 0
            player.position = (300, 600)
            player.game_status = 'game'


        font.render_to(screen, (20, 20), f'Score: {player.score}', (255, 255, 255), (0, 0, 0))
        pygame.display.flip()
        clock.tick(player.fps)

