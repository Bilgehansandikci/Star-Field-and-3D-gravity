import math
import random
import time
import numpy
from numpy import random as nrdm

def applygravity(points,g):
    truepoints = []
    for p1 in points:
        coor = p1[0:3]
        for p2 in points:
            if points.index(p1) != points.index(p2) and p1[3] != 0:
                birlesme = False
                fx = p1[0] - p2[0]
                fy = p1[1] - p2[1]
                fz = p1[2] - p2[2]
                d = int(round(math.sqrt(fx**2 + fy**2 + fz**2)))

                if d <= (p1[3] ** (1. / 4.)):
                    xv = (p1[4] * p1[3] + p2[4] * p2[3]) / (p1[3] + p2[3])
                    yv = (p1[5] * p1[3] + p2[5] * p2[3]) / (p1[3] + p2[3])
                    zv = (p1[6] * p1[3] + p2[6] * p2[3]) / (p1[3] + p2[3])  # Momentum korunumu
                    p1[4], p1[5], p1[6] = xv, yv, zv
                    p1[3] += p2[3]  # Yıldız birleştirme
                    p2[3] = 0

                else:
                    ap = (g * p2[3]) / d ** 2

                    x = fx / d
                    y = fy / d
                    z = fz / d

                    xn = coor[0] + x*ap - p1[4]
                    p1[4] = (x * ap + p1[4])
                    yn = coor[1] + y * ap - p1[5]
                    p1[5] = (y * ap + p1[5])
                    zn = coor[2] + z * ap - p1[6]
                    p1[6] = (z * ap + p1[6])
                    coor =[ xn , yn , zn ]
        if p1[3] > 0:
            truepoints.append(coor[0:3] + p1[3:8])

    #print(truepoints[0][3:7])
    return truepoints


def rotater(x,y,alpha):
    rx = x * math.cos(alpha) - y * math.sin(alpha)  ##  rot
    ry = x * math.sin(alpha) + y*math.cos(alpha)
    return (rx,ry)

def disteq(x):
    return 4*(math.exp(x))/((1 + math.exp(x))**2)

def Unigenerator(list,number,unisize,mode):
    nf = True
    i = 0
    if mode == "galaxy":
        while nf:
            i += 1
            p = [random.randint(-unisize,unisize),random.randint(-unisize,unisize),random.randint(-unisize,unisize)
                ,random.randint(27,1000),0,0,0,[random.randint(200,256),random.randint(200,256),random.randint(200,256)]]
            v = math.sqrt(p[0]**2 + 50*p[1]**2 + p[2]**2)
            q = math.sqrt(p[0]**2 + p[1]**2 + p[2]**2)
            if random.randint(0,20000) < disteq(8*(v/unisize))*10000-2:
                list.append(p)
            if random.randint(0,10000) < disteq(22*(q/unisize))*10000-1:
                if q < unisize/20:
                    p[3] *= 3
                    list.append(p)
                elif q < unisize/12:
                    p[3] *= 2
                    list.append(p)
                else:
                    list.append(p)
            if len(list) >= number:
                nf = False
        list.append([0,0,0,27000,0,0,0,(255,255,255)])
        print(i)
        return list
    elif mode == "normal":
        for i in range(number):
            p = [random.randint(-unisize, unisize), random.randint(-unisize, unisize), random.randint(-unisize, unisize)
                ,random.randint(27,1000),0,0,0,[random.randint(150,256),random.randint(150,256),random.randint(150,256)]]
            list.append(p)
        print(".")
        return list






    ##Sphere





class Person:
    def __init__(self, coordinates, rotation, view, windowsize):  # 3 elemanlı 2 list alıyor
        self.pos = coordinates
        self.rot = rotation
        self.posx = coordinates[0]
        self.posy = coordinates[1]
        self.posz = coordinates[2]
        self.rotx = (rotation[0]/180)*math.pi
        self.view = view * math.pi / 360
        self.roty = (rotation[1]/180)*math.pi
        self.wsize = windowsize  # gercek boyutun yarısı

    def viewcone(points):  # butun noktaların listesini alır
        seenpoints = []
        for p in points:                      ### x" = cx -sy  ;  y" = sx + cy
            distance = p[2] - Person.posz
            xdif = p[0] - Person.posx
            ydif = p[1] - Person.posy
            b = p[3] # boyut

            xy1 = rotater(xdif,distance,-Person.rotx)
            qy = rotater(xy1[1] , ydif ,-Person.roty)

            x = xy1[0]
            y = qy[1]
            d = qy[0]
            u = math.sqrt(x**2 + y**2 + d**2)

            pss = d * math.tan(Person.view)

            if (x < pss and y < pss) and (pss > 0):
                seenpoints.append([(x / pss) * Person.wsize , (y / pss) * Person.wsize,int(round(5*b/u)),p[7]])

        return seenpoints

class Cube:
    def __init__(self,points):
        Cube.points = points






#Person.__init__(Person,[0,0,5],[90,90,0],90,5)

#print(Person.viewcone([[1,1,4,1],[1,1,3,2],[2,3,1,10],[-3,4,-3,5]]))

"""if abs(x) > 0.447:
        return 1/(43*x**4)
    elif abs(x) <= 0.447:"""

# dy1 = distance*math.cos(Person.rotx) - ydif*math.sin(Person.rotx) ##x rot
# y = distance*math.sin(Person.rotx) + ydif*math.cos(Person.rotx)

# dx1 = distance * math.cos(Person.roty) - xdif * math.sin(Person.roty)  ##y rot
# x = distance * math.sin(Person.roty) + xdif * math.cos(Person.roty)

# x = x1 * math.cos(Person.rotz) - y1 * math.sin(Person.rotz)  ##z rot
# y = x1 * math.sin(Person.rotz) + y1 * math.cos(Person.rotz)

#ox = xy1[0] / math.sqrt(xy1[0]**2+xy1[1]**2)
#oz = xy1[1] / math.sqrt(xy1[0]**2+xy1[1]**2)


"""

                try:
                    ap = (g * p2[3]) / d ** 2
                except:
                    xv = (p1[4]*p1[3] + p2[4]*p2[3])/(p1[3]+p2[3])
                    yv = (p1[5] * p1[3] + p2[5] * p2[3]) / (p1[3] + p2[3])
                    zv = (p1[6] * p1[3] + p2[6] * p2[3]) / (p1[3] + p2[3]) # Momentum korunumu
                    p1[4], p1[5] , p1[6] = xv , yv ,zv
                    p1[3] += p2[3] # Yıldız birleştirme
                    p2[3] = 0
                    birlesme = True
    
"""