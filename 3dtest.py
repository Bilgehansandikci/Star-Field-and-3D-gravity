import pygame
import math
import random
import clases3d
from clases3d import Person as observer
from pygame import gfxdraw

  ####### INITIALIZATION ########

mod = input("fizik modu ('gravity','normal')>>> ")

slot = int(input("Kaydedilmiş evren yüklensin mi? ( 1 , 0 ) >>> "))

points = []
if slot == 1:
    savedfile = input("Dosya adı>>> ")
    ekrbyt = int(input("Ekran boyutu>>> "))
    acı = int(input("Görüş açısı (70,90)>>> "))
    hız = int(input("Hız girin(2)>>> "))
    stpoint = int(input("Başlama konum oranı(2,1,0)>>> "))
    sdoc = open(savedfile+".txt", "r")
    e = sdoc.read().split("eb")
    a = e[1].split(";")
    e = int(e[0])
    for i in range(len(a)):
        a[i] = a[i].strip("[").strip("]").split(",")
        for j in range(len(a[i])-1):
            a[i][j] = float(a[i][j])
            a[i][-1][1:-1] = a[i][-1].split("tp")
            for jk in  range(len(a[i][-1])):
                a[i][-1][jk] = int(a[i][-1][jk])
            a[-1] = tuple(a[-1])

    points = a
    sdoc.close()
elif slot == 0:
    ekrbyt = int(input("Ekran boyutu>>> "))
    acı = int(input("Görüş açıs (70,90)>>> "))
    hız = int(input("Hız girin(2)>>> "))
    stpoint = int(input("Başlama konum oranı(2,1,0)>>> "))
    e = int(input("Uzay boyutu girin( S:100 , M:300 , L:1.000 , XL:10.000 )>>> "))
    genmod = input("Mod('galaxy' ve ya 'normal')>>> ")
    numofpoints = int(input("Yıldız sayısı >>> "))
    points = clases3d.Unigenerator(points, numofpoints, e, genmod)

  ####### INITIALIZATION ########
#points = [[e,e,e,10,0,0,0,[255,255,255]],[-e,e,e,10,0,0,0,[255,255,255]],[e,-e,e,10,0,0,0,[255,255,255]],[-e,-e,e,10,0,0,0,[255,255,255]],[e,e,-e,10,0,0,0,[255,255,255]],[-e,e,-e,10,0,0,0,[255,255,255]],[e,-e,-e,10,0,0,0,[255,255,255]],[-e,-e,-e,10,0,0,0,[255,255,255]]]
win = pygame.display.set_mode((ekrbyt, ekrbyt))
observer.__init__(observer, [0,  0, -stpoint*e], [0, 0], acı, int(ekrbyt / 2))  # [x , y , z] ;  [yatay,dikey] ; gorus acısı
 ##[e,e,e],[-e,e,e],[e,-e,e],[-e,-e,e],[e,e,-e],[-e,e,-e],[e,-e,-e],[-e,-e,-e] köşeler
vrx,vry,vrz,h = 0,0,0,0
run = True
fr = 20 # frame delay
moddict = { "gravity" : clases3d.applygravity, "normal" : points }
print(".")

def noktaciz(info): # x ; y ; boyut
    try:
        #gfxdraw.pixel(win, round(cord[0]), round(cord[1]), (255, 255, 255))
        pygame.draw.circle(win,tuple(info[3]), (round(info[0]), round(info[1])), int(round(info[2])**(1./3.)))
    except:
        pass

while run:
    pygame.time.delay(fr)
    if mod == "gravity":
        points =  clases3d.applygravity(points,0.000005)
    elif mod == "normal":
        pass

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_UP:
                vry = -1
            if event.key == pygame.K_DOWN:
                vry = 1
            if event.key == pygame.K_RIGHT:
                vrx = -1
            if event.key == pygame.K_LEFT:
                vrx = 1
            if event.key == pygame.K_SPACE:
                h = hız
            if event.key == pygame.K_1:
                fr = 10
            if event.key == pygame.K_2:
                fr = 5
            if event.key == pygame.K_3:
                fr = 1
            if event.key == pygame.K_d:
                vrz = -1
            if event.key == pygame.K_a:
                vrz = 1
            if event.key == pygame.K_k:
                save = input("Kaydetmek istediginiz dosya ismi>>> ")
                f = open(save+".txt", "w")
                s = ""
                for i in points:
                    s += str(i[0:-1])+","+str(i[-1]).replace(",","tp",2)+";"
                s =str(e)+"eb"+s[0:-1]
                f.write(s)
                f.close

            if event.key == pygame.K_LSHIFT:
                h = hız*5
            if event.key == pygame.K_LCTRL:
                h = -hız*2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_1:
                fr = 20
            if event.key == pygame.K_2:
                fr = 20
            if event.key == pygame.K_3:
                fr = 20
            if event.key == pygame.K_UP:
                vry = 0
            if event.key == pygame.K_DOWN:
                vry = 0
            if event.key == pygame.K_RIGHT:
                vrx = 0
            if event.key == pygame.K_LEFT:
                vrx = 0
            if event.key == pygame.K_SPACE:
                h = 0
            if event.key == pygame.K_d:
                vrz = 0
            if event.key == pygame.K_a:
                vrz = 0
            if event.key == pygame.K_LSHIFT:
                h = 0
            if event.key == pygame.K_LCTRL:
                h = 0

    observer.rotx += 2*vrx * math.pi / 180
    observer.roty += 2*vry * math.pi / 180
    hx = math.cos(observer.roty)*-math.sin(observer.rotx)
    hy = math.sin(observer.roty)
    hz = math.cos(observer.rotx)*math.cos(observer.roty)
    observer.posx += hx * h
    observer.posy += hy * h
    observer.posz += hz * h
    seenpts = observer.viewcone(points)
    win.fill((0,0,0))
    for i in seenpts:
        l = list(map(lambda x: x + (ekrbyt / 2), i[0:2]))
        l.append(i[2])
        l.append(i[3])
        noktaciz(l)

    pygame.display.update()




pygame.quit()



"""for i in range(numofpoints):
    points.append([random.randint(-int(evrbyt / 2), int(evrbyt / 2)),
                   random.randint(-int(evrbyt / 2), int(evrbyt / 2)),
                   random.randint(-int(evrbyt / 2), int(evrbyt / 2))])
pygame.display.toggle_fullscreen()"""