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

def escala(x1,y1,x2,y2,escx,escy):
    return(x1*escx,x2*escx,y1*escy,y2*escy)

def transformacoes(x1,y1,x2,y2,escx,escy,rot):
    return