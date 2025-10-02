import pygame
import math
from datetime import datetime

pygame.init()
screen_size = (640, 480)
screen = pygame.display.set_mode(screen_size)
screen.fill((255, 255, 255))

start_position = (screen_size[0]/2, screen_size[1]/2)
radius = 210


while True:

    screen.fill((255, 255, 255))
    s = datetime.now().second
    m = datetime.now().minute
    h = datetime.now().hour
    s_angle = math.radians((360/60)*s -90)
    m_angle = math.radians((360/60)*m -90)
    h_angle = math.radians((360/12)*(h % 12. + m/60) -90)
    skive = radius
    y = m*2
    s_inner_radius = radius -y
    m_inner_radius = radius -y
    h_inner_radius = radius -y
    s_end_offset = [radius*math.cos(s_angle), radius*math.sin(s_angle)]
    m_end_offset = [radius*math.cos(m_angle), radius*math.sin(m_angle)]
    h_end_offset = [radius*math.cos(h_angle), radius*math.sin(h_angle)]



    s_end_position = (start_position[0]+s_end_offset[0], start_position[1]+s_end_offset[1])
    m_end_position = (start_position[0]+m_end_offset[0], start_position[1]+m_end_offset[1])
    h_end_position = (start_position[0]+h_end_offset[0], start_position[1]+h_end_offset[1])
    # pygame.draw.line(screen, (0,0,0), start_position, end_position, 5)
    pygame.draw.circle(screen, (0, 0, 0), start_position, skive, 1)
    pygame.draw.circle(screen, (0,0,0), (s_end_position[0], s_end_position[1]), 6, 2)
    pygame.draw.circle(screen, (0,0,0), (m_end_position[0], m_end_position[1]), 12, 2)
    pygame.draw.circle(screen, (0,0,0), (h_end_position[0], h_end_position[1]), 18, 2)

    for hour in range(12):
        angle = math.radians((360/12)*hour - 90)
        x_mark = start_position[0] + skive*math.cos(angle)
        y_mark = start_position[1] + skive*math.sin(angle)
        pygame.draw.circle(screen, (0,0,0), (x_mark, y_mark), 7, 2)

    for x in range(0, 360, 90):
        inner_offset = [s_inner_radius*math.cos(math.radians(x)), s_inner_radius*math.sin(math.radians(x))]
        pygame.draw.aaline(screen, (0,0,0), (start_position[0]+inner_offset[0], start_position[1]+inner_offset[1]), (s_end_position[0], s_end_position[1]), 20)

    for x in range(0, 360, 30):
        inner_offset = [m_inner_radius*math.cos(math.radians(x)), m_inner_radius*math.sin(math.radians(x))]
        pygame.draw.aaline(screen, (0,0,0), (start_position[0]+inner_offset[0], start_position[1]+inner_offset[1]), (m_end_position[0], m_end_position[1]), 10)

    for x in range(0, 360, 30):
        inner_offset = [h_inner_radius*math.cos(math.radians(x)), h_inner_radius*math.sin(math.radians(x))]
        pygame.draw.aaline(screen, (0,0,0), (start_position[0]+inner_offset[0], start_position[1]+inner_offset[1]), (h_end_position[0], h_end_position[1]), 10)

    pygame.display.flip()



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()