import pygame, sys

pygame.init()

display = pygame.display.set_mode((500,500))
pygame.display.set_caption("Pushaway Game Mechanic Testing")
clock = pygame.time.Clock()

background_color = (255,255,255) #white
shape_coords = [250,250]
acceleration = 0.1
velocity = 0
force = 0

def gravity(x,y,height):
    global velocity,acceleration
    y += velocity
    velocity += acceleration
    return x,y

def push_mech(mouse,shape):
    print(mouse)
    print(shape)
    distance = ((mouse[1]-shape[1])**2 + (mouse[0]-shape[0])**2)**0.5
    
    if mouse[1] > shape[1]:
        direction = 1
    else:
        direction = -1

    return(distance*direction)
    


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_coord = pygame.mouse.get_pos()
            force = push_mech(mouse_coord,shape_coords)

    display.fill(background_color)

    pygame.draw.circle(display,"blue",(shape_coords[0],shape_coords[1]),15)

    if shape_coords[1] + 20 >= 500:
        pass
    else:
        shape_coords = gravity(shape_coords[0],shape_coords[1],500)
        print(shape_coords)
    
    if force != 0:
        velocity += force/100
        force -= velocity 

    pygame.display.update()
    clock.tick(30)