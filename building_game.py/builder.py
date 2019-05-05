import os
import sys
import sys
import pygame
pygame.init()
pygame.display.init()
#screen = pygame.display.set_mode((1000, 900))
screen = pygame.display.set_mode((1000, 700))
eraser = pygame.image.load('blocks/eraser.jpg')
start_pad = pygame.image.load('blocks/start_pad.png')
pygame.display.set_caption('BUILDER')
grass = pygame.image.load('blocks/grass_dirt.jpeg')
sand = pygame.image.load('blocks/realistic_sand.jpeg')
dirt = pygame.image.load('blocks/dirt.jpeg')
dirt = pygame.transform.scale(dirt, (50, 50))
sand = pygame.transform.scale(sand, (50, 50))
grass = pygame.transform.scale(grass, (50, 50))
start_pad = pygame.transform.scale(start_pad, (50, 50))
eraser = pygame.transform.scale(eraser, (50, 50))
monster = pygame.image.load('sprite_walking_img/L11E.png')
monster = pygame.transform.scale(monster, (50, 50))
end_pad = pygame.image.load('blocks/end_pad.png')
end_pad = pygame.transform.scale(end_pad, (50, 50))
blocks = []
save_blocks = []
building = False
clock = pygame.time.Clock()
start_pad_placed = False
end_pad_placed = False
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  screen.fill((0, 255, 0))
  for i in range(len(blocks)):
    #if blocks[i][2] > 200:
    screen.blit(blocks[i][0], (blocks[i][1], blocks[i][2]))
  #pygame.draw.line(screen, (0, 0, 255), [0, 198], [1000, 198], 3)
  #screen.blit(grass, (20, 20))
  #screen.blit(sand, (20 + 150 + 20, 20))
  #screen.blit(dirt, ((1000 - 20) - 150, 20))
  key = pygame.key.get_pressed()
  if key[pygame.K_1]:
    block = grass
    building = True
    build_x = 0
    build_y = 0
  if key[pygame.K_2]:
    block = sand
    building = True
    build_x = 0
    build_y = 0
  if key[pygame.K_3]:
    block = dirt
    building = True
    build_x = 0
    build_y = 0
  if key[pygame.K_4] and start_pad_placed == False:
    block = start_pad
    building = True
    build_x = 0
    build_y = 0
  if key[pygame.K_5]:
    block = eraser
    building = True
    build_x = 0
    build_y = 0
  if key[pygame.K_6]:
    block = monster
    building = True
    build_x = 0
    build_y = 0
  if key[pygame.K_7] and end_pad_placed == False:
    block = end_pad
    building = True
    build_x = 0
    build_y = 0
  if building:
    if key[pygame.K_DOWN] and build_y < 700 - 50:
      build_y += 50
    if key[pygame.K_UP] and build_y > 0:
      build_y -= 50
    if key[pygame.K_LEFT] and build_x >= 0:
      build_x -= 50
    if key[pygame.K_RIGHT] and build_x <= 1000 - 50:
      build_x += 50
    screen.blit(block, (build_x, build_y))
    if key[pygame.K_RETURN]:
      if block == start_pad:
        start_pad_placed = True
      if block == end_pad:
        end_pad_placed = True
      if block != eraser:
        for i in range(len(blocks)):
          if blocks[i][1] == build_x and blocks[i][2] == build_y:
            del blocks[i]
            break
        pygame.draw.rect(screen, (0, 0, 255), (0, 0, 50, 50))
        blocks.append([block, build_x, build_y])
      #elif blocks == end_pad:
      #  end_pad_placed = True
      else:
        for i in range(len(blocks)):
          if blocks[i][1] == build_x and blocks[i][2] == build_y:
            del blocks[i]
            break
        start_pad_placed = False
        for i in range(len(blocks)):
          if blocks[i][0] == start_pad:
            start_pad_placed = True
          #blocks.pop(i)
          #blocks.pop(i)
      building = False
      #screen.fill((0, 255, 0))
      #pygame.draw.line(screen, (0, 0, 255), [0, 198], [1000, 198], 3)
      #screen.blit(grass, (20, 20))
      #screen.blit(sand, (20 + 50 + 20, 20))
      #screen.blit(dirt, ((1000 - 20) - 50, 20))    
      #screen.blit(grass, (build_x, build_y))
      #pygame.display.update()
      #keys = pygame.key.get_pressed()
      #if keys[pygame.K_d]:
      #  building = False
  pygame.display.update()
  if key[pygame.K_s]:
    if key[pygame.K_RSHIFT] or key[pygame.K_LSHIFT]:
      for i in range(len(blocks)):
        if blocks[i][0] == grass:
          save_blocks.append(['grass', blocks[i][1], blocks[i][2]])
        elif blocks[i][0] == sand:
          save_blocks.append(['sand', blocks[i][1], blocks[i][2]])
        elif blocks[i][0] == dirt:
          save_blocks.append(['dirt', blocks[i][1], blocks[i][2]])
        elif blocks[i][0] == start_pad:
          save_blocks.append(['start', blocks[i][1], blocks[i][2]])
        elif blocks[i][0] == monster:
          save_blocks.append(['monster', blocks[i][1], blocks[i][2]])
        elif blocks[i][0] == end_pad:
          save_blocks.append(['end_pad', blocks[i][1], blocks[i][2]])
      pygame.display.quit()
      file_name = input('what file name would you like this saved to? ')
      os.chdir('saves')
      f = open(file_name + '.py', 'w')
      f.write('blocks = {}'.format(save_blocks))
      f.close()
      sys.exit()
  clock.tick(10)
