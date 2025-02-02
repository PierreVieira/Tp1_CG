from src.colisao import *
from src.menu_pause import *
from src.arquivos import *
from src.globais import *
from src import objetos_primeira_parte, globais
from pygame import mixer
from src.objetos_segunda_parte import *
def conversao(x, y):
    if x < 300:
        x = -(100 -x/3)
    else:
        x = x/3 - 100
    if y < 350:
        y = 100 - y/3.5
    else:
        y = -(y/3.5 - 100)
    return (x, y)
def reorganizar(lista):
    for c in range(len(lista)):
        x_object = randint(-95, 95)
        y_object = randint(-95, 0)
        while(analise_de_proximidade(x_object, y_object, lista, 22)):
            x_object = randint(-95, 95)
            y_object = randint(-95, 0)
        lista[c]['x'] = x_object
        lista[c]['y'] = y_object
    return lista

def voltando_ao_inicio():
    globais.anzol['y'] = 90
    globais.anzol['x'] = 0
    globais.parte = 'menu'
    globais.cont_fora_da_tela = 0
    nova_lista = []
    for c in objetos_primeira_parte.all1:
        c['id'] = 0
        nova_lista.append(c)
    for i in range(25):
        globais.s2 -= 6
        vida['x'] = globais.s2
        objetos_segunda_parte.lives.append(vida.copy())
    objetos_primeira_parte.all1 = reorganizar(nova_lista)
    globais.esta_pausado = False
    globais.aux_musica = True

def movimentoMouse(x, y):
    x, y = conversao(x, y)
    seguidor_mouse['x'] = x
    seguidor_mouse['y'] = y
    if globais.parte == 'menu':
        if collision(seguidor_mouse, botao_iniciar_jogo):
            botao_borda['x'] = botao_iniciar_jogo['x']
            botao_borda['y'] = botao_iniciar_jogo['y']
        elif collision(seguidor_mouse, botao_creditos):
            botao_borda['x'] = botao_creditos['x']
            botao_borda['y'] = botao_creditos['y']
        elif collision(seguidor_mouse, botao_sair):
            botao_borda['x'] = botao_sair['x']
            botao_borda['y'] = botao_sair['y']
        elif collision(seguidor_mouse, botao_instrucoes):
            botao_borda['x'] = botao_instrucoes['x']
            botao_borda['y'] = botao_instrucoes['y']
        elif collision(seguidor_mouse, botao_ranking):
            botao_borda['x'] = botao_ranking['x']
            botao_borda['y'] = botao_ranking['y']
        else:
            botao_borda['x'] = 3000
            botao_borda['y'] = 3000

def clicks_do_mouse(button, state, x, y):
    if button == GLUT_LEFT_BUTTON:
        if globais.parte == 'menu':
            if collision(seguidor_mouse, botao_iniciar_jogo):
                globais.parte = 1
                globais.aux_musica = True
            elif collision(seguidor_mouse, botao_creditos):
                globais.parte = 'creditos'
                globais.aux_musica = True
            elif collision(seguidor_mouse, botao_sair):
                exit()
            elif collision(seguidor_mouse, botao_instrucoes):
                globais.parte = 'instrucoes'
            elif collision(seguidor_mouse, botao_ranking):
                globais.parte = 'ranking'
                exibir_resultado()

        if globais.esta_pausado:
            if collision(seguidor_mouse, voltar_menu_principal):
                globais.esta_querendo_confirmar = False
                globais.ultima_tecla = 114
                voltando_ao_inicio()
            elif collision(seguidor_mouse, audio_switchE):
                mixer.music.set_volume(0)
            elif collision(seguidor_mouse, audio_switchD):
                mixer.music.set_volume(100)
            elif collision(seguidor_mouse, quitar_game):
                globais.esta_querendo_confirmar = True
                globais.ultima_tecla = 27
    elif button == GLUT_RIGHT_BUTTON and not(globais.parte == 1 or globais.parte == 2 or globais.parte == 3):
        globais.aux_musica = True
        globais.parte = 'menu'