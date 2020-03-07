import pygame
from pygame.locals import *
from Classes import *

pygame.init()

#loading
display = tela()
tela_jogo = pygame.display.set_mode((display.width, display.height))
bg = pygame.image.load('assets/background-day.png')
bg = pygame.transform.scale(bg,(display.width, display.height))


grupo_jogador = pygame.sprite.Group() # cria um grupo
obj_jogador = Passaro()					  # constroi o objeto
grupo_jogador.add(obj_jogador)			  # adiciona o objeto no grupo

grupo_chao = pygame.sprite.Group()
for i in range(2): # cria 2 objetos chao 
	obj_chao = Chao(2*config.totalW * i) # altura e posição dos objetos
	grupo_chao.add(obj_chao)


grupo_obst = pygame.sprite.Group()
for i in range(2):
	obj_obst = get_random_obst(config.totalW * i + 800)
	grupo_obst.add(obj_obst[0])
	grupo_obst.add(obj_obst[1])



#tela_jogo.blit(bg, (0,0)) # DEBUG aceleração visivel

fps = pygame.time.Clock()
#laco principal
while True:
	fps.tick(30)

	tela_jogo.blit(bg, (0,0)) # poe o backGround na tela


	for evento in pygame.event.get():
		if evento.type == KEYDOWN and evento.key == K_SPACE:
			obj_jogador.jump()
		if evento.type == QUIT:
			pygame.quit()
	

	if is_off_screen(grupo_chao.sprites()[0]): #repete os objetos chao indefinidamente
		grupo_chao.remove(grupo_chao.sprites()[0])
		new_chao = Chao(2*config.totalW - 20) # -20 tapa buraco
		grupo_chao.add(new_chao) 

	if is_off_screen(grupo_obst.sprites()[0]):
		grupo_obst.remove(grupo_obst.sprites()[0])	# remove o cano
		grupo_obst.remove(grupo_obst.sprites()[0])	# remove o cano flipado
		new_obst = get_random_obst(config.totalW * 2) # sem folga
		grupo_obst.add(new_obst[0])
		grupo_obst.add(new_obst[1])
		print(grupo_obst)


	if pygame.sprite.groupcollide(grupo_jogador,grupo_chao,False,False): #false false remove from groups 1 n 2
		break

	if pygame.sprite.groupcollide(grupo_jogador,grupo_obst,False,False):
		break


	grupo_jogador.update()	
	grupo_jogador.draw(tela_jogo)	# mostra todos elementos do grupo na superficie

	grupo_chao.update()
	grupo_chao.draw(tela_jogo)

	grupo_obst.update()
	grupo_obst.draw(tela_jogo)

	pygame.display.update()	  #desenha cada frame
     

print('GAME OVER, Magrao')