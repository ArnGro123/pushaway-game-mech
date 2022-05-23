from turtle import shape
import pygame, sys

pygame.init()

display = pygame.display.set_mode((500,500))
pygame.display.set_caption("Pushaway Game Mechanic Testing")
clock = pygame.time.Clock()

background_color = (255,255,255) #white
shape_coords = [250,250]
acceleration = 0.1
velocity = 0
force = 5
dr_x = 0
dr_y = 0

def gravity(x,y):
    global velocity,acceleration
    y += velocity
    velocity += acceleration
    return x,y

def direction_mech(mouse,shape):
    print(mouse)
    print(shape)

    dr_x = 0
    dr_y = 0

    if mouse[0] > shape[0]:
        dr_x = -1
    elif mouse[0] < shape[0]:
        dr_x = 1

    if mouse[1] > shape[1]:
        dr_y = -1
    elif mouse[1] < shape[1]:
        dr_y = 1
    
    return dr_x,dr_y
    


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_coord = pygame.mouse.get_pos()
            dr_x,dr_y = direction_mech(mouse_coord,shape_coords)
            force = 5
            velocity = 0 


    display.fill(background_color)

    pygame.draw.circle(display,"blue",(shape_coords[0],shape_coords[1]),15)

    if shape_coords[1] + 20 >= 500:
        pass
    else:
        shape_coords = gravity(shape_coords[0],shape_coords[1])
        shape_coords = list(shape_coords)


    if force >= 0:
        if shape_coords[0]-20 > 0 and shape_coords[0]+20 < 500:
            shape_coords[0] += force * dr_x
        shape_coords[1] += force * dr_y
        force -= 0.1
    
    print(force)

    pygame.display.update()
    clock.tick(30)