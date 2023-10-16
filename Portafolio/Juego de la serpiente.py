import turtle
import time
import random

posponer = 0.1

#Marcador
score = 0
high_score = 0 

#Configuracion de la ventana
pantalla = turtle.Screen()
pantalla.title("Juego de la serpiente")
pantalla.bgcolor("black")
pantalla.setup(width = 600, height = 600)
pantalla.tracer(0)

#Cabeza serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"

#Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)

#Texto del marcador
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Score: 0   Hig score: 0", align = "center", font = ("Courier", 24, "normal") )

#Cuerpo serpiente
cuerpos = []

#Funciones
def arriba():
    cabeza.direction = "up"
def abajo():
    cabeza.direction = "down"
def derecha():
    cabeza.direction = "right"
def izquierda():
    cabeza.direction = "left"            

def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)

    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)

    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)     

#Teclado
pantalla.listen()
pantalla.onkeypress(arriba, "Up")
pantalla.onkeypress(abajo, "Down")
pantalla.onkeypress(derecha, "Right")
pantalla.onkeypress(izquierda, "Left")               

while True:
    pantalla.update()

    #Colisiones borde
    if cabeza.xcor() > 280 or cabeza.xcor() < -290  or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.dirrection = "stop"

        #Esconder los cuerpos
        for cuerpo in cuerpos:
            cuerpo.goto(5000,5000)

        #Reiniciar marcador
        score = 0
        texto.clear() 
        texto.write("Score: {}   Hig score: {}".format(score, high_score), align = "center", font = ("Courier", 24, "normal") )     

        #Limpiar los cuerpos
        cuerpos.clear()  

    #Coliciones comida
    if cabeza.distance(comida) < 20:
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        comida.goto(x,y)

        nuevo_cuerpos = turtle.Turtle()
        nuevo_cuerpos.speed(0)
        nuevo_cuerpos.shape("square")
        nuevo_cuerpos.color("grey")
        nuevo_cuerpos.penup()
        cuerpos.append(nuevo_cuerpos)

        #Aumentar marcador
        score += 10

        if score > high_score:
            high_score = score

        texto.clear() 
        texto.write("Score: {}   Hig score: {}".format(score, high_score), align = "center", font = ("Courier", 24, "normal") )     

    #Mover cuerpo
    totalSeg = len(cuerpos)
    for index in range(totalSeg -1, 0, -1):
        x = cuerpos[index -1].xcor()
        y = cuerpos[index -1].ycor()
        cuerpos[index].goto(x,y)
    
    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        cuerpos[0].goto(x,y)

    mov()

    #Coliciones cuerpo
    for cuerpo in cuerpos:
        if cuerpo.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction = "stop"

            #Esconder los cuerpos
            for cuerpo in cuerpos:
                cuerpo.goto(5000,5000)

                cuerpo.clear()

            #Reiniciar marcador
            score = 0
            texto.clear() 
            texto.write("Score: {}   Hig score: {}".format(score, high_score), align = "center", font = ("Courier", 24, "normal") )



    time.sleep(posponer)

