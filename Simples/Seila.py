import pygame
from random import randrange
pygame.init()

largura = 600
altura = 600

azul = (0,0,150)
branco = (255, 255, 255)
cor_1 = (0,160, 255)
cor_2 = (200,255, 160)
cor_3 = (255,255, 100)
cor_selected = (0,244, 32)
cor_venceu = (0, 240, 244)

pos_p1_x = 0
pos_p1_y = 0
pos_p2_x = 600-5
pos_p2_y = 0

pos_ball_x = 300 
pos_ball_y = 300
direction = randrange(-2, 2)
v_ball_y = 5
v_ball_x = 2
if direction < 1:
    v_ball_x = -2

tela = pygame.display.set_mode((largura, altura), pygame.RESIZABLE | pygame.SCALED)
pygame.display.set_caption("Game0001")

relogio = pygame.time.Clock()
inicio = True
continuar = ""

def texto(msg, cor, tam, x, y):
        estilo_da_fonte = pygame.font.SysFont("comicsansms", tam)
        mensagem = estilo_da_fonte.render(msg, True, cor)
        tela.blit(mensagem, (x, y))
def colisao_simples(x1,y1, tamx1, tamy1, x2, y2, tamx2, tamy2):
    x = False
    y = False
    for i in range(x2, x2 + tamx2):
        if x1 <= i <= x1 + tamx1:
            x = True
    for i in range(y2, y2 + tamy2):
        if y1 <= i <= y1 + tamy1:
            y = True
    if x == True and y == True:
        return True
    else:
        return False

def Fim(player):
    gameover = True
    decision = True
    while gameover:
        tela.fill((0,0,0))

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                gameover = False
                return False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    if decision == False:
                        return False
                    else:
                        return True

        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            decision = False
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            decision = True
        
        if (player == 1):
            texto("Player 1 venceu!", cor_venceu, 20, 210, 100)
        else:
            texto("Player 2 venceu!", cor_venceu, 20, 210, 100)

        if decision:
            texto("Reiniciar", cor_selected, 20, 110, 300)
            texto("Acabar", branco, 20, 400, 300)
        else:
            texto("Reiniciar", branco, 20, 110, 300)
            texto("Acabar", cor_selected, 20, 400, 300)
            
        
            
        relogio.tick(60)
        pygame.display.flip()
        
        
while inicio:
    tela.fill(azul)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            inicio = False
            
    if pygame.key.get_pressed()[pygame.K_w]:
        pos_p2_y -= 7
    if pygame.key.get_pressed()[pygame.K_s]:
        pos_p2_y += 7
            
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        pos_p1_y += 7
    if pygame.key.get_pressed()[pygame.K_UP]:
        pos_p1_y -= 7

    if pos_p1_y < 0:
        pos_p1_y += 5
    if pos_p1_y > altura - (100):
        pos_p1_y -= 5

    if pos_p2_y < 0:
        pos_p2_y += 5
    if pos_p2_y > altura - (100):
        pos_p2_y -= 5

    pos_ball_y += v_ball_y
    if pos_ball_y > 600 - 25:
        v_ball_y = -5
    if pos_ball_y < 0:
        v_ball_y = 5


    pos_ball_x += v_ball_x

    if colisao_simples(pos_p1_x, pos_p1_y, 5, 100, pos_ball_x, pos_ball_y, 25, 25) == True:
        v_ball_x *= -1
        v_ball_x += 1
    if colisao_simples(pos_p2_x, pos_p2_y, 5, 100, pos_ball_x, pos_ball_y, 25, 25) == True:
        v_ball_x *= -1
        v_ball_x -= 1

    if pos_ball_x < 0:
        inicio = Fim(2)
        pos_ball_x = 300 
        pos_ball_y = 300
        direction = randrange(-2, 2)
        v_ball_x = 2
        if direction < 1:
            v_ball_x = -2
    if pos_ball_x > 600:
        inicio = Fim(1)
        pos_ball_x = 300 
        pos_ball_y = 300
        direction = randrange(-2, 2)
        v_ball_x = 2
        if direction < 1:
            v_ball_x = -2
        
    pygame.draw.rect(tela, cor_1,(pos_p1_x, pos_p1_y, 5, 100))
    pygame.draw.rect(tela, cor_2,(pos_p2_x, pos_p2_y, 5, 100))
    pygame.draw.rect(tela, cor_3,(pos_ball_x, pos_ball_y, 25, 25))
    
    relogio.tick(60)
    pygame.display.flip()
    
pygame.quit()
