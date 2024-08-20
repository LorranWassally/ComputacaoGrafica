import matplotlib.pyplot as plt

# Lista para armazenar os pontos
points = []

def Draw8(x, y, xc, yc):
    # Adiciona os pontos à lista
    points.append((xc + x, yc + y))
    points.append((xc - x, yc + y))
    points.append((xc + x, yc - y))
    points.append((xc - x, yc - y))
    points.append((xc + y, yc + x))
    points.append((xc - y, yc + x))
    points.append((xc + y, yc - x))
    points.append((xc - y, yc - x))

def AlgCirculo(raio):
    x = raio
    y = 0
    p = 5/4 - raio

    Draw8(x, y, xc=0, yc=0)

    while x > y:
        y += 1
        if p <= 0:
            p += 2 * y + 1
        else:
            x -= 1
            p += 2 * y - 2 * x + 1

        Draw8(x, y, xc=0, yc=0)

AlgCirculo(raio=10)

# Separando os pontos em listas para plotar
x_points, y_points = zip(*points)

# Criando o gráfico
plt.figure(figsize=(8, 8))
plt.scatter(x_points, y_points, c='blue', s=10)
plt.title('Pontos do Círculo usando o Algoritmo de Bresenham')
plt.xlabel('x')
plt.ylabel('y')
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.show()
