import pygame
import sys
import random


class Player:
	def __init__(self, x, y, color, speed, image):
		self.x = x
		self.y = y
		self.width = image.get_width()
		self.height = image.get_height()
		self.color = color
		self.rect = pygame.Rect(x,y,self.width,self.height)
		self.speed = speed
		self.image = image

	def move(self, dir):
		self.x+= (self.speed*dir)
		self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
		
	def draw(self, surface):
		#pygame.draw.rect(surface,self.color,self.rect)
		surface.blit(self.image, (self.x, self.y))


class Enemy:
	def __init__(self, x, y, color, speed, image):
		self.x = x
		self.y = y
		self.color = color
		self.speed = speed
		self.image = image
		self.width = image.get_width()
		self.height = image.get_height()
		self.rect = pygame.Rect(x,y,self.width,self.height)

	def move(self):
		self.y+= self.speed
		self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

	def draw(self, surface):
		#pygame.draw.rect(surface,self.color,self.rect)
		surface.blit(self.image, (self.x, self.y))

	def reset(self):
		self.y = 0-20
		self.x = random.randint(0,SCREENWIDTH)
		self.rect = pygame.Rect(self.x, self.y, self.width, self.height)






pygame.init()

SCREENWIDTH = 600
SCREENHEIGHT = 600

game_display = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
clock = pygame.time.Clock()
score = 0
font_size = 40
font = pygame.font.SysFont(None, font_size)
score_surface = font.render(f"Score: {score}", True, (255,255,0))
game_over_surface = font.render("Game Over!! Press "+ "Space"+" to restart", True, (0,100,155))
game_over = False

#colors
bg_color = (0,0,0)
player_color = (0,0,255)
enemy_color = (255,0,0)

# images
player_image = pygame.image.load("Red_Ship_Space.png")
player_image = pygame.transform.scale2x(player_image)
enemy_image = pygame.image.load("Green_Ship_Space.png")
enemy_image = pygame.transform.scale2x(enemy_image)

# player , enemy
player = Player(SCREENWIDTH/2 - 30, SCREENHEIGHT - 60, player_color, 50, player_image)
enemy1 = Enemy(random.randint(0,SCREENWIDTH), 0 -20, enemy_color, 10, enemy_image)
enemy2 = Enemy(random.randint(0,SCREENWIDTH), 0-20, enemy_color, 10, enemy_image)
enemies = [enemy1, enemy2]

run = True
while run:
	clock.tick(30)
	# event
	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			pygame.quit()
			sys.exit()

		if(event.type == pygame.KEYDOWN):
			if(event.key == pygame.K_LEFT and player.rect.left > 0 and game_over == False):

				player.move(-1)

			if(event.key == pygame.K_RIGHT and player.rect.right < SCREENWIDTH and game_over == False):

				player.move(1)

			if(event.key == pygame.K_SPACE and game_over == True):
				score = 0
				game_over = False
				enemy1 = Enemy(random.randint(0,SCREENWIDTH), 0 -20, enemy_color, 10, enemy_image)
				enemy2 = Enemy(random.randint(0,SCREENWIDTH), 0-20, enemy_color, 10, enemy_image)
				enemies = [enemy1, enemy2]
				score_surface = font.render(f"Score: {score}", True,(255,255,0))







	# update

	for enemy in enemies:
		if(game_over == False):

			enemy.move()
			if(enemy.rect.top > SCREENHEIGHT):
				enemy.reset()
				score+=1
				score_surface = font.render(f"Score: {score}", True,(255,255,0))

			if(enemy.rect.colliderect(player.rect)):
				game_over = True
				



	# drawing

	game_display.fill(bg_color)
	player.draw(game_display)
	for enemy in enemies:
		enemy.draw(game_display)

	game_display.blit(score_surface,(SCREENWIDTH-score_surface.get_width(),0))
	if(game_over == True):
		game_display.blit(game_over_surface, (SCREENWIDTH//2 - game_over_surface.get_width()//2 , SCREENHEIGHT//2- game_over_surface.get_height()//2))

	pygame.display.flip()

