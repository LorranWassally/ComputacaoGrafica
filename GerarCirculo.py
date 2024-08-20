def Draw8(x, y, xc, yc):
    print(x,y)
    pass

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
        Draw8(y, x, xc=0, yc=0)
        Draw8(-x, y, xc=0,yc=0)
        Draw8(y, -x, xc=0,yc=0)
        Draw8(x, -y, xc=0,yc=0)
        Draw8(-y, x, xc=0,yc=0)
        Draw8(-x, -y, xc=0,yc=0)
        Draw8(-y, -x, xc=0,yc=0)

AlgCirculo(raio=10)