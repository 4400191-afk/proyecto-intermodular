import pygame
import random

pygame.init()
pantalla = pygame.display.set_mode((800, 400))
pygame.display.set_caption("NEONDASH")
reloj = pygame.time.Clock()
fuente = pygame.font.SysFont(None, 36)

# Jugador
jugador = pygame.Rect(100, 300, 30, 30) 
velocidad_y = 0
gravedad = 1

# Juego
puntuacion = 0
obstaculos = []
temporizador = 0

estado = "MENU"
nombre = ""

def enviar_puntuacion(nombre_jugador, puntos):
    with open("puntuaciones.txt", "a") as archivo:
        archivo.write(nombre_jugador + "," + str(puntos) + "\n")

ejecutando = True
while ejecutando:

    pantalla.fill((10, 10, 20)) 

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

        if estado == "MENU":
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    estado = "JUGANDO"
                elif evento.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]   
                else:
                    nombre += evento.unicode

        elif estado == "FIN_JUEGO":
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    jugador.y = 300
                    velocidad_y = 0
                    puntuacion = 0
                    obstaculos = []
                    estado = "JUGANDO"

    if estado == "MENU":
        pantalla.blit(fuente.render("Nombre: " + nombre, True, (255, 255, 255)), (250, 150))
        pantalla.blit(fuente.render("ENTER para jugar", True, (200, 200, 200)), (250, 200))

    elif estado == "JUGANDO":
        pygame.draw.line(pantalla, (0, 255, 255), (0, 330), (800, 330), 2)

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_SPACE] and jugador.y == 300:
            velocidad_y = -15

        velocidad_y += gravedad
        jugador.y += velocidad_y
        
        if jugador.y > 300:
            jugador.y = 300

        puntuacion += 1
        temporizador += 1

        if temporizador > random.randint(30, 60):

            ancho_azar = random.randint(15, 40)  
            alto_azar = random.randint(20, 50)  
            
            nuevo_obstaculo = pygame.Rect(800, 330 - alto_azar, ancho_azar, alto_azar)
            
            obstaculos.append(nuevo_obstaculo)
            temporizador = 0

        for obstaculo in obstaculos:
            obstaculo.x -= 7
          
            pygame.draw.rect(pantalla, (255, 0, 0), obstaculo)
            
            if jugador.colliderect(obstaculo):
                enviar_puntuacion(nombre, puntuacion)
                estado = "FIN_JUEGO"

        pygame.draw.rect(pantalla, (0, 255, 0), jugador)
        pantalla.blit(fuente.render("Puntuación: " + str(puntuacion), True, (255, 255, 255)), (10, 10))

    elif estado == "FIN_JUEGO":
        pantalla.blit(fuente.render("FIN DEL JUEGO", True, (255, 0, 0)), (300, 150))
        pantalla.blit(fuente.render("ESPACIO para reiniciar", True, (200, 200, 200)), (255, 200))

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()