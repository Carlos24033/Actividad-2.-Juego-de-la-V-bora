"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""
from turtle import *
from random import randrange, choice
from freegames import square, vector

# Lista de 5 colores diferentes (excluyendo el rojo)
colores_disponibles = ['blue', 'green', 'purple', 'orange', 'yellow']

# Seleccionar colores aleatorios para que la víbora y la comida sean diferentes entre sí
color_vibora = choice(colores_disponibles)
colores_restantes = [c for c in colores_disponibles if c != color_vibora]
color_comida = choice(colores_restantes)

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    # Dibuja el cuerpo de la víbora con el color aleatorio asignado
    for body in snake:
        square(body.x, body.y, 9, color_vibora)

    # Dibuja la comida con el color aleatorio diferente
    square(food.x, food.y, 9, color_comida)
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
