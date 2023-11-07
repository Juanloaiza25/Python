# ...
import time
import turtle
import random

Posponer = 0.12

#Variables Marcador

Score = 0
High_Score = 0
#Funcion Para resetear Marcador

def resetear_marcador():

    Marcador.clear()
    Marcador.write("Score: {}          High Score: {}".format(Score, High_Score), align="center", font=("Courier", 12))

#Funcion de Morir       

def morir():
    global Score
    Score = 0
    Cabeza.goto(0,0)
    Cabeza.direction = "stop"
    time.sleep(Posponer)
    for segment in Cuerpo:
        segment.goto(1000, 1000)
    Cuerpo.clear()

    

#Ventana

window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("black")
window.setup(width=600, height=600)
window.tracer(0)

#Cabeza de la serpiente

Cabeza = turtle.Turtle()
Cabeza.speed(0)
Cabeza.shape("square")
Cabeza.penup()
Cabeza.goto(0,0)
Cabeza.direction = "stop"
Cabeza.color("white")

#Comida

Comida = turtle.Turtle()
Comida.speed(0)
Comida.shape("circle")
Comida.penup()
Comida.goto(0,100)
Comida.color("red")

#Cuerpo de la serpiente

Cuerpo = []

#Marcador

Marcador = turtle.Turtle()
Marcador.speed(0)
Marcador.shape("square")
Marcador.penup()
Marcador.goto(0,260)
Marcador.color("white")
Marcador.hideturtle()
Marcador.write("Score: 0          High Score: 0", align="center", font=("Courier", 12))



# Funciones para mover la cabeza del snake

def arriba():
    Cabeza.direction = "up"

def abajo():
    Cabeza.direction = "down"

def izquierda():
    Cabeza.direction = "left"

def derecha():
    Cabeza.direction = "right"
    
def move():

    if Cabeza.direction == "up":
        y = Cabeza.ycor()
        Cabeza.sety(y + 20)

    if Cabeza.direction == "down":
        y = Cabeza.ycor()
        Cabeza.sety(y - 20)

    if Cabeza.direction == "left":
        x = Cabeza.xcor()
        Cabeza.setx(x - 20)

    if Cabeza.direction == "right":
        x = Cabeza.xcor()
        Cabeza.setx(x + 20)            

# Teclado
window.listen()
window.onkeypress(arriba, "Up")
window.onkeypress(abajo, "Down")
window.onkeypress(izquierda, "Left")
window.onkeypress(derecha, "Right")

# Bucle principal del juego
while True:
    window.update()

    #Colisiones bordes

    if Cabeza.xcor() > 280 or Cabeza.xcor() < -280 or Cabeza.ycor() > 280 or Cabeza.ycor() < -280:
        morir()
        resetear_marcador()
        
        

    #Colisiones Comida

    if Cabeza.distance(Comida) < 25:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        Comida.goto(x,y)
        ParteNueva = turtle.Turtle()
        ParteNueva.speed(0)
        ParteNueva.shape("square")
        ParteNueva.penup()
        ParteNueva.color("grey")
        Cuerpo.append(ParteNueva)

        #Aumentar marcador

        Score += 10
        if Score > High_Score:
            High_Score = Score
        Marcador.clear()
        Marcador.write("Score: {}          High Score: {}".format(Score, High_Score), align="center", font=("Courier", 12))

    #Mover el cuerpo de la serpiente

    PartesTotales = len(Cuerpo)
    for index in range(PartesTotales -1, 0, -1):
        x = Cuerpo[index - 1].xcor()
        y = Cuerpo[index - 1].ycor()
        Cuerpo[index].goto(x,y)
    if PartesTotales > 0:
        x = Cabeza.xcor()
        y = Cabeza.ycor()
        Cuerpo[0].goto(x,y)

    move()
    #Colisiones con el cuerpo

    for segment in Cuerpo:
        if segment.distance(Cabeza) < 20:
            morir()
            resetear_marcador()
            


    time.sleep(Posponer)


