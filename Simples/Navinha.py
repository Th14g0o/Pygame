import pygame
from random import randrange
pygame.init()

fundo = (0,0,0)
cor_nave_p1 = (100,100,100)
cor_vidro_p1 = (0, 200, 255)
cor_bala = (250, 150, 0)
cor_vida = (255, 0, 0)
cor_nave_inimigo = (0, 150, 0)
cor_vidro_inimigo = (0, 255, 100)
cor_score = (255,255,255)

largura = 300
altura = 300
score = 0.00

pos_x_p1 = largura/2
pos_y_p1 = altura - 20
pos_x_b1 = 0
pos_y_b1 = 0
tiro1 = False
dano = 0

pos_x_inimigo1 = randrange(19, largura -30, 10)
pos_y_inimigo1 = randrange(-90, -40, 10)
pos_x_inimigo2 = randrange(19, largura -30, 10)
pos_y_inimigo2 = randrange(-140, -40, 10)

pos_x_vida = 15
pos_y_vida = 25

tela = pygame.display.set_mode((largura, altura), pygame.RESIZABLE | pygame.SCALED)
pygame.display.set_caption("Navinha")

inicio = True
FPS = pygame.time.Clock()

def texto(msg, tam, cor, x, y):
    fonte = pygame.font.SysFont("comicsansms", tam )
    text = fonte.render(msg, True, cor)
    tela.blit(text, (x, y))

def vida(x, y):
    pygame.draw.rect(tela, cor_vida, (x, y, 5, 5))

    pygame.draw.rect(tela, cor_vida, (x-5, y-5, 5, 5))
    pygame.draw.rect(tela, cor_vida, (x, y-5, 5, 5))
    pygame.draw.rect(tela, cor_vida, (x+5, y-5, 5, 5))
    
    pygame.draw.rect(tela, cor_vida, (x-5, y-10, 5, 5))
    pygame.draw.rect(tela, cor_vida, (x-10, y-10, 5, 5))
    pygame.draw.rect(tela, cor_vida, (x, y-10, 5, 5))
    pygame.draw.rect(tela, cor_vida, (x+5, y-10, 5, 5))
    pygame.draw.rect(tela, cor_vida, (x+10, y-10, 5, 5))
     
    pygame.draw.rect(tela, cor_vida, (x-5, y-15, 5, 5))
    pygame.draw.rect(tela, cor_vida, (x-10, y-15, 5, 5))
    pygame.draw.rect(tela, cor_vida, (x, y-15, 5, 5))
    pygame.draw.rect(tela, cor_vida, (x+5, y-15, 5, 5))
    pygame.draw.rect(tela, cor_vida, (x+10, y-15, 5, 5))

    pygame.draw.rect(tela, cor_vida, (x+5, y-20, 5, 5))
    pygame.draw.rect(tela, cor_vida, (x-5, y-20, 5, 5))

    
    
def nave_p(x, y):
    pygame.draw.rect(tela, cor_nave_p1, (x, y, 10, 10))

    pygame.draw.rect(tela, cor_nave_p1, (x-10, y - 10, 10, 10))
    pygame.draw.rect(tela, cor_nave_p1, (x-20, y - 10, 10, 10))
    pygame.draw.rect(tela, cor_nave_p1, (x, y - 10, 10, 10))
    pygame.draw.rect(tela, cor_nave_p1, (x+10, y - 10, 10, 10))
    pygame.draw.rect(tela, cor_nave_p1, (x+20, y - 10, 10, 10))

    pygame.draw.rect(tela, cor_nave_p1, (x-10, y - 20, 10, 10))
    pygame.draw.rect(tela, cor_vidro_p1, (x, y - 20, 10, 10))
    pygame.draw.rect(tela, cor_nave_p1, (x+10, y - 20, 10, 10))
    
    pygame.draw.rect(tela, cor_nave_p1, (x, y - 30, 10, 10))
    pygame.draw.rect(tela, cor_nave_p1, (x, y - 40, 10, 10))

def inimigo(x,y):
    pygame.draw.rect(tela, cor_nave_inimigo, (x, y, 10, 10))

    pygame.draw.rect(tela, cor_nave_inimigo, (x-10, y-10, 10, 10))
    pygame.draw.rect(tela, cor_vidro_inimigo, (x, y-10, 10, 10))
    pygame.draw.rect(tela, cor_nave_inimigo, (x+10, y-10, 10, 10))

    pygame.draw.rect(tela, cor_nave_inimigo, (x-20, y-20, 10, 10))
    pygame.draw.rect(tela, cor_vidro_inimigo, (x-10, y-20, 10, 10))
    pygame.draw.rect(tela, cor_nave_inimigo, (x, y-20, 10, 10))
    pygame.draw.rect(tela, cor_vidro_inimigo, (x+10, y-20, 10, 10))
    pygame.draw.rect(tela, cor_nave_inimigo, (x+20, y-20, 10, 10))

    pygame.draw.rect(tela, cor_nave_inimigo, (x+10, y-30, 10, 10))
    pygame.draw.rect(tela, cor_nave_inimigo, (x+20, y-30, 10, 10))
    pygame.draw.rect(tela, cor_nave_inimigo, (x+20, y-40, 10, 10))

    pygame.draw.rect(tela, cor_nave_inimigo, (x-10, y-30, 10, 10))
    pygame.draw.rect(tela, cor_nave_inimigo, (x-20, y-30, 10, 10))
    pygame.draw.rect(tela, cor_nave_inimigo, (x-20, y-40, 10, 10))

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

while inicio:
    tela.fill(fundo)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            inicio = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a and tiro1 == False:
                pos_x_b1 = pos_x_p1
                pos_y_b1 = pos_y_p1- 40
                tiro1 = True

    if pygame.key.get_pressed()[pygame.K_LEFT]:
        pos_x_p1 -= 5
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        pos_x_p1 += 5

    if pos_x_p1 + 30 > largura:
        pos_x_p1 -= 5
    if pos_x_p1 - 20 < 0:
        pos_x_p1 += 5
        
    if tiro1:
        pygame.draw.rect(tela, cor_bala, (pos_x_b1, pos_y_b1, 10, 10))
    pos_y_b1 -= 4
    if pos_y_b1 + 10 < 0:
        tiro1 = False

    pos_y_inimigo1 += 3
    pos_y_inimigo2 += 3

    if pos_y_inimigo1 > altura+40:
        pos_x_inimigo1 = randrange(19,largura -30, 10)
        pos_y_inimigo1 = randrange(-140, -40, 10)
    if pos_y_inimigo2 > altura+40:
        pos_x_inimigo2 = randrange(19,largura -30, 10)
        pos_y_inimigo2 = randrange(-90, -40, 10)
    
    if colisao_simples(pos_x_b1, pos_y_b1, 10, 10, pos_x_inimigo1-20, pos_y_inimigo1-40, 40, 40):
        pos_x_inimigo1 = randrange(19,largura -30, 10)
        pos_y_inimigo1 = randrange(-140, -40, 10)
    if colisao_simples(pos_x_b1, pos_y_b1, 10, 10, pos_x_inimigo2-20, pos_y_inimigo2-40, 40, 40):
        pos_x_inimigo2 = randrange(19,largura -30, 10)
        pos_y_inimigo2 = randrange(-140, -40, 10)
        
    if colisao_simples(pos_x_p1-20, pos_y_p1-40, 40, 40, pos_x_inimigo2-20, pos_y_inimigo2-40, 40, 40):
        dano += 1
        pos_x_inimigo2 = randrange(19,largura -30, 10)
        pos_y_inimigo2 = randrange(-90, -40, 10)
    if colisao_simples(pos_x_p1-20, pos_y_p1-40, 40, 40, pos_x_inimigo1-20, pos_y_inimigo1-40, 40, 40):
        dano += 1
        pos_x_inimigo1 = randrange(19,largura -30, 10)
        pos_y_inimigo1 = randrange(-90, -40, 10)
        

    if dano == 3:
        inicio = False
    inimigo(pos_x_inimigo1, pos_y_inimigo1)
    inimigo(pos_x_inimigo2, pos_y_inimigo2)
    
    nave_p(pos_x_p1, pos_y_p1)

    if dano <= 2:
        vida(pos_x_vida , pos_y_vida)
    if dano <= 1:
        vida((pos_x_vida*2)+ 15 , pos_y_vida)
    if dano == 0:
        vida((pos_x_vida*3)+ 30 , pos_y_vida)

    texto(f"Score: {int(score)}", 20, cor_score, largura/3, 5)
    score += 0.05
    
    pos_x_p1
    FPS.tick(60)
    pygame.display.flip()

pygame.quit()
    
