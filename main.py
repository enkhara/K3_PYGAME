import pygame as pg 
# para importar una serie de constantes que tiene paygame com las teclas de teclado
from pygame.locals import *
import sys
import random

#constantes

_fps = 60

#Clases y Funciones utilizadas
'''
class Ball(pg.sprite.Sprite):
    #cuadrado con su posicion y color
    def __init__(self,x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface(16, 16)
        self.rect = self.image.get_rect()

        self.x = x
        self.y = y
        
        self.color = (255, 2555, 255) #RGB color blanco 

        #iniciar la parte grafica
        self.rect.x = self.x
        self.rect.y = self.y
        self.image.fill(self.color)#pinta el recuadro de este color (blanco = 255, 255, 255)
'''

class Raquet(pg.Surface):
    x = 0
    y = 0
    w = 16
    h = 96
    color = (255, 255, 255)
    velocidad = 15
    diry = 1

    def __init__(self):
        pg.Surface.__init__(self, (self.w, self.h))
        self.fill(self.color)
    
    def setColor(self, color):
        self.color = color
        self.fill(self.color) 
    
    def avanza(self):
        self.y += self.diry * self.velocidad

        if self.y <= 0:
            self.y = 0
            
        if self.y >= 600 - self.h:
            self.y = 600 - self.h
        
        #direccion positiva o negativa y la velocidad separado 
        



class Ball(pg.Surface):

    x = 0
    y = 0
    w = 16
    h = 16
    color = (255, 255, 255)
    velocidad = 5
    dirx = velocidad
    diry = velocidad

    def __init__(self):
        pg.Surface.__init__(self, (self.w, self.h))
        self.fill((self.color))

    def setColor(self, color):
        self.color = color
        self.fill(self.color)   
    
    def avanza(self):
        if self.x >= 800:
            self.dirx = -self.velocidad
        if self.x <= 0:
            self.dirx = self.velocidad
        if self.y >= 600:
            self.diry = -self.velocidad
        if self.y <= 0:
            self.diry = self.velocidad
        
        self.x += self.dirx
        self.y += self.diry

    def comprobarChoque(self, candidata):

        '''
        if candidata.x >= self.x and candidata.x <= self.x+16 or \
            candidata.x+16 >= self.x and candidata.x+16 <= self.x+16:
            return True
        else:
            return False
        '''
        #equivalente al if de arriba
        '''
        if (candidata.x >= self.x and candidata.x <= self.x+16 or \
            candidata.x+16 >= self.x and candidata.x+16 <= self.x+16) and \
            (candidata.y >= self.y and candidata.y <= self.y+16 or \
            candidata.y+16 >= self.y and candidata.y+16 <= self.y+16):
            return True
        else:
            return False
        '''
        if (candidata.x >= self.x and candidata.x <= self.x+self.w or \
            candidata.x+candidata.w >= self.x and candidata.x+candidata.w <= self.x+self.w) and \
            (candidata.y >= self.y and candidata.y <= self.y+self.h or \
            candidata.y+candidata.h >= self.y and candidata.y+candidata.h <= self.y+self.h):

            #si chocan cambiamos la direccion de las x
            self.dirx = self.dirx * -1
            self.x += self.dirx


 

class Game:
    clock = pg.time.Clock()
    

    def __init__(self, width, height):
        self.size = (width, height)
        self.display = pg.display #instanciamos un objeto de tipo display
        #creamor la pantalla y le ponemos indicamos un título
        self.screen = self.display.set_mode(self.size) #pantalla de nuestro juego
        self.screen.fill((60,60,60))
        self.display.set_caption('Mi juego') #titulo pantalla juego

        
        #posicionamos la bola en la pantalla
        #self.ball = Ball(392, 292) 
        self.ball1 = Ball()
        self.ball1.setColor((255,0,0))
        self.ball1.x =random.randrange(800)
        self.ball1.y = random.randrange(600)
        self.ball1.velocidad = random.randrange(2,9)

        self.player1 = Raquet()
        self.player1.x = 768
        self.player1.y = 252
        
        '''
        #crea una tupla de objeto Ball()
        self.balls = []
        
        #para crear 5 bolas de clase Ball() con atributos random
        for i in range(random.randrange(5,15)):
            b= Ball()
            b.setColor((random.randrange(256),random.randrange(256),random.randrange(256)))
            b.x = random.randrange(800)
            b.y = random.randrange(600)
            b.velocidad = random.randrange(10)

            #añade a la lista de bolas la bola que se acaba de crear
            self.balls.append(b)
        '''
    
    def start (self):

       
        #bucle principal del juego
        while True:
            self.clock.tick(_fps)
            #control de los eventos, entradas de teclado y ratón
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()
                
                if event.type ==KEYDOWN:
                    if event.key == K_UP:
                        self.player1.diry = -1
                        self.player1.avanza()
            
                    if event.key == K_DOWN:
                        self.player1.diry = 1
                        self.player1.avanza()
            #modifica la posición de ball
            self.ball1.avanza()
            self.ball1.comprobarChoque(self.player1)
            
           
            '''
            for ball in self.balls:
                ball.avanza()
            '''
            #Pintar los sprites en screen
            #refresca la pantalla fill vuelve a pintar el fondo de pantalla
            self.screen.fill((60,60,60))
            #que situe en pantalla la bola que hemos creando
            '''
            equivalente al siguiente for, es mejor por que aún no sabiendo el numero de bolas que hay las podemos gestionar todas
            for i in range(5):
                self.screen.blit(self.balls[i], (self.balls[i].x, self.balls[i].y))
            '''

            '''
            for ball in self.balls:
                self.screen.blit(ball, (ball.x, ball.y))
            '''

            self.screen.blit(self.ball1, (self.ball1.x, self.ball1.y))
            self.screen.blit(self.player1,(self.player1.x, self.player1.y))
          

            self.display.flip()

if __name__ == "__main__":
    pg.init()
    game = Game (800, 600)
    game.start()
    