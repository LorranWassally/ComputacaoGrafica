def BresIncli(x1,y1,x2,y2):
    incli = (y2-y1)/(x2-x1)
    return incli

def BresFinal(x1,y1,x2,y2):
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
BresFinal(0,0,5,2)