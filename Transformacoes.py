def Translacao(x1,y1,x2,y2):
    if x1>=0:
        transx=0-x1
    elif x1<=0:
        transx=0+x1
    if y1>=0:
        transy=0-y1
    elif y1<=0:
        transy=0+y1
    return(x1+transx,x2+transx,y1+transy,y2+transy,transx,transy)

def TranslacaoReversa(x1,y1,x2,y2,transx,transy):
    return(x1+transx,x2+transy,y1+transy,y2+transy)

def Escala(x1,y1,x2,y2,escx,escy):
    return(x1*escx,x2*escx,y1*escy,y2*escy)

def Rotacao(x1,y1,x2,y2,rot):
    if rot == 30:
        sen = 0.5
        cos = 0.85
    elif rot == 45:
        sen = 0.65
        cos = 0.65
    elif rot == 60:
        sen = 0.85
        cos = 0.5

    x1 = x1*cos - y1*sen
    y1 = x1*sen - y1*cos
    x2 = x2*cos - y2*sen
    y2 = x2*sen - y2*cos
    return (x1,x2,y1,y2)

def transformacoes(x1,y1,x2,y2,escx,escy,rot,transx,transy):
    x1,x2,y1,y2,transxt,transyt = Translacao(x1,y1,x2,y2)
    x1,x2,y1,y2 = Escala(x1,y1,x2,y2,escx,escy)
    x1,x2,y1,y2 = Rotacao(x1,y1,x2,y2,rot)
    x1,x2,y1,y2 = TranslacaoReversa(x1,y1,x2,y2,transxt,transyt)

    return (x1,y1,x2,y2)