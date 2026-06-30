trajectory = [10, 20, 30, 40, 50]

def robot_move(trajectory):
    for angle in trajectory:
        print(f"Robot arm moving to angle {angle}°")

robot_move(trajectory)

# Nota:
# Este script simula el movimiento repetitivo de un brazo robótico,
# mostrando ángulos secuenciales como si siguiera una trayectoria simple.
# Representa lógica básica de automatización usada en cobots y robots industriales.
