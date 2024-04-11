def translacao(x,y,transx,transy):
    return (x+transx,y+transy)

def escala(x,y,escx,escy):
    x1 = round(x*escx)
    y1 = round(y*escy)
    return(x1,y1)

def rotacao(x,y,rot):
    if rot == 30:
        sen = 0.5
        cos = 0.85
    elif rot == 45:
        sen = 0.65
        cos = 0.65
    elif rot == 60:
        sen = 0.85
        cos = 0.5
    x1 = x*cos+y*-sen
    y1 = x*sen+y*cos
    
    return (x1,y1)