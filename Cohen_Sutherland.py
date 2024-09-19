# Definindo as regiões de código
INSIDE = 0 # 0000
LEFT = 1 # 0001
RIGHT = 2 # 0010
BOTTOM = 4 # 0100
TOP = 8 # 1000
# Definindo a janela de recorte
x_min, y_min = 10, 10
x_max, y_max = 200, 200
# Função para calcular o código da região
def compute_outcode(x, y):
    code = INSIDE
    if x < x_min:
        code |= LEFT
    elif x > x_max:
        code |= RIGHT
    if y < y_min:
        code |= BOTTOM
    elif y > y_max:
        code |= TOP
    return code
def cohen_sutherland_clip(x1, y1, x2, y2):
    outcode1 = compute_outcode(x1, y1)
    outcode2 = compute_outcode(x2, y2)
    accept = False
    while True:
        # Caso trivial: ambos os pontos estão dentro
        if outcode1 == 0 and outcode2 == 0:
            accept = True
            break
        # Caso trivial: a linha está fora da janela
        elif (outcode1 & outcode2) != 0:
            break
        else:
            # A linha cruza a janela, então precisa ser cortada
            x, y = 0, 0
            # Escolhe um ponto fora da janela
            if outcode1 != 0:
                outcode_out = outcode1
            else:
                outcode_out = outcode2
            # Calcula a interseção com os limites da janela
            if outcode_out & TOP: # ponto acima da janela
                x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
                y = y_max
            elif outcode_out & BOTTOM: # ponto abaixo da janela
                x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
                y = y_min
            elif outcode_out & RIGHT: # ponto à direita da janela
                y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
                x = x_max
            elif outcode_out & LEFT: # ponto à esquerda da janela
                y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
                x = x_min
            # Atualiza o ponto fora da janela com o novo ponto de interseção
            if outcode_out == outcode1:
                x1, y1 = x, y
                outcode1 = compute_outcode(x1, y1)
            else:
                x2, y2 = x, y
                outcode2 = compute_outcode(x2, y2)
    if accept:
        return (x1, y1, x2, y2) # Linha recortada
    else:
        return None # A linha está completamente fora da área de recorte
# Exemplo de uso
x1, y1 = 5, 5 # Ponto inicial da linha
x2, y2 = 150, 150 # Ponto final da linha
clipped_line = cohen_sutherland_clip(x1, y1, x2, y2)
if clipped_line:
 print(f"Linha recortada: {clipped_line}")
else:
 print("A linha está completamente fora da área de recorte.")