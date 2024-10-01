import numpy as np
import matplotlib.pyplot as plt
# Pontos de controle
P0 = np.array([0, 0])
P1 = np.array([1, 2])
P2 = np.array([2, 0])
# Função para calcular a curva de Bézier quadrática
def bezier_quadratica(t, P0, P1, P2):
    return (1 - t)**2 * P0 + 2 * (1 - t) * t * P1 + t**2 * P2
# Valores de t de 0 a 1
t = np.linspace(0, 1, 100)
# Calculando a curva
bezier_curve = np.array([bezier_quadratica(ti, P0, P1, P2) for ti in t])
# Gráfico
plt.plot(bezier_curve[:, 0], bezier_curve[:, 1], label='Curva de Bézier')
plt.scatter([P0[0], P1[0], P2[0]], [P0[1], P1[1], P2[1]], color='red', label='Pontos de Controle')
plt.plot([P0[0], P1[0], P2[0]], [P0[1], P1[1], P2[1]], '--', color='gray', label='Polígono de
Controle')
plt.legend()
plt.title("Curva de Bézier Quadrática")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.axis("equal")
plt.show()