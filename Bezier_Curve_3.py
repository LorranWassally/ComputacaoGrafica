import numpy as np
import matplotlib.pyplot as plt

# Pontos de controle
P0 = np.array([0, 0])
P1 = np.array([2, 4])
P2 = np.array([4, 0])
P3 = np.array([6, 2])  # Adicionando o quarto ponto de controle

# Função para calcular a curva de Bézier cúbica
def bezier_cubica(t, P0, P1, P2, P3):
    return (1 - t)**3 * P0 + 3 * (1 - t)**2 * t * P1 + 3 * (1 - t) * t**2 * P2 + t**3 * P3

# Valores de t de 0 a 1
t = np.linspace(0, 1, 100)

# Calculando a curva
bezier_curve = np.array([bezier_cubica(ti, P0, P1, P2, P3) for ti in t])

# Gráfico
plt.plot(bezier_curve[:, 0], bezier_curve[:, 1], label='Curva de Bézier Cúbica')
plt.scatter([P0[0], P1[0], P2[0], P3[0]], [P0[1], P1[1], P2[1], P3[1]], color='red', label='Pontos de Controle')
plt.plot([P0[0], P1[0], P2[0], P3[0]], [P0[1], P1[1], P2[1], P3[1]], '--', color='gray', label="Polígono de Controle")
plt.legend()
plt.title("Curva de Bézier Cúbica")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.axis("equal")
plt.show()