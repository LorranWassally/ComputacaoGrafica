# Função para calcular o ponto de interseção entre uma aresta do polígono e o limite da janela de recorte
def intersect(p1, p2, clip_edge):
    x1, y1 = p1
    x2, y2 = p2
    if clip_edge == 'left':
        x, y = x_min, y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
    elif clip_edge == 'right':
        x, y = x_max, y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
    elif clip_edge == 'bottom':
        x, y = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1), y_min
    elif clip_edge == 'top':
        x, y = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1), y_max
    return (x, y)
# Função para verificar se um ponto está dentro da área de recorte para um dado lado de recorte
def inside(p, clip_edge):
    x, y = p
    if clip_edge == 'left':
        return x >= x_min
    elif clip_edge == 'right':
        return x <= x_max
    elif clip_edge == 'bottom':
        return y >= y_min
    elif clip_edge == 'top':
        return y <= y_max
# Função principal do algoritmo de Sutherland-Hodgman
def sutherland_hodgman_clip(polygon, clip_window):
    def clip_polygon(polygon, clip_edge):
        clipped_polygon = []
        p1 = polygon[-1]
        for p2 in polygon:
            if inside(p2, clip_edge):
                if not inside(p1, clip_edge):
                    clipped_polygon.append(intersect(p1, p2, clip_edge))
                clipped_polygon.append(p2)
            elif inside(p1, clip_edge):
                clipped_polygon.append(intersect(p1, p2, clip_edge))
            p1 = p2
        return clipped_polygon

    # Definindo os lados da janela de recorte
    for edge in ['left', 'right', 'bottom', 'top']:
        polygon = clip_polygon(polygon, edge)
    return polygon
# Definindo a janela de recorte
x_min, y_min = 10, 10
x_max, y_max = 100, 100
# Definindo o polígono original
polygon = [(5, 5), (120, 10), (120, 120), (10, 120)]
# Realizando o recorte
clipped_polygon = sutherland_hodgman_clip(polygon, [(x_min, y_min), (x_max,
y_max)])
# Resultado final do polígono recortado
print(f"Polígono recortado: {clipped_polygon}")