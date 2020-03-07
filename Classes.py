import config
import pygame
import random

pygame.init()

class tela():
    def __init__(self):
        self.width = config.totalW  #define altura e largura do objeto
        self.height = config.totalH
    

class Passaro(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self) # inicializa o sprite


		self.animation = [
		pygame.image.load('assets/bluebird-upflap.png').convert_alpha(),
		pygame.image.load('assets/bluebird-midflap.png').convert_alpha(),
		pygame.image.load('assets/bluebird-downflap.png').convert_alpha()] # animacao do objeto

		self.image = pygame.image.load('assets/bluebird-midflap.png').convert_alpha() # carrega o sprite incial
		self.current_img = 0


		self.rect = self.image.get_rect()
		self.rect[0] = 180	#Posicao inical de X
		self.rect[1] = 120	# "         "   de Y

		self.speed = config.speed

	def update(self):
		self.current_img = (self.current_img + 1) % 3 # looping 1 2 3	
		self.image = self.animation[self.current_img] # troca a img dentro do loop
		self.rect[1] += self.speed			# velocidade constante de 10 px/f
		self.speed += config.NaturalDownForce # aceleração de 1 px/f
		#print(self.speed) # DEBUG func, printa a velocidade do joojador
	def jump(self):
		self.speed = -config.speed


class Obstaculo(pygame.sprite.Sprite):
	def __init__(self,inverted, x,height):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('assets/pipe-green.png')
		self.image = pygame.transform.scale(self.image,(config.obsW,config.obsH))

		self.rect = self.image.get_rect()
		self.rect[0] = x

		if inverted == True:
			self.image = pygame.transform.flip(self.image, False, True) # axis X flip false, axis y flip 
			self.rect[1] = -(self.rect[3] - height)				#posiciona o obstaculo no ceu
		else:
			self.rect[1] = config.totalH - height				# posiciona o obstaculo no chao
																# o excedente é a distância entre um obstaculo e outro 

		self.mask = pygame.mask.from_surface(self.image)

	def update(self):
		self.rect[0] -= config.speed # move os obstaculos na direção oposta do jogador




class Chao(pygame.sprite.Sprite):
	def __init__(self,x):
		pygame.sprite.Sprite.__init__(self)
		self.width = config.totalW * 2
		self.height = 100
		self.image = pygame.image.load('assets/base.png')
		self.image = pygame.transform.scale(self.image,(self.width,self.height))
		self.rect = self.image.get_rect()
		self.rect[0] = x
		self.rect[1] = config.totalH - 100

		self.mask = pygame.mask.from_surface(self.image)

	def update(self):
		self.rect[0] -= config.speed



def is_off_screen(sprite): # verifica se o sprite saiu da tela
	return sprite.rect[0] < -(sprite.rect[2])  #se sua posicao for menor que o tamanho total do objeto negativo


def get_random_obst(xpos):
	size  = random.randint(100, 300)
	obst  = Obstaculo(False, xpos, size)
	obst_inverted  = Obstaculo(True, xpos, config.totalH - size - config.Distancia_obst)
	return (obst, obst_inverted)