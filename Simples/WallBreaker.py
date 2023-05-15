import pygame
pygame.init()


def coli(x1,y1,tamx1,tamy1, x2,y2,tamx2,tamy2):
    x = False
    y = False
    for i in range(x2, x2 + tamx2):
        if x1 == i or x1+tamx1 == i:
            x = True 
            break
    for i in range(y2, y2 +tamy2):
        if y1 == i or y1+tamy1 == i:
            y = True
            break
    if (x and y):
        if  x1 > x2+tamx2/2:
            return 1
        return 2
    return False

largura = 250
altura = 250

fundo = (0,0,60)
p = (0, 100, 200)
b = (0, 200, 100)

pos_x_p1 = 125
pos_y_p1 = 215
segunda_vez = True

pos_x_b1 = 125
pos_y_b1 = 200
vx = 1
vy = 3
dano = 100
toque = True

tela = pygame.display.set_mode((largura, altura), pygame.RESIZABLE | pygame.SCALED)
pygame.display.set_caption("Quebra Parede")

relogio = pygame.time.Clock()
inicio = True

blocos =[]
for t in range(0, 3):
    for i in range(0, 10):
        cor = pygame.Color(150, 150, 150)
        x = 0 + (i*25)
        y = 0 + (t*25)
        dados = [cor , x, y]
        blocos.append(dados)
    
while inicio:
    tela.fill(fundo)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            inicio = False

    for i in blocos:
        if coli(pos_x_b1, pos_y_b1, 15, 15, i[1], i[2], 25, 25) != False:
            vy *= -1
            vx *= -1
            if i[0].r - dano > 0:
                i[0].r -= dano
                i[0].g -= dano
                i[0].b -= dano
            else:
                blocos_falso = blocos.copy()
                blocos_falso.pop(blocos.index(i))
                blocos = blocos_falso
            segunda_vez = True
        pygame.draw.rect(tela, i[0], (i[1], i[2], 25, 25))

    if coli(pos_x_b1, pos_y_b1, 15, 15,  pos_x_p1, pos_y_p1, 70, 5) != False and segunda_vez:
        vx = abs(vx)
        if coli(pos_x_b1, pos_y_b1, 15, 15,  pos_x_p1, pos_y_p1, 70, 5) != 1:
            vx *= -1
        vy *= -1
        segunda_vez = False
        toque = True
        
    if pos_x_b1 < 0:
        vx = abs(vx)
        segunda_vez = True
        toque = True
    if pos_x_b1 > largura - 15:
        vx = abs(vx) *- 1
        segunda_vez = True
        toque = True
    if pos_y_b1 < 0:
        vy = abs(vy)
        segunda_vez = True
        toque = True
    if pos_y_b1 > altura - 15:
        vy = abs(vy) * -1
        segunda_vez = True
        toque = True

    pos_x_b1 += vx
    pos_y_b1 += vy


    if pygame.key.get_pressed()[pygame.K_LEFT]:
        pos_x_p1 -= 3
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        pos_x_p1 += 3

    if pos_x_p1 < 0:
        pos_x_p1 += 3
    if pos_x_p1 > largura - 70:
        pos_x_p1 -= 3

    
    pygame.draw.rect(tela, p, (pos_x_p1, pos_y_p1, 70, 5))
    pygame.draw.rect(tela, b, (pos_x_b1, pos_y_b1, 15, 15))


    if blocos == []:
        toque = True
        pos_x_b1 = 125
        pos_y_b1 = 200
        vx = 1
        vy = 3
        pos_x_p1 = 125
        pos_y_p1 = 215
        segunda_vez = True
        if dano != 10:
            dano -= 10
        for t in range(0, 3):
            for i in range(0, 10):
                cor = pygame.Color(100, 100, 100)
                x = 0 + (i*25)
                y = 0 + (t*25)
                dados = [cor , x, y]
                blocos.append(dados)
        pygame.time.delay(500)
        

    relogio.tick(60)
    pygame.display.flip()
    
pygame.quit()
