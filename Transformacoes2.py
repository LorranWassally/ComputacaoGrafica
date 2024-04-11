def translacao(x,y,transx,transy):
    return (x+transx,y+transy)

def escala(x,y,escx,escy):
    transx = 0-x
    transy = 0-y
    x = x+transx
    y = y+transy
    x1 = round(x*escx)
    y1 = round(y*escy)
    x1 = x-transx
    y1 = y-transy
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
    transx = 0-x
    transy = 0-y
    x = x+transx
    y = y+transy
    x1 = x*cos+y*-sen
    y1 = x*sen+y*cos
    x1 = x1-transx
    y1 = y1-transy
    
    return (x1,y1)