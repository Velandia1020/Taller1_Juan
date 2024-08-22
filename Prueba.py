import math
import time
import os

# Configuración de la espiral
width, height = 40, 20
frames = 100
speed = 0.8 #velocidad

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_spiral(t):
    for y in range(-height // 3, height // 3):
        for x in range(-width // 3, width // 3):
            distance = math.sqrt(x**2 + y**2)
            angle = distance * 0.5 + t
            char = '*' if math.cos(angle) > 0 else ' '
            print(char, end='')
        print()

def animate_spiral():
    t = 0
    while True:
        clear_console()
        draw_spiral(t)
        time.sleep(speed)
        t += 0.2

if __name__ == "__main__":
    animate_spiral()
