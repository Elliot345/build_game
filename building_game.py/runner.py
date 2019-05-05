import pygame
import time
import sys
import os
end_pad = pygame.image.load('blocks/end_pad.png')
end_pad = pygame.transform.scale(end_pad, (50, 50))
monster_vel = 6
vel = 5
time_dead = 0
os.chdir('saves')
os.system('ls')
file = input('File: ')
f = open(file, 'r')
exec('{}'.format(f.read()))
f.close()
start_found = False
end_found = False
for i in range(len(blocks)):
  if blocks[i][0] == 'start':
    avitar_x = blocks[i][1]
    avitar_y = blocks[i][2]
    start_found = True
    del blocks[i]
    break
for i in range(len(blocks)):
  if blocks[i][0] == 'end_pad':
    end_x = blocks[i][1]
    end_y = blocks[i][2]
    end_found = True
    del blocks[i]
    break
for i in range(len(blocks)):
  if blocks[i][0] == 'monster':
    monster_x = blocks[i][1]
    monster_y = blocks[i][2]
    monster_found = True
    del blocks[i]
    break
if start_found == False:
  print('No start pad')
  sys.exit()
if end_found == False:
  print('No end pad')
  sys.exit()
if monster_found == False:
  print('No monster start pad')
  sys.exit()
os.chdir('..')
fire_left = pygame.image.load('sprite_walking_img/fire_left.png')
fire_right = pygame.image.load('sprite_walking_img/fire_right.png')
fire_right = pygame.transform.scale(fire_right, (50, 50))
fire_left = pygame.transform.scale(fire_left, (50, 50))
L1E = pygame.image.load('sprite_walking_img/L1E.png')
L2E = pygame.image.load('sprite_walking_img/L2E.png')
L3E = pygame.image.load('sprite_walking_img/L3E.png')
L4E = pygame.image.load('sprite_walking_img/L4E.png')
L5E = pygame.image.load('sprite_walking_img/L5E.png')
L6E = pygame.image.load('sprite_walking_img/L6E.png')
L7E = pygame.image.load('sprite_walking_img/L7E.png')
L8E = pygame.image.load('sprite_walking_img/L8E.png')
L9E = pygame.image.load('sprite_walking_img/L9E.png')
L10E = pygame.image.load('sprite_walking_img/L10E.png')
L11E = pygame.image.load('sprite_walking_img/L11E.png')
R1E = pygame.image.load('sprite_walking_img/R1E.png')
R2E = pygame.image.load('sprite_walking_img/R2E.png')
R3E = pygame.image.load('sprite_walking_img/R3E.png')
R4E = pygame.image.load('sprite_walking_img/R4E.png')
R5E = pygame.image.load('sprite_walking_img/R5E.png')
R6E = pygame.image.load('sprite_walking_img/R6E.png')
R7E = pygame.image.load('sprite_walking_img/R7E.png')
R8E = pygame.image.load('sprite_walking_img/R8E.png')
R9E = pygame.image.load('sprite_walking_img/R9E.png')
R10E = pygame.image.load('sprite_walking_img/R10E.png')
R11E = pygame.image.load('sprite_walking_img/R11E.png')
R1E = pygame.transform.scale(R1E, (50, 50))
R2E = pygame.transform.scale(R2E, (50, 50))
R3E = pygame.transform.scale(R3E, (50, 50))
R4E = pygame.transform.scale(R4E, (50, 50))
R5E = pygame.transform.scale(R5E, (50, 50))
R6E = pygame.transform.scale(R6E, (50, 50))
R7E = pygame.transform.scale(R7E, (50, 50))
R8E = pygame.transform.scale(R8E, (50, 50))
R9E = pygame.transform.scale(R9E, (50, 50))
R10E = pygame.transform.scale(R10E, (50, 50))
R11E = pygame.transform.scale(R11E, (50, 50))
L1E = pygame.transform.scale(L1E, (50, 50))
L2E = pygame.transform.scale(L2E, (50, 50))
L3E = pygame.transform.scale(L3E, (50, 50))
L4E = pygame.transform.scale(L4E, (50, 50))
L5E = pygame.transform.scale(L5E, (50, 50))
L6E = pygame.transform.scale(L6E, (50, 50))
L7E = pygame.transform.scale(L7E, (50, 50))
L8E = pygame.transform.scale(L8E, (50, 50))
L9E = pygame.transform.scale(L9E, (50, 50))
L10E = pygame.transform.scale(L10E, (50, 50))
L11E = pygame.transform.scale(L11E, (50, 50))
L1 = pygame.image.load('sprite_walking_img/L1.png')
L2 = pygame.image.load('sprite_walking_img/L2.png')
L3 = pygame.image.load('sprite_walking_img/L3.png')
L4 = pygame.image.load('sprite_walking_img/L4.png')
L5 = pygame.image.load('sprite_walking_img/L5.png')
L6 = pygame.image.load('sprite_walking_img/L6.png')
L7 = pygame.image.load('sprite_walking_img/L7.png')
L8 = pygame.image.load('sprite_walking_img/L8.png')
L9 = pygame.image.load('sprite_walking_img/L9.png')
R1 = pygame.image.load('sprite_walking_img/R1.png')
R2 = pygame.image.load('sprite_walking_img/R2.png')
R3 = pygame.image.load('sprite_walking_img/R3.png')
R4 = pygame.image.load('sprite_walking_img/R4.png')
R5 = pygame.image.load('sprite_walking_img/R5.png')
R6 = pygame.image.load('sprite_walking_img/R6.png')
R7 = pygame.image.load('sprite_walking_img/R7.png')
R8 = pygame.image.load('sprite_walking_img/R8.png')
R9 = pygame.image.load('sprite_walking_img/R9.png')
grass = pygame.image.load('blocks/grass_dirt.jpeg')
dirt = pygame.image.load('blocks/dirt.jpeg')
sand = pygame.image.load('blocks/realistic_sand.jpeg')
grass = pygame.transform.scale(grass, (50, 50))
dirt = pygame.transform.scale(dirt, (50, 50))
sand = pygame.transform.scale(sand, (50, 50))
standing = pygame.image.load('sprite_walking_img/standing.png')
screen = pygame.display.set_mode((1000, 700))
direction = 'none'
clock = pygame.time.Clock()
walk_num = 0
jump_num = 20
jumping = False
fall_frame = 0
falling = False
prev_height = 10000000
monsters = []
monster_direction = 'L'
monster_walk_num = 1
spitting_fire = False
monster_falling = False
monster_jumping = True
monster_jump_num = 10
monster_fall_frame = 0
for i in range(len(blocks)):
  if blocks[i][0] == 'monster':
    monsters.append([blocks[i][1], blocks[i][2], 1, 'L'])
for i in range(len(monsters)):
  for i in range(len(blocks)):
    if blocks[i][0] == 'monster':
      del blocks[i]
      break
for i in range(len(blocks)):
  if blocks[i][0] == 'grass':
    blocks[i][0] = grass
  elif blocks[i][0] == 'sand':
    blocks[i][0] = sand
  elif blocks[i][0] == 'dirt':
    blocks[i][0] = dirt
monster_walk_num = 1
monster_direction = 'L'
monster_prev_height = 100000000
monster_dead = False
avitar_dead = False
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  key = pygame.key.get_pressed()
  if key[pygame.K_LEFT] and avitar_x + 18 > 0:
    hit = False
    for i in range(len(blocks)):
      if (avitar_x + 14) - 6 < blocks[i][1] + 50 and avitar_x + 14 > blocks[i][1] + 50 and avitar_y < 40 + blocks[i][2] and avitar_y > blocks[i][2] - 40 and blocks[i][0] != end_pad:
        hit = True
    if not hit:
      avitar_x -= vel
      if direction != 'L':
        walk_num = 1
        direction = 'L'
      else:
        walk_num += 1
  elif key[pygame.K_RIGHT] and avitar_x + 18 < 1000:
    hit = False
    for i in range(len(blocks)):
      if (avitar_x - 14) + 50 + 6 > blocks[i][1] and (avitar_x + 50) - 14 < blocks[i][1] and avitar_y < 40 + blocks[i][2] and avitar_y > blocks[i][2] - 40 and blocks[i][0] != end_pad:
        hit = True
    if not hit:
      avitar_x += vel
      if direction != 'R':
        walk_num = 1
        direction = 'R'
      else:
        walk_num += 1
  #for b in range(len(monsters)):
  #  if avitar_x < monsters[b][1]:
  #    hit = False
  #    for i in range(len(blocks)):
  #      if monsters[x][0] - 6 < blocks[i][1] + 50 and monsters[x][0] + 14 > blocks[i][0] + 50 and monsters[x][1] < 40 + blocks[i][2] and avitar_y > blocks[i][2] - 40:
  #        hit = True
  #    if not hit:
  #      monsters[x][0] -= vel
  #      if monsters[x][3] != 'L':
  #        monsters[x][2] = 1
  #        monsters[x][3] = 'L'
  #      else:
  #        monsters[x][2] += 1
  #for i in range(len(monsters)):
  else:
    direction = 'none'
  if key[pygame.K_UP] and jumping != True and falling != True:
    jumping = True
  if walk_num > 8:
    walk_num = 1
  if direction == 'none':
    img = standing
  else:
    exec('img = {}{}'.format(direction, walk_num))
  if jumping:
    jump_num -= 1
    hit = False
    for i in range(len(blocks)):
      if blocks[i][0] != end_pad:
        if avitar_x + 39 >= blocks[i][1] and avitar_x <= 39 + blocks[i][1] and avitar_y >= blocks[i][2] + 50 and avitar_y <= blocks[i][2] + 55:
          hit = True
    if not hit:
      avitar_y -= (jump_num ** 2) / 20
    if jump_num == 0:
      jumping = False
      jump_num = 20
  if falling:
    fall_frame += 1
  if not jumping:
    falling = True
    for i in range(len(blocks)):
      if avitar_x + 30 >= blocks[i][1] and avitar_x <= blocks[i][1] + 30 and avitar_y + 50 <= blocks[i][2] and avitar_y + 50 >= blocks[i][2] - 5:
        falling = False
      if avitar_x + 30 >= blocks[i][1] and avitar_x <= blocks[i][1] + 30 and prev_height + 50 < blocks[i][2] and avitar_y + 50 + ((fall_frame ** 2) / 20) > blocks[i][2]:
        falling = False
        avitar_y = blocks[i][2] - 50
      if avitar_x + 30 >= end_x and avitar_x + 40 <= end_x + 50 and avitar_y + 50 <= end_y + 50 and avitar_y + 50 >= (end_y + 50) - 5:
        falling = False
      if avitar_x + 30 >= end_x and avitar_x <= end_x + 30 and prev_height + 50 < end_y + 50 and avitar_y + 50 + ((fall_frame ** 2) / 20) > end_y + 50:
        falling = False
        avitar_y = end_y
  if not falling:
    fall_frame = 0
  avitar_y += (fall_frame ** 2) / 20
  screen.fill((0, 255, 0))
  if not avitar_dead:
    screen.blit(img, (avitar_x, avitar_y))
  for i in range(len(blocks)):
    screen.blit(blocks[i][0], (blocks[i][1], blocks[i][2]))
  #for x in range(len(monsters)):
  #  exec('screen.blit({}E, (monsters[x][0], monsters[x][1]))'.format(str(monsters[x][3]) + str(monsters[x][2])))
  prev_height = avitar_y
  #print(monsters)
  #print(walk_num)
  if key[pygame.K_a] and monster_x + 18 > 0:
    spitting_fire = False
    hit = False
    for i in range(len(blocks)):
      if (monster_x + 14) - 6 < blocks[i][1] + 50 and monster_x + 14 > blocks[i][1] + 50 and monster_y < 40 + blocks[i][2] and monster_y > blocks[i][2] - 40 and blocks[i][0] != end_pad:
        hit = True
    if not hit:
      monster_x -= monster_vel
      if monster_direction != 'L':
        monster_walk_num = 1
        monster_direction = 'L'
      else:
        monster_walk_num += 1
  elif key[pygame.K_d] and monster_x + 18 < 1000:
    spitting_fire = False
    hit = False
    for i in range(len(blocks)):
      if (monster_x - 14) + 50 + 6 > blocks[i][1] and (monster_x + 50) - 14 < blocks[i][1] and monster_y < 40 + blocks[i][2] and monster_y > blocks[i][2] - 40 and blocks[i][0] != end_pad:
        hit = True
    if not hit:
      monster_x += monster_vel
      if monster_direction != 'R':
        monster_walk_num = 1
        monster_direction = 'R'
      else:
        monster_walk_num += 1
  elif monster_falling != True and key[pygame.K_s] and monster_jumping != True and monster_dead != True:
    walk_num = 1
    spitting_fire = True
    if monster_direction == 'R' and avitar_x + 14 < monster_x + 40 + 36 and avitar_y + 30 > monster_y and avitar_y < monster_y + 30:
      avitar_dead = True
    elif monster_direction == 'L' and (avitar_x + 50) - 14 < monster_x + 14 and (avitar_x + 50) - 14 > monster_x - 30 and avitar_y + 30 > monster_y and avitar_y < monster_y + 30:
      avitar_dead = True
  else:
    spitting_fire = False
    monster_walk_num = 1
  if key[pygame.K_w] and monster_jumping != True and monster_falling != True:
    monster_jumping = True
  if monster_walk_num > 8:
    monster_walk_num = 1
  if monster_direction != 'none':
    exec('img = {}{}E'.format(monster_direction, monster_walk_num))
  else:
    exec('img = {}{}E'.format(monster_direction, 1))
    walk_num = 1
    spitting_fire = False
  if monster_jumping:
    monster_jump_num -= 1
    hit = False
    for i in range(len(blocks)):
      if monster_x + 39 >= blocks[i][1] and monster_x <= 39 + blocks[i][1] and monster_y >= blocks[i][2] + 50 and monster_y <= blocks[i][2] + 55:
        hit = True
    if not hit:
      monster_y -= (monster_jump_num ** 2) / 20
    if monster_jump_num == 0:
      monster_jumping = False
      monster_jump_num = 20
  if monster_falling:
    monster_fall_frame += 1
  if not monster_jumping:
    monster_falling = True
    for i in range(len(blocks)):
      if monster_x + 30 >= blocks[i][1] and monster_x <= blocks[i][1] + 30 and monster_y + 50 <= blocks[i][2] and monster_y + 50 >= blocks[i][2] - 5:
        monster_falling = False      
      if monster_x + 30 >= blocks[i][1] and monster_x <= blocks[i][1] + 30 and monster_prev_height + 50 < blocks[i][2] and monster_y + 50 + ((monster_fall_frame ** 2) / 20) > blocks[i][2]:
        monster_falling = False
        monster_y = blocks[i][2] - 50
  if not monster_falling:
    monster_fall_frame = 0
  monster_y += (monster_fall_frame ** 2) / 20
  #screen.fill((0, 255, 0))
  if not monster_dead:
    screen.blit(img, (monster_x, monster_y))
  for i in range(len(blocks)):
    screen.blit(blocks[i][0], (blocks[i][1], blocks[i][2]))
  if not monster_dead:
    if spitting_fire:
      if monster_direction == "L":
        screen.blit(fire_left, ((monster_x + 20) - 50, monster_y))
      else:
        screen.blit(fire_right, ((monster_x + 50) - 23, monster_y))
  if not monster_dead:
    screen.blit(end_pad, (end_x, end_y))
  if avitar_x + 10 >= end_x and avitar_y >= end_y and avitar_y + 50 <= end_y + 50 and (avitar_x + 50) - 7 <= end_x + 50:
    monster_dead = True
  elif avitar_y + (fall_frame ** 2) / 20 > end_y + 50 and avitar_y + 50 < end_y and avitar_x + 10 >= end_x and (avitar_x + 50) - 7 <= end_x + 50:
    monster_dead = True
  pygame.display.update()
  monster_prev_height = monster_y
  #print(monsters)
  #print(walk_num)
  if time_dead > 5:
    break
  if monster_dead == True or avitar_dead == True:
    time_dead += 1 
  clock.tick(70)
time.sleep(3)
