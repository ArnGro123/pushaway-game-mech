import pygame, sys, math, random as rand

pygame.init()

display = pygame.display.set_mode((500,500))
pygame.display.set_caption("Pushaway Game Mechanic Testing")
clock = pygame.time.Clock()

sprite = pygame.image.load("concept_art_sprite.png").convert_alpha()
sprite = pygame.transform.smoothscale(sprite,(60,100))

sprite_2 = pygame.image.load("concept_art_sprite_2.png").convert_alpha()
sprite_2 = pygame.transform.smoothscale(sprite_2,(80,20))

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

def angle_calc(coord1,coord2):
    angle = math.degrees(math.atan2(coord1,coord2)) 
    return angle

class Particle():
    def __init__(self,x,y,image,direction):
        self.x = x
        self.y = y
        self.circle = image
        self.direction = direction
    
    def spawn(self):
        display.blit(self.circle,(self.x,self.y))

    def particles_force(self):
        force = rand.randrange(1,5)
        self.x += force * self.direction
        self.y += force * self.direction


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
            for i in range(10):
                Particle.spawn(self)
                Particle.particles_force(self)


    display.fill(background_color)
    display.blit(sprite,(shape_coords[0],shape_coords[1]))
    
    rotated_sprite_2 = pygame.transform.rotate(sprite_2,angle_calc(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]))
    sprite_2_rect = rotated_sprite_2.get_rect()
    sprite_2_rect.center = (shape_coords[0],shape_coords[1]+40)

    display.blit(rotated_sprite_2,(shape_coords[0],shape_coords[1]+40))


    if shape_coords[1] + 100 >= 500:
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