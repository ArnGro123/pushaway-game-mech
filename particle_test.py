import pygame, sys, math, random as rand

pygame.init()

display = pygame.display.set_mode((500,500))
pygame.display.set_caption("Particle Test")
clock = pygame.time.Clock()

particles = []
particle_colors = ["grey","white"]

def draw_particles(x,y):
   
    for i in range(10):
        particles.append([rand.choice(particle_colors),rand.randrange(x-10,x+10),rand.randrange(y-10,y+10),rand.randrange(1,10)])
    
    for i in particles:
        pygame.draw.circle(display,i[0],(i[1],i[2]),i[3])
        x_list = [0.2,-0.2]
        i[1] += rand.choice(x_list)
        i[2] -= 0.1
        i[3] -= 0.01
        if i[3] <= 0:
            particles.remove(i)
    

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            draw_particles(mouse[0],mouse[1])
            while len(particles) > 0:
                draw_particles(mouse[0], mouse[1])

    
    
   

    pygame.display.update()