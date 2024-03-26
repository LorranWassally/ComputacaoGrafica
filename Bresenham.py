def BresIncli(x1,y1,x2,y2):
    incli = (y2-y1)/(x2-x1)
    return incli

def Bres1oct(x1,y1,x2,y2):
    x=x1
    y=y1
    incli = BresIncli(x1,y1,x2,y2)
    e=incli+0.5
    print(x,y)
    while x < x2:
        if e >= 1:
            e=e-1
            y=y+1
        x=x+1
        e=e+incli
        print(x,y)
    return

def Bres2oct(x1,y1,x2,y2):
    x=y1
    y=x1
    incli = BresIncli(y1,x1,y2,x2)
    e=incli+0.5
    print(y,x)
    while x < y2:
        if e >= 1:
            e=e-1
            y=y+1
        x=x+1
        e=e+incli
        print(y,x)
    return

def Bres8oct(x1,y1,x2,y2):
    x=x1
    y=y1*-1
    incli = BresIncli(x1,y1*-1,x2,y2*-1)
    e=incli+0.5
    print(x,y*-1)
    while x < x2:
        if e >= 1:
            e=e-1
            y=y+1
        x=x+1
        e=e+incli
        print(x,y*-1)
    return

Bres8oct(0,0,5,-2)