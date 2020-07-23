#importa las librerias que se van a usar
import socket
import threading
import pygame,sys
from pygame.locals import *
from random import randint
from random import sample

#Genera el servidor con la ip y la cantidad de clientes que va a recibir 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8080))
server.listen(4)



#define dos variables globales y una lista vacia que es el mazo  
global jugadores
global deck
deck=[]

#Define la clase jugador
class Jugador:
    #funciones para controlar las acciones de cada jugador
    #init inicia a cada jugador con un defuse
    def __init__(self):
        #self.activo = False
        self.lista=['cartaDefuse']
    #funcion para revolver el deck, usa el metodo sample() que toma valores al azar y los reacomoda 
    def usarShuffle(self): 
        global deck
        deck=sample(deck,len(deck))
        self.lista.remove('cartaShuffle')
        
    #Funcion que enseña las siguientes tres cartas, usa el metodo pop() que saca el ultimo valor de la lista y lo elimina
    def usarFuture(self): 
        self.lista.remove('cartaFuture')
        aux=deck
        listaS=[]
        for i in range(3):
            n=aux.pop()
            listaS=listaS+[n]
            print(listaS)
            print(i+1,':',n)
    #funcion del comodin, se le quita una carta al jugador y se le agrega al que uso la carta    
    #función entra el jugador al que se le va a quitar la carta
    def usarComodin1(self,jugador):
        x=randint(0,len(jugador.lista))
        n=jugador.lista.pop(x)
        self.lista.append(n)
        self.lista.remove('cartaComodin1')
        self.lista.remove('cartaComodin1')
    def usarComodin2(self,jugador): #A la función entra el jugador al que se le va a quitar la carta
        x=randint(0,len(jugador.lista))
        n=jugador.lista.pop(x)
        self.lista.append(n)
        self.lista.remove('cartaComodin2')
        self.lista.remove('cartaComodin2')
    def usarComodin3(self,jugador): #A la función entra el jugador al que se le va a quitar la carta
        x=randint(0,len(jugador.lista))
        n=jugador.lista.pop(x)
        self.lista.append(n)
        self.lista.remove('cartaComodin3')
        self.lista.remove('cartaComodin3')
    def usarComodin4(self,jugador): #A la función entra el jugador al que se le va a quitar la carta
        x=randint(0,len(jugador.lista))
        n=jugador.lista.pop(x)
        self.lista.append(n)
        self.lista.remove('cartaComodin4')
        self.lista.remove('cartaComodin4')
    def usarComodin5(self,jugador): #A la función entra el jugador al que se le va a quitar la carta
        x=randint(0,len(jugador.lista))
        n=jugador.lista.pop(x)
        self.lista.append(n)
        self.lista.remove('cartaComodin5')
        self.lista.remove('cartaComodin5')
    #funcion que agrega una carta al jugador y verifica si es bomba y hace la respectiva accion
    def agarrarCarta(self):
        x=deck.pop()
        self.lista.append(x)
        if x=='cartaBomba':
            n=self.lista.count('cartaDefuse')
            self.lista.remove('cartaBomba')
            if n!=0:
                self.lista.remove('cartaDefuse')
            else:
                
                self.activo=False #Se pone en falso el activo para saber que deja de jugar
    #funcion que llamma la funcion darCarta con la clase jugador 
    def usarFavor(self,jugador):
        self.lista.remove('cartaFavor')
        jugador.darCarta()
    #funcion que da la carata deseada por el jugador
    def darCarta(self):
        carta='cartaDefuse' #Carta variable, por defecto Defuse, pero varia a lo que el jugaor elija
        self.lista.remove(carta)
        
#funcion que crea el deck de forma aleatoria, depende la cantidad de cartas por jugador
#y llama la funcion para repartirlas
def crearDeck(jugadores):
    if jugadores==3 or jugadores==4:
        cartaDefuse=6-jugadores
    else:
        cartaDefuse=2
    cartaFavor=4
    cartaShuffle=4
    cartaFuture=5
    cartaComodin1=4
    cartaComodin2=4
    cartaComodin3=4
    cartaComodin4=4
    cartaComodin5=4
    cartasBomba=jugadores-1
    total=cartaDefuse+cartaFavor+cartaShuffle+cartaFuture+cartaComodin1+cartaComodin2+cartaComodin3+cartaComodin4+cartaComodin5

    for i in range(total):
        x=randint(0,len(deck))
        if cartaDefuse != 0:
            deck.insert(x,'cartaDefuse')
            cartaDefuse -= 1
        elif cartaFavor != 0:
            deck.insert(x,'cartaFavor')
            cartaFavor -= 1
        elif cartaShuffle != 0 :
            deck.insert(x,'cartaShuffle')
            cartaShuffle -= 1
        elif cartaFuture != 0 :
            deck.insert(x,'cartaFuture')
            cartaFuture -= 1
        elif cartaComodin1 !=0:
            deck.insert(x,'cartaComodin1')
            cartaComodin1 -= 1
        elif cartaComodin2 !=0:
            deck.insert(x,'cartaComodin2')
            cartaComodin2 -= 1
        elif cartaComodin3 !=0:
            deck.insert(x,'cartaComodin3')
            cartaComodin3 -= 1
        elif cartaComodin4 !=0:
            deck.insert(x,'cartaComodin4')
            cartaComodin4 -= 1
        elif cartaComodin5 !=0:
            deck.insert(x,'cartaComodin5')
            cartaComodin5 -= 1
    
    for i in range(cartasBomba):
        if jugadores==2:
            x=randint(0,len(deck)-14)
        elif jugadores==3:
            x=randint(0,len(deck)-21)
        elif jugadores==4:
            x=randint(0,len(deck)-28)
        deck.insert(x,'cartaBomba')
    repartirCartas()
    return deck 

#funcion que reparte las cartas a los jugadores activos
def repartirCartas():
    if jugador1.activo:
        for i in range(7):
            x=deck.pop()
            jugador1.lista.append(x)
    if jugador2.activo:
        for i in range(7):
            x=deck.pop()
            jugador2.lista.append(x)
    if jugador3.activo:
        for i in range(7):
            x=deck.pop()
            jugador3.lista.append(x)
    if jugador4.activo:
        for i in range(7):
            x=deck.pop()
            jugador4.lista.append(x)
            

                
jugador1=Jugador()
jugador2=Jugador()
jugador3=Jugador()
jugador4=Jugador()





#print('Deck:',deck) #Printea en Shell, No hay que printear el deck
#print('Jugador 1:',jugador1.lista) #Printea las cartas de cada jugador 
#print('Jugador 2:',jugador2.lista) #No hay que printearlas 
#print('Jugador 3:',jugador3.lista)
#print('Jugador 4:',jugador4.lista)

'''print('-------------------------') #Para comprobar agarrarCarta
jugador1.agarrarCarta()
print(deck)
print(jugador1.lista)
print(jugador1.activo)
'''

'''print('-----------------------') #Para comprobar Shuffle
jugador1.usarShuffle()
print(deck)
print(jugador1.lista)
'''


'''print('-----------------------') #Para comprobar Favor
jugador1.usarFavor(jugador2)
print(jugador1.lista)
print(jugador2.lista)
'''

'''print('-----------------------') #Para comprobar Comodin
jugador1.usarComodin1(jugador2) #Para que funcione, tiene que tener 2 comodines 1
print(jugador1.lista)
print(jugador2.lista)
'''

'''
print('-----------------------') #Para comprobar Future
jugador1.usarFuture() 
print(jugador1.lista)
'''

#funcion que controla a los clientes, recibe y envia los mensajes entre el cliente y el servidor 
def manejoCliente(conn,addr):
    print(f'[Jugador {threading.activeCount()-2}] Conectado.')
    connected = True
    while connected:
        msg_l = conn.recv(64).decode('utf-8')
        if msg_l:
            msg_l = int(msg_l)
            msg = conn.recv(msg_l).decode('utf-8')
            print(f'[{addr}] {msg}')
            conn.send(f'{jugador1.lista}'.encode('utf-8'))
        if msg=='2':
            jugador1.activo=True
            jugador2.activo=True
            jugador3.activo=False
            jugador4.activo=False
            jugadores=2
            #print('2')
            crearDeck(jugadores)
        if msg=='3':
            jugador1.activo=True
            jugador2.activo=True
            jugador3.activo=True
            jugador4.activo=False
            jugadores=3
            #print('3')
            crearDeck(jugadores)
        if msg=='4':
            jugador1.activo=True
            jugador2.activo=True
            jugador3.activo=True
            jugador4.activo=True
            jugadores=4
            #print('4')
            crearDeck(jugadores)
        if msg=='defuse':
            print('rec defuse')
        if msg=='shuffle':
            jugador1.usarShuffle()
            #print('rec shuffle')
            conn.send('Cartas Revueltas'.encode('utf-8'))
        if msg=='favor':
            jugador1.usarFavor(jugador2)
            #print('rec favor')
        if msg=='STF':
            jugador1.usarFuture()
            #print('rec STF')
        if msg=='Comodin':
            jugador1.usarComodin1(jugador2)
            #print('rec Comodin')
        if msg=='Robar':
            jugador1.agarrarCarta()
            #print('rec Robar')
    
#funcion que inicia el servidor, controla la cantidad de clientes activos
#tambien abre un hilo con la funcion manejoClientes para que este constantemente recibiendo y enviando mensajes
def start():
    print(f'[Servidor] Server activo {socket.gethostbyname(socket.gethostname())}')
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=manejoCliente, args=(conn,addr))
        thread.start()
        numeroJ=threading.activeCount()
        print(f'[activo]{numeroJ - 2}')

print('Iniciando el servidor')
start()
