#Proyecto 2 Exploding kittens
#importa la libreria socket y se conecta con el servidor
import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8080))
turno=False
#Importa la libreria pygame y la inicia
import pygame, sys
from pygame.locals import *
mainClock= pygame.time.Clock()
pygame.init()
#define las variables que se van a utilizar
GREEN = (0, 255, 0)
BLUE = (0, 0, 180)
global c1
global c2
global c3
global c4
global c5
global c6
c1=0
c2=0
c3=0
c4=0
c5=0
c6=0
#Genera la pantalla, color y tamano
background_colour = (0,0,0)
(width, height) = (800, 500)
screen = pygame.display.set_mode((width, height))
screen.fill(background_colour)
pygame.display.flip()

##Funciones de las cartas
##Funcion para enviar mensajes al servidor y recibirlos
def send(msg):
    message = msg.encode('utf-8')
    msg_l = len(message)
    send_l = str(msg_l).encode('utf-8')
    send_l += b' ' * (64 - len(send_l))
    client.send(send_l)
    client.send(message)
    msg=(client.recv(2048).decode('utf-8'))
    print(msg)
    lista=msg.split()
    print('.......................')
    print('lista: ',lista)
    print('.......................')
    #for para ver cual es el numero que se tiene de cada cartas
    for i in lista:
        if i=="['cartaDefuse'," or i=="['cartaDefuse']":
            global c1
            c1+=1
        if i=="'cartaShuffle',":
            global c2
            c2+=1
        if i=="'cartaFavor',":
            global c3
            c3+=1
        if i=="'cartaFuture',":
            global c4
            c4+=1
        elif i=="'cartaComodin1'," or i=="'cartaComodin2'," or i=="'cartaComodin3'," or i=="'cartaComodin4'," or i=="'cartaComodin5',":
            global c5
            c5+=1
    print('defuse',c1)
    print('Shuffle',c2)
    print('Favor',c3)
    print('Future',c4)
    print('Comodin',c5)
    ##Numeros posicion de los numeros
    #(15,270)
    #(175,270)
    #(335,270)
    #(495,270)
    #(655,270)
    #carga las imagenes de los numero
    cero = pygame.image.load('numeros/0.png')
    uno = pygame.image.load('numeros/1.png')
    dos = pygame.image.load('numeros/2.png')
    tres = pygame.image.load('numeros/3.png')
    cuatro = pygame.image.load('numeros/4.png')
    cinco = pygame.image.load('numeros/5.png')
    seis = pygame.image.load('numeros/6.png')
    siete = pygame.image.load('numeros/7.png')
    #if de cada carta para enseñar en pantalla la cantidad con imagenes
    #Defuse
    if c1==0:
        screen.blit(cero,(15,270))
    elif c1==1:
        screen.blit(uno,(15,270))
    elif c1==2:
        screen.blit(dos,(15,270))
    elif c1==3:
        screen.blit(tres,(15,270))
    elif c1==4:
        screen.blit(cuatro,(15,270))
    elif c1==5:
        screen.blit(cinco,(15,270))
        
    #Shuffle 
    if c2==0:
        screen.blit(cero,(175,270))
    elif c2==1:
        screen.blit(uno,(175,270))
    elif c2==2:
        screen.blit(dos,(175,270))
    elif c2==3:
        screen.blit(tres,(175,270))
    elif c2==4:
        screen.blit(cuatro,(15,270))

    #Favor
    if c3==0:
        screen.blit(cero,(335,270))
    elif c3==1:
        screen.blit(uno,(335,270))
    elif c3==2:
        screen.blit(dos,(335,270))
    elif c3==3:
        screen.blit(tres,(335,270))
    elif c3==4:
        screen.blit(cuatro,(335,270))

    #STF
    if c4==0:
        screen.blit(cero,(495,270))
    elif c4==1:
        screen.blit(uno,(495,270))
    elif c4==2:
        screen.blit(dos,(495,270))
    elif c4==3:
        screen.blit(tres,(495,270))
    elif c4==4:
        screen.blit(cuatro,(495,270))

    #Comodin
    if c5==0:
        screen.blit(cero,(655,270))
    elif c5==1:
        screen.blit(uno,(655,270))
    elif c5==2:
        screen.blit(dos,(655,270))
    elif c5==3:
        screen.blit(tres,(655,270))
    elif c5==4:
        screen.blit(cuatro,(655,270))
    elif c5==5:
        screen.blit(cinco,(655,270))
    elif c5==6:
        screen.blit(seis,(655,270))
    elif c5==7:
        screen.blit(siete,(655,270))
    #se devuelven los numeros para que se vuelvan a contar
    c1=0
    c2=0
    c3=0
    c4=0
    c5=0
    c6=0
    

#Nombre e icono de la ventana
#pygame.display.set_caption('Exploding Kittens')
icon = pygame.image.load('menuImg/cat.png')
pygame.display.set_icon(icon)

##Menu imagenes
click=False
#funcion del menu principal, muestra las imagenes y las formas clickeables   
def menu():
  click=False
  pygame.display.set_caption('Exploding Kittens')
  while True:
    b=pygame.Rect(310,250,270,40)
    pygame.draw.rect(screen,(0,0,0),b)
    
    b1=pygame.Rect(310,300,270,40)
    pygame.draw.rect(screen,(0,0,0),b1)

    b2=pygame.Rect(310,350,270,40)
    pygame.draw.rect(screen,(0,0,0),b2)
    
    mx, my = pygame.mouse.get_pos()
    
    botonPlay = pygame.image.load('menuImg/2 jugadores.png')
    screen.blit(botonPlay,(310,250))
    
    botonPlay1 = pygame.image.load('menuImg/3 jugadores.png')
    screen.blit(botonPlay1,(310,300))
    
    botonPlay2 = pygame.image.load('menuImg/4 jugadores.png')
    screen.blit(botonPlay2,(310,350))
    
    titulo = pygame.image.load('menuImg/titulo.png')
    screen.blit(titulo,(30,50))
    gato = pygame.image.load('menuImg/gato.png')
    screen.blit(gato,(-20,250))
    
    
    if b.collidepoint((mx,my)):
      if click:
        send('2')
        #print('opcion1')
        game(2)
    if b1.collidepoint((mx,my)):
      if click:
        send('3')
        #print('opcion2')
        game(3)
    if b2.collidepoint((mx,my)):
      if click:
        send('4')
        #print('opcion3')
        game(4)
        
    click=False
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == MOUSEBUTTONDOWN:
        if event.button == 1:
          click=True
          
    pygame.display.update()

#funcion del menu del juego, muestra las cartas y el tablero y genera las zonas clickeables
def game(jugadores):
  click=False
  pygame.display.set_caption('Juego')
  running = True
  screen.fill((70,0,0))
  pygame.display.flip()
  while running:
    mx, my = pygame.mouse.get_pos()
  ##Muestra las imagenes 
    ##Defuse(15,305)
    c=pygame.Rect(15,305,130,180)
    pygame.draw.rect(screen,(0,10,0),c)
    
    cartaDefuse = pygame.image.load('cartas/DEFUSE.png')
    screen.blit(cartaDefuse,(15,305))
    
    ##Shuffle(175,305)
    c1=pygame.Rect(175,305,130,180)
    pygame.draw.rect(screen,(0,0,0),c1)

    cartaShuffle = pygame.image.load('cartas/SHUFFLE.png')
    screen.blit(cartaShuffle,(175,305))
    
    ##Favor(335,305)
    c2=pygame.Rect(335,305,130,180)
    pygame.draw.rect(screen,(0,0,0),c2)
    
    cartaFavor = pygame.image.load('cartas/FAVOR.png')
    screen.blit(cartaFavor,(335,305))

    ##STF(495,305)
    c3=pygame.Rect(495,305,130,180)
    pygame.draw.rect(screen,(0,50,0),c3)

    cartaSTF = pygame.image.load('cartas/SEETHEFUTURE.png')
    screen.blit(cartaSTF,(495,305))

    ##Comidin(655,305)
    c4=pygame.Rect(655,305,130,180)
    pygame.draw.rect(screen,(0,0,100),c4)

    cartaComodin = pygame.image.load('cartas/COMODIN1.png')
    screen.blit(cartaComodin,(655,305))

    ##Robar(200,10)
    c5=pygame.Rect(255,70,130,180)
    pygame.draw.rect(screen,(0,0,100),c5)

    robar = pygame.image.load('cartas/cartas.png')
    screen.blit(robar,(170,10))

    ##Descarte(415,100)
    ##descarte=pygame.Rect(415,70,130,180)
    ##pygame.draw.rect(screen,(0,0,100),descarte)


  ###############################################################  
    if c.collidepoint((mx,my)):
      if click:
        screen.blit(cartaDefuse,(415,70))
        send('defuse')
        
    if c1.collidepoint((mx,my)):
      if click:
        screen.blit(cartaShuffle,(415,70))
        send('shuffle')
        
    if c2.collidepoint((mx,my)):
      if click:
        screen.blit(cartaFavor,(415,70))
        send('favor')
        
    if c3.collidepoint((mx,my)):
      if click:
        screen.blit(cartaSTF,(415,70))
        send('STF')
        
    if c4.collidepoint((mx,my)):
      if click:
        screen.blit(cartaComodin,(415,70))
        send('Comodin')

    if c5.collidepoint((mx,my)):
      if click:
        send('Robar')
        
    click=False
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == MOUSEBUTTONDOWN:
        if event.button == 1:
          click=True
      if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
          screen.fill((0,0,0))
          pygame.display.flip()
          running=False
          print('salir')
    
    pygame.display.update()
    mainClock.tick(60)

menu()
