#Field Runners
#Produced By 8.5 Class:)
#Imports
import pygame as p
import time as t
#Functions
#1
def aks(a,b,c,d):
    a=p.image.load(b)
    a=p.transform.smoothscale(a,(int(c),int(d)))
    return a
#2
def menu(a,b,sound):
    b=b*890/900
    x=aks('x','load.png',a,b)
    music=p.mixer.Sound('sounds\\01 Fieldrunners Theme Song.ogg')
    tmusic=0
    t0=t.time()
    while True:
        for event in p.event.get():
            if event.type==p.QUIT:
                music.stop()
                return 0
            if event.type==p.MOUSEBUTTONDOWN and event.button==1:
                    sound.play()
                    t.sleep(sound.get_length())
                    music.stop()
                    t.sleep(0.3)
                    return 1
        # updates
        t1=t.time()
        dt=t1-t0
        t0=t1
        tmusic=tmusic-dt
        if tmusic<0:
            music.play()
            tmusic=music.get_length()
        # draws
        sc.fill((0,0,0))
        sc.blit(x,(0,0))
        p.display.update()
#3
def field(a,b,n):
    c=16/9*b/a
    tool_zel=int(a*((tanh(c)*c*tanh(1/c)))**0.5)//16
    x=100*a//tool_zel
    y=100*b//tool_zel
    pic=p.image.load('gnds\\'+str(n)+'.png')
    print('ground image number '+str(n)+' has loaded successfully')
    a2,b2=pic.get_size()
    pic=crop(pic,((a2-x)//2,(b2-y)//2,x,y))
    print('ground image number '+str(n)+' has cropped successfully')
    pic=p.transform.smoothscale(pic,(a,b))
    return [(a-16*tool_zel)//2, (b-9*tool_zel)//2, tool_zel, pic]
#4
def manategh():
    a=int(input('enter screen width: '))
    b=int(input('enter screen height: '))
    areas=emptymatrix((9,16,4))
    [x0,y0,tool_zel,pic]=field(a,b,0)
    for i in range(9):
        for j in range(16):
            areas[i][j]=[x0+tool_zel*j,
                         y0+tool_zel*i,
                         tool_zel,
                         'tookhali']
    return (a,b),pic,areas
#5
def ghadr(n):
    if n<0:
        n=-n
    return n
#6
def upgrade_guns(areas,budjet,cost_upgrade_guns,event,gun_for_upgrade,guns,mine_areas,sell_profit_guns,sell_profit_upgrade_guns,zaman):
    if event.type==p.MOUSEBUTTONDOWN and event.button==1:
        x,y=event.pos
        if gun_for_upgrade!=-1:
            g=guns[gun_for_upgrade]
            if x>=g[1]-0.10885*a and x<g[1]+(-0.10885+3/35)*a and y>=g[2]-0.05027*b and y<g[2]+0.05027*b:
                budjet=budjet+sell_profit_guns[g[0]-1]+(g[5]-1)*sell_profit_upgrade_guns[g[0]-1]
                j=0
                while j<len(zaman):
                    if zaman[j][0]==gun_for_upgrade:
                        zaman.pop(j)
                        j=j-1
                    elif zaman[j][0]>gun_for_upgrade:
                        zaman[j][0]=zaman[j][0]-1
                    j=j+1
                areas[g[4]][g[3]][3]='tookhali'
                mine_areas[g[4]][g[3]]=False
                guns.pop(gun_for_upgrade)
            elif x>=g[1]+0.03215*a and x<g[1]+(0.03215+3/35)*a and y>=g[2]-0.05027*b and y<g[2]+0.05027*b:
                if g[5]<3 and budjet>=cost_upgrade_guns[g[0]-1]:
                    budjet-=cost_upgrade_guns[g[0]-1]
                    g[5]=g[5]+1
            gun_for_upgrade=-1
        else:
            for i in range(len(guns)):
                area=areas[guns[i][4]][guns[i][3]]
                if x>=area[0] and x<area[0]+area[2] and y>=area[1] and y<area[1]+area[2]:
                    gun_for_upgrade=i
    return budjet,gun_for_upgrade
#7
def draw_gun_for_upgrade(sc,areas,gun_for_upgrade,guns,icon_sell,icon_upgrade,icon_upgrade_disablded):
    if gun_for_upgrade!=-1:
        g=guns[gun_for_upgrade]
        if g[0]==5:
            rect=p.transform.scale(green_rect,(a,areas[g[4]][g[3]][2]))
            sc.blit(rect,(0,areas[g[4]][g[3]][1]))
            rect=p.transform.scale(green_rect,(areas[g[4]][g[3]][2],areas[g[4]][g[3]][1]))
            sc.blit(rect,(areas[g[4]][g[3]][0],0))
            rect=p.transform.scale(green_rect,(areas[g[4]][g[3]][2],b-areas[g[4]][g[3]][1]-areas[g[4]][g[3]][2]))
            sc.blit(rect,(areas[g[4]][g[3]][0],areas[g[4]][g[3]][1]+areas[g[4]][g[3]][2]))
        else:
            if g[0]==6:
                radius=(g[5]*3)**0.5*areas[0][0][2]
            else:
                radius=10**0.5*areas[0][0][2]
            circle=p.transform.scale(green_circle,(int(2*radius),int(2*radius)))
            sc.blit(circle,(g[1]-radius,g[2]-radius))
        sc.blit(icon_sell,(g[1]-0.10885*a,g[2]-0.05027*b))
        text=littlefont.render('$'+str(sell_profit_guns[g[0]-1]+(g[5]-1)*sell_profit_upgrade_guns[g[0]-1]),True,(0,0,0))
        sc.blit(text,((g[1]+(246/4655-0.10885)*a-text.get_width()/2,g[2]+0.02*b)))
        if g[5]<3 and budjet>=cost_upgrade_guns[g[0]-1]:
            sc.blit(icon_upgrade,(g[1]+0.03215*a,g[2]-0.05027*b))
        else:
            sc.blit(icon_upgrade_disabled,(g[1]+0.03215*a,g[2]-0.05027*b))
        if g[5]<3:
            text=littlefont.render('$'+str(cost_upgrade_guns[g[0]-1]),True,(0,0,0))
        else:
            text=littlefont.render('max',True,(0,0,0))
        sc.blit(text,((guns[gun_for_upgrade][1]+(246/4655+0.03215)*a-text.get_width()/2,guns[gun_for_upgrade][2]+0.02*b)))
    return
#8
def menu_guns(a,b,cost_guns,budjet,areas):
    for i in range(6):
        text=littlefont.render('$'+str(cost_guns[i]),True,(0,0,0))
        atext,btext=text.get_size()
        if budjet>=cost_guns[i]:
            sc.blit(gunpics[i][3],(int((0.95-(5-i)*0.0725-3/70)*a),int(0.89973*b)))
        else:
            sc.blit(gunpics[i][4],(int((0.95-(5-i)*0.0725-3/70)*a),int(0.89973*b)))
        sc.blit(text,(int((0.95-(5-i)*0.0725+93/9310)*a-atext/2),int(0.97*b)))
    return
#9
def buy_guns(areas,event,drag,dt,guns,sound_invalid,sound_tower_place2,sound_UI_button,budjet,cost_guns,soldiers):
    f=False
    if event.type==p.MOUSEBUTTONDOWN and event.button==1:
        drag[1],drag[2]=event.pos
        for i in range(6):
            if drag[1]>=(0.95-(5-i)*0.0725-3/70)*a and drag[1]<(0.95-(4-i)*0.0725-3/70)*a and drag[2]>=0.89973*b:
                if budjet>=cost_guns[i]:
                    drag[0]=i+1
                    sound_UI_button.play()
    elif event.type==p.MOUSEBUTTONUP and event.button==1 and drag[0]!=0:
        drag[1],drag[2]=event.pos
        drag[3]=(drag[1]-areas[0][0][0])//areas[0][0][2]
        drag[4]=(drag[2]-areas[0][0][1])//areas[0][0][2]
        if drag[3]>=0 and drag[3]<16 and drag[4]>=0 and drag[4]<9:
            if areas[drag[4]][drag[3]][3][0]=='t' and (not mine_areas[drag[4]][drag[3]]):
                f=True
                for s in soldiers:
                    if s[3]==drag[3] and s[4]==drag[4]:
                        f=False
                if f or drag[0]==6:
                    if drag[0]!=6:
                        areas[drag[4]][drag[3]][3]='por'
                    else:
                        mine_areas[drag[4]][drag[3]]=True
                    waze=waze_v(areas)
                    if waze[4][0]==0:
                        areas[drag[4]][drag[3]][3]='tookhali'
                        waze=waze_v(areas)
                        f=False
                    else:
                        #(نوع,x,y,xa,ya,level,zavie,hadaf,True/False)
                        guns.append([drag[0],(drag[3]+0.5)*areas[0][0][2]+areas[0][0][0],(drag[4]+0.5)*areas[0][0][2]+areas[0][0][1]
                                    ,drag[3],drag[4],1,90,-1,drag[0]!=6])
                        sound_tower_place2.play()
                        guns[-1][7]=choose_soldier(guns[-1],areas,dt,soldiers)
                        budjet=budjet-cost_guns[drag[0]-1]
                        drag[0]=0
        if not f:
            drag[0]=0
            sound_invalid.play()
    elif event.type==p.MOUSEMOTION:
        drag[1],drag[2]=event.pos
        drag[3]=(drag[1]-areas[0][0][0])//areas[0][0][2]
        drag[4]=(drag[2]-areas[0][0][1])//areas[0][0][2]
    elif event.type==p.KEYDOWN:
        if event.key>48 and event.key<55:
            if budjet>=cost_guns[event.key-49]:
                drag[0]=event.key-48
            sound_UI_button.play()
        if event.key>256 and event.key<263:
            if budjet>=cost_guns[event.key-257]:
                drag[0]=event.key-256
            sound_UI_button.play()
    return f,budjet
#10
def budjet_joon(a,b,budjet,scr,soldiers,joon_karbar):
    i=0
    while i<len(soldiers):
        if soldiers[i][7]<0:
            soldier_id=int(soldiers[i][0][1:])
            budjet=budjet+(1,2,1,2,1,2,10,20)[soldier_id-1]
            scr=scr+(50,75,125,350,175,300,500,2000)[soldier_id-1]
            for g in guns:
                if g[0]!=6:
                    if g[7]==i:
                        g[7]=-1
                    elif g[7]>i:
                        g[7]=g[7]-1
            for t in tirha:
                if t[5]==i:
                    t[5]=-1
                elif t[5]>i:
                    t[5]=t[5]-1
            soldiers.pop(i)
        elif soldiers[i][1]>a-25:
            for g in guns:
                if g[0]!=6:
                    if g[7]==i:
                        g[7]=-1
                    elif g[7]>i:
                        g[7]=g[7]-1
            for t in tirha:
                if t[5]==i:
                    t[5]=-1
                elif t[5]>i:
                    t[5]=t[5]-1
            soldiers.pop(i)
            joon_karbar=joon_karbar-1
        else:
            i=i+1
    return budjet,joon_karbar,scr
#11
def emptymatrix(D,val=0):
    if len(D)==1:
        return D[0]*[0]
    A=[]
    for i in range(D[0]):
        A.append(emptymatrix(D[1:],val))
    return A
#12
def waze_v(areas):
    waze=emptymatrix((9,16))
    A=[]
    if areas[4][15][3][0]=='t':
        waze[4][15]=1
        A=[(4,15)]
    i=1
    while A!=[]:
        i=i+1
        for j in range(len(A)):
            for k,l in [(-1,0),(0,-1),(0,1),(1,0)]:
                if 0<=A[j][0]+k<9 and 0<=A[j][1]+l<16:
                    if areas[A[j][0]+k][A[j][1]+l][3][0]=='t' and waze[A[j][0]+k][A[j][1]+l]==0:
                        waze[A[j][0]+k][A[j][1]+l]=i
                        A.append((A[j][0]+k,A[j][1]+l))
        for k in range(j+1):
            A.pop(0)
    return waze
#13
def update(dt,fixdistance,soldiers,sorat_soldiers,waze,x0,y0,a,b,flag=False):
    m=max(sorat_soldiers)
    while fixdistance*m>=a/2:
        update(dt,a/4/m,soldiers,sorat_soldiers,waze,x0,y0,a,b,flag)
        fixdistance=fixdistance-a/4/m
    for s in soldiers:
        x=s[1]
        y=s[2]
        xa=s[3]
        ya=s[4]
        i=s[5]# جهت حرکت
        distance=sorat_soldiers[int(s[0][1])-1]*fixdistance
        distance2=0
        if type(xa)==str:
            x=x+distance
            y=y0+4.5*a
            if xa=='en' and x>=x0:
                xa=0
                ya=4
                xia=x-b
                yia=a/2
        else:
            xia=x-a*xa-x0# x in area
            yia=y-a*ya-y0# y in area
            if flag and not(ya==4 and xa==15):
                if i=='r' and xia*2>=a and(waze[ya][xa+1]==0 or waze[ya][xa+1]>=waze[ya][xa]):
                    i='l'
                elif i=='u' and yia*2<a and(waze[ya-1][xa]==0 or waze[ya-1][xa]>=waze[ya][xa]):
                    i='d'
                elif i=='d' and yia*2>=a and(waze[ya+1][xa]==0 or waze[ya+1][xa]>=waze[ya][xa]):
                    i='u'
                elif i=='l' and xia*2<a and(waze[ya][xa-1]==0 or waze[ya][xa-1]>=waze[ya][xa]):
                    i='r'
            if i=='r':
                xia2=xia+distance
                if xia*2<a and xia2*2>=a:
                    distance2=xia2-a/2
                    xia2=a/2
                    m=waze[ya][xa]
                    for i2,j,k in[('l',0,-1),('d',1,0),('u',-1,0),('r',0,1)]:
                        if (0<=ya+j<9 and 0<=xa+k<16) and (0!=waze[ya+j][xa+k]<=m):
                            i=i2
                            m=waze[ya+j][xa+k]
                    if ya==4 and xa==15:
                        i='r'
                if xia2>a:
                    xa=xa+1
                    xia2=xia2-a
                x=x0+a*xa+xia2
            elif i=='u':# don't use "if" instead "elif"
                yia2=yia-distance
                if yia*2>=a and yia2*2<a:
                    distance2=a/2-yia2
                    yia2=a/2
                    m=waze[ya][xa]
                    for i2,j,k in[('l',0,-1),('d',1,0),('u',-1,0),('r',0,1)]:
                        if (0<=ya+j<9 and 0<=xa+k<16) and (0!=waze[ya+j][xa+k]<=m):
                            i=i2
                            m=waze[ya+j][xa+k]
                    if ya==4 and xa==15:
                        i='r'
                if yia2<0:
                    ya=ya-1
                    yia2=yia2+a
                y=y0+a*ya+yia2
            elif i=='d':# don't use "if" instead "elif"
                yia2=yia+distance
                if yia*2<a and yia2*2>=a:
                    distance2=yia2-a/2
                    yia2=a/2
                    m=waze[ya][xa]
                    for i2,j,k in[('l',0,-1),('d',1,0),('u',-1,0),('r',0,1)]:
                        if (0<=ya+j<9 and 0<=xa+k<16) and (0!=waze[ya+j][xa+k]<=m):
                            i=i2
                            m=waze[ya+j][xa+k]
                    if ya==4 and xa==15:
                        i='r'
                if yia2>a:
                    ya=ya+1
                    yia2=yia2-a
                y=y0+a*ya+yia2
            else:
                xia2=xia-distance
                if xia*2>=a and xia2*2<a:
                    distance2=a/2-xia2
                    xia2=a/2
                    m=waze[ya][xa]
                    for i2,j,k in[('l',0,-1),('d',1,0),('u',-1,0),('r',0,1)]:
                        if (0<=ya+j<9 and 0<=xa+k<16) and (0!=waze[ya+j][xa+k]<=m):
                            i=i2
                            m=waze[ya+j][xa+k]
                    if ya==4 and xa==15:
                        i='r'
                if xia2<0:
                    xa=xa-1
                    xia2=xia2+a
                x=x0+a*xa+xia2
            if i=='r':
                x=x+distance2
            elif i=='u':
                y=y-distance2
            elif i=='d':
                y=y+distance2
            elif i=='l':
                x=x-distance2
            if x>x0+16*a:
                xa='ex'
                ya='ex'
        s[1]=x
        s[2]=y
        s[3]=xa
        s[4]=ya
        s[5]=i
        # فاصله از مقصد
        if not flag:
            s[8]=s[8]-distance
        elif type(xa)==str:
            if xa=='en':
                s[8]=a*waze[4][0]+(x0-x)+b
            else:
                s[8]=b+(x0+16*a)-x
        elif i=='r':
            s[8]=a*waze[ya][xa]-xia+b
        elif i=='u':
            s[8]=a*waze[ya][xa]+yia+b-a
        elif i=='d':
            s[8]=a*waze[ya][xa]-yia+b
        else:
            s[8]=a*waze[ya][xa]+xia+b-a
        s[9]=s[9]-dt
    return soldiers
#14
def sinh(x):
    e=2.718281828459045
    return(e**x-e**(-x))/2
#15
def cosh(x):
    e=2.718281828459045
    return(e**x+e**(-x))/2
#16
def tanh(x):
    return sinh(x)/cosh(x)
#17
def crop(img,rect):
    img2=p.Surface((rect[2],rect[3]))
    for i in range(rect[3]):
        for j in range(rect[2]):
            c=img.get_at((j+rect[0],i+rect[1]))
            img2.set_at((j,i),c)
    return img2
#18
def black_and_white(img):
    x,y=img.get_size()
    img2=p.Surface((x,y))
    for i in range(y):
        for j in range(x):
            r,g,b,t=img.get_at((j,i))
            brightness=(r+g+b)/3
            img2.set_at((j,i),(brightness,brightness,brightness,t))
    return img2
#19
def load_gunpics(a,b,areas):
    gunpics=[]
    aicon=int(3/35*a)
    bicon=int(0.10054*b)
    a2=areas[0][0][2]
    for i in range(6):
        gunpics.append([0]*5)
        pic=p.image.load('guns\g'+str(i+1)+' level-3.png')
        gunpics[i][2]=p.transform.smoothscale(pic,(a2,a2))
        pic=p.image.load('guns\g'+str(i+1)+' level-2.png')
        gunpics[i][1]=p.transform.smoothscale(pic,(a2,a2))
        pic=p.image.load('guns\g'+str(i+1)+' level-1.png')
        gunpics[i][0]=p.transform.smoothscale(pic,(a2,a2))
        pic=p.image.load('guns\g'+str(i+1)+' icon.png')
        gunpics[i][3]=p.transform.smoothscale(pic,(aicon,bicon))
        gunpics[i][4]=black_and_white(gunpics[i][3])
    return gunpics
#20
def enter1(trtes,dt,b,areas,entrance,joon_soldiers,soldiers,_round):
    if soldiers==[]:
        trtes=trtes-dt
    if trtes<0 and soldiers==[]:
        trtes=0
        _round=_round+1
        if _round<=100:
            s=entrance.readline()
            typ=s[:2]
            n=int(s[3:5])
            for i in range(n):
                soldiers.append([typ,-i*a/4/(_round**0.5),b/2,'en','en','r',joon_soldiers[int(s[1])-1]*_round**0.5,0,0,0])
                soldiers[i][7]=soldiers[i][6]
                soldiers[i][8]=areas[0][0][2]*waze[4][0]+2*areas[0][0][0]
                trtes=2
        else:
            entrance.close()
    return trtes,soldiers,_round
#21
def draw_guns(sc,guns,gunpics):
    for g in guns:
        #(نوع,x,y,xa,ya,level,zavie,hadaf/time_remaining_to_explode,True/False)
        gunpic=gunpics[g[0]-1][g[5]-1]
        if g[0]!=6:
            gunpic=p.transform.rotate(gunpic,g[6]-90)
        x,y=gunpic.get_size()
        sc.blit(gunpic,(g[1]-x/2,g[2]-y/2))
    return
#22
def choose_soldier(gun,areas,dt,soldiers):
    if gun[0]==5:
        fasele_ta_maghsad=1000*a
        n=-1
        for i in range(len(soldiers)):
            s=soldiers[i]
            if(gun[4]==4 and type(s[4])==str and s[1]>=0) or gun[3]==s[3] or gun[4]==s[4]:
                if s[8]<fasele_ta_maghsad:
                    n=i
                    fasele_ta_maghsad=s[8]
    elif gun[0]==6:
        i=0
        n=gun[7]
        while not f and i<len(soldiers):
            s=soldiers[i]
            if(s[1]-gun[1])**2+(s[2]-gun[2])**2<=3*areas[0][0][2]**2:
                gun[8]=True
            i=i+1
        if gun[8]:
            n=n-dt
        else:
            n=1.5
    else:
        fasele_ta_maghsad=1000*a
        n=-1
        for i in range(len(soldiers)):
            s=soldiers[i]
            if(s[1]-gun[1])**2+(s[2]-gun[2])**2<=10*areas[0][0][2]**2:
                if s[8]<fasele_ta_maghsad:
                    if prediction(areas,gun,s,sorat_soldiers) is not None:
                        n=i
                        fasele_ta_maghsad=s[8]
    return n
#23
def angle_gun(areas,guns,soldiers):
    for g in guns:
        if g[0]==5:
            if g[7]!=-1:
                s=soldiers[g[7]]
                xas=s[3]#xa of soldier
                yas=s[4]#ya of soldier
                if type(xas)==str:
                    yas=4
                    if xas=='en':
                        xas=-1
                    else:
                        xas=16
                if xas>g[3]:
                    g[6]=0
                elif yas>g[4]:
                    g[6]=-90
                elif xas<g[3]:
                    g[6]=180
                else:
                    g[6]=90
        elif g[0]==6:
            g[6]=90
        else:
            if g[7]!=-1:
                s=soldiers[g[7]]
                p=prediction(areas,g,s,sorat_soldiers)
                if p is not None:
                    if p[0]>g[1]:
                        ang=atan((g[2]-p[1])/(p[0]-g[1]))
                    elif g[2]>p[1]:
                        ang=atan((g[1]-p[0])/(g[2]-p[1]))+pi/2
                    elif g[2]==p[1]:
                        ang=pi
                    else:
                        ang=-atan((p[0]-g[1])/(g[2]-p[1]))-pi/2
                    g[6]=ang*180/pi
    return
#24
def tarakom(soldiers):
    x=len(soldiers)*[0]
    for i in range(len(x)):
        x[i]=(soldiers[i][1],soldiers[i][2])
    for i in range(len(x)):
        for j in range(len(x)):
            print(i)
            if x[j][1]==x[i][1] and soldiers[i][5]!=False:
                soldiers[i][5]=False
            elif x[j][2]==x[i][2] and soldiers[i][5]!=False:
                soldiers[i][5]=False
    return soldiers
#25
def bordar(a,b):
    t=(a**2+b**2)**0.5
    a=a/t
    b=b/t
    return a,b
#26
def tir(a,b,areas,dt,gun_for_upgrade,guns,sc,soldiers,sound_explosion_large_01,tirha,zaman):
    #new
    i=0
    while i<len(guns):
        guns[i][7]=choose_soldier(guns[i],areas,dt,soldiers)
        if guns[i][0]==4:
            if guns[i][7]!=-1:
                soldiers[guns[i][7]][7]-=2*dt
                soldiers[guns[i][7]][9]=2
            i=i+1
        elif guns[i][0]==5:
            if guns[i][8]:
                if guns[i][7]!=-1:
                    ntir=[]
                    ntir.append(guns[i][0])
                    ntir.append(guns[i][1])
                    ntir.append(guns[i][2])
                    s=soldiers[guns[i][7]]
                    xas=s[3]#xa of soldier
                    yas=s[4]#ya of soldier
                    if type(xas)==str:
                        yas=4
                        if xas=='en':
                            xas=-1
                        else:
                            xas=16
                    if xas>guns[i][3]:
                        ntir.append(1)
                        ntir.append(0)
                    elif yas>guns[i][4]:
                        ntir.append(0)
                        ntir.append(1)
                    elif xas<guns[i][3]:
                        ntir.append(-1)
                        ntir.append(0)
                    else:
                        ntir.append(0)
                        ntir.append(-1)
                    ntir[1]=ntir[1]+ntir[3]*areas[0][0][2]/2
                    ntir[2]=ntir[2]+ntir[4]*areas[0][0][2]/2
                    ntir.append(guns[i][7])
                    ntir.append(guns[i][5])
                    tirha.append(ntir)
                    nzaman=[]
                    nzaman.append(i)
                    nzaman.append(0.1)
                    zaman.append(nzaman)
                    guns[i][8]=False
            i=i+1
        elif guns[i][0]==6:
            if guns[i][7]<=0:
                j=0
                for j in range(len(soldiers)):
                    s=soldiers[j]
                    if(s[1]-guns[i][1])**2+(s[2]-guns[i][2])**2<=3*areas[0][0][2]**2*guns[i][5]:
                        soldiers[j][7]=-10
                mine_areas[guns[i][4]][guns[i][3]]=False
                j=0
                while j<len(zaman):
                    if zaman[j][0]==i:
                        zaman.pop(i)
                        j=j-1
                    elif zaman[j][0]>i:
                        zaman[j][0]=zaman[j][0]-1
                    j=j+1
                if gun_for_upgrade>i:
                    gun_for_upgrade=gun_for_upgrade-1
                elif gun_for_upgrade==i:
                    gun_for_upgrade=-1
                guns.pop(i)
                i=i-1
                sound_explosion_large_01.play()
            i=i+1
        else:
            if guns[i][8]:
                if guns[i][7]!=-1:
                    ntir=[]
                    ntir.append(guns[i][0])
                    ntir.append(guns[i][1])
                    ntir.append(guns[i][2])
                    s=soldiers[guns[i][7]]
                    predict=prediction(areas,guns[i],s,sorat_soldiers)
                    if predict is not None:
                        itir,jtir=bordar(predict[0]-guns[i][1],predict[1]-guns[i][2])
                        ntir.append(itir)
                        ntir.append(jtir)
                        ntir[1]=ntir[1]+itir*areas[0][0][2]/2
                        ntir[2]=ntir[2]+jtir*areas[0][0][2]/2
                        ntir.append(guns[i][7])
                        ntir.append(guns[i][5])
                        tirha.append(ntir)
                        nzaman=[]
                        nzaman.append(i)
                        nzaman.append(1)
                        zaman.append(nzaman)
                        guns[i][8]=False
            i=i+1
    i=0
    while i<len(zaman):
        if zaman[i][1]<0:
            guns[zaman[i][0]][8]=True
            zaman.pop(i)
        else:
            zaman[i][1]=zaman[i][1]-dt
            i=i+1
    #old
    i=0
    while i<len(tirha):
        if tirha[i][1]>=0 and tirha[i][1]<a and tirha[i][2]>=areas[0][0][1] and tirha[i][2]<b-areas[0][0][1]:
            tirha[i][1]+=100*tirha[i][3]*dt
            tirha[i][2]+=100*tirha[i][4]*dt
            i=i+1
        else:
            tirha.pop(i)
    return gun_for_upgrade
#27
def reduce_joon_soldiers(soldiers,tirha):
    i=0
    while i<len(tirha):
        j=0
        b=False
        while j<len(soldiers) and not b:
            if ((tirha[i][1]-soldiers[j][1])**2+(tirha[i][2]-soldiers[j][2])**2)**0.5<10:
                soldiers[j][7]-=damage_guns[tirha[i][0]-1]*tirha[i][6]
                soldiers[j][9]=2
                tirha.pop(i)
                b=True
            else:
                j=j+1
        if not b:
            i=i+1
    return soldiers,tirha
#28
def prediction(areas,gun,soldier,sorat_soldiers):
    v=5/sorat_soldiers[int(soldier[0][1])-1]
    if soldier[5]=='r':
        a=gun[1]-soldier[1]
        h=soldier[2]-gun[2]
    elif soldier[5]=='u':
        a=soldier[2]-gun[2]
        h=soldier[1]-gun[1]
    elif soldier[5]=='d':
        a=gun[2]-soldier[2]
        h=gun[1]-soldier[1]
    else:
        a=soldier[1]-gun[1]
        h=gun[2]-soldier[2]
    a=a+areas[0][0][2]/2/v
    d=a*v
    e=v**2-1#a
    f=2*d*v#b
    g=d**2-h**2#c
    # solution
    delta=f**2-4*e*g
    if delta<0:
        return None
    root1=(-f-delta**0.5)/2/e
    root2=(-f+delta**0.5)/2/e
    # choose better solution
    if root1>root2:
        b=root1
        root1=root2
        root2=b
    if a+root1>=0:
        b=root1
    elif a+root2>=0:
        b=root2
    else:
        return None
    # find the point
    if soldier[5]=='r':
        x=gun[1]+b
        y=soldier[2]
    elif soldier[5]=='u':
        x=soldier[1]
        y=gun[2]-b
    elif soldier[5]=='d':
        x=soldier[1]
        y=gun[2]+b
    else:
        x=gun[1]-b
        y=soldier[2]
    return(x,y)
# areas
# areas[i][j]=(x_noghte_bala_samt_chap,y_noghte_bala_samt_chap,tool_zel,por/tookhali)
(a,b),gndpic,areas=manategh()
mine_areas=emptymatrix((9,16),False)
gunpics=load_gunpics(a,b,areas)
#sources
p.init()
a1=16
b1=9
sc=p.display.set_mode((a,b))
p.display.set_caption('Field runners')
p.display.set_icon(p.image.load('icon.ico'))
import pygetwindow
for i in pygetwindow.getWindowsWithTitle('field runners'):
    if i.title=='Field runners':
        i.moveTo(-8,0)
font=p.font.Font('ltunivers-720-condheavy.ttf',35)
littlefont=p.font.Font('ltunivers-720-condheavy.ttf',b//40)
# math
pi=3.14159265358979323846
from math import atan
#soldiers
soldiers=[]
#soldiers[i]=(نوع,x,y,xa,ya,jahat,joon,joon_baghi_mande,fasele_ta_maghsad,5-modat zamane gozashte pas az akharin tir)
anvas=('s1','s2','s3','s4','s5','s6')# types of soldiers
joon_soldiers=(3,5,7,9,11,13,25,70)
sorat_soldiers=(2,4,6,8,10,12,1,1)
color_soldiers=((255,255,0)# خورشيد تابان
                ,(255,165,0)# خورشيدي که چيز هاي جديدي هم بلد است
                ,(0,128,0)# سرسبز و با طراوت
                ,(0,0,255)# کشف دريا ها و سرزمين هاي جديد
                ,(128,0,128)# 
                ,(165,42,42)# کوهي استوار
                ,(83,21,21)#
                ,(0,0,0))# رنگ سياه ترکيب همه ي رنگ هاست و اين سرباز همه کاري بلد است
#guns
guns=[]
#guns[i]=(نوع,x,y,xa,ya,level,zavie,hadaf,True/False)
anvag=('g1','g2','g3','g4','g5','g6')
damage_guns=(1,3,3,'ليزر',15,'مين')
cost_guns=(2,3,4,5,6,7)
cost_upgrade_guns=(1,2,3,4,5,8)
sell_profit_guns=(1,2,3,4,5,6)
sell_profit_upgrade_guns=(1,1,2,3,4,6)
#tirha
tirha=[]
#tirha[i]=(نوع,x,y,i,j,hadaf,level)
anvat=('t1','t2','t3','t4','t5','t6')# types of arrows
#zaman
zaman=[]
#zaman[i]=(شماره سلاح در ليست,time left from last tir)
#karbar
audio=True
budjet=5
budjet_img=p.image.load('UserInterface\hud_money.png')
budjet_img=p.transform.scale(budjet_img,(int(0.0625*a),int(0.08333*b)))
drag=[0,0,0,0,0,False]# type of gun, x, y, xa, ya, posiblity of placing
dt=0
entrance=open('entrance.asc','r')
ffwd=False
ffwd_img=p.image.load('UserInterface\hud_fast_forward.png')
ffwd_img=p.transform.scale(ffwd_img,(int(0.0625*a),int(0.0833*b)))
ffwd_disabled_img=p.image.load('UserInterface\hud_fast_forward_disabled.png')
ffwd_disabled_img=p.transform.scale(ffwd_disabled_img,(int(0.0625*a),int(0.0833*b)))
green_circle=p.image.load('green_circle.png')
green_rect=p.image.load('green_rect.png')
gun_for_upgrade=-1
hud_audio_off=p.image.load('UserInterface\hud_audio_off.png')
hud_audio_off=p.transform.scale(hud_audio_off,(int(0.0625*a),int(0.0833*b)))
hud_audio_on=p.image.load('UserInterface\hud_audio_on.png')
hud_audio_on=p.transform.scale(hud_audio_on,(int(0.0625*a),int(0.0833*b)))
hud_pause=p.image.load('UserInterface\hud_pause.png')
hud_pause=p.transform.scale(hud_pause,(int(0.0625*a),int(0.0833*b)))
hud_play=p.image.load('UserInterface\hud_play.png')
hud_play=p.transform.scale(hud_play,(int(0.0625*a),int(0.0833*b)))
icon_sell=p.image.load('UserInterface\icon_sell.png')
icon_sell=p.transform.scale(icon_sell,(int(3/35*a),int(0.10054*b)))
icon_upgrade=p.image.load('UserInterface\icon_upgrade.png')
icon_upgrade=p.transform.scale(icon_upgrade,(int(3/35*a),int(0.10054*b)))
icon_upgrade_disabled=p.image.load('UserInterface\icon_upgrade_disabled.png')
icon_upgrade_disabled=p.transform.scale(icon_upgrade_disabled,(int(3/35*a),int(0.10054*b)))
is_waze_changing=True
joon_img=p.image.load('UserInterface\hud_health.png')
joon_img=p.transform.scale(joon_img,(int(0.0625*a),int(0.08333*b)))
joon_karbar=20
pause=False
red_circle=p.image.load('red_circle.png')
red_rect=p.image.load('red_rect.png')
_round=0
scr=0
sound_explosion_large_01=p.mixer.Sound('sounds\explosion_large_01.wav')
sound_invalid=p.mixer.Sound('sounds\invalid.wav')
sound_tower_place2=p.mixer.Sound('sounds\\tower_place2.wav')
sound_UI_button=p.mixer.Sound('sounds\\UI_button.wav')
time_remaining_to_enter_soldier=10
#perform
print('click to exit from parade')
run=menu(a,b,sound_UI_button)
music=p.mixer.Sound('sounds\\02 Grasslands.ogg')
tmusic=0
t0=t.time()
t2=t0
nframes=0
while run==1 and joon_karbar>0:
    for e in p.event.get():
        if e.type==p.QUIT:
            if run%2==1:
                run=run-1
        elif e.type==p.KEYDOWN:
            if e.key==p.K_f:
                ffwd=not ffwd
                sound_UI_button.play()
            elif e.key==p.K_SPACE or e.key==p.K_p:
                pause=not pause
            elif e.key==p.K_m:
                if audio:
                    sound_explosion_large_01.set_volume(0)
                    sound_invalid.set_volume(0)
                    sound_tower_place2.set_volume(0)
                    sound_UI_button.set_volume(0)
                    music.set_volume(0)
                    audio=False
                else:
                    sound_explosion_large_01.set_volume(1)
                    sound_invalid.set_volume(1)
                    sound_tower_place2.set_volume(1)
                    sound_UI_button.set_volume(1)
                    music.set_volume(1)
                    audio=True
        elif e.type==p.MOUSEBUTTONDOWN:
            x,y=e.pos
            if x>=0.16875*a and x<0.23125*a and y>=0.90835*b and y<99165*b:
                ffwd=not ffwd
                sound_UI_button.play()
            if x>=0.02775*a and x<0.09025*a and y>=0.90835*b and y<99165*b:
                pause=not pause
            if x>=0.24875*a and x<0.31125*a and y>=0.90835*b and y<99165*b:
                if audio:
                    sound_explosion_large_01.set_volume(0)
                    sound_invalid.set_volume(0)
                    sound_tower_place2.set_volume(0)
                    sound_UI_button.set_volume(0)
                    music.set_volume(0)
                    audio=False
                else:
                    sound_explosion_large_01.set_volume(1)
                    sound_invalid.set_volume(1)
                    sound_tower_place2.set_volume(1)
                    sound_UI_button.set_volume(1)
                    music.set_volume(1)
                    audio=True
        f,budjet=buy_guns(areas,e,drag,dt,guns,sound_invalid,sound_tower_place2,sound_UI_button,budjet,cost_guns,soldiers)
        is_waze_changing=is_waze_changing or f
        budjet,gun_for_upgrade=upgrade_guns(areas,budjet,cost_upgrade_guns,e,gun_for_upgrade,guns,mine_areas,sell_profit_guns,sell_profit_upgrade_guns,zaman)
    f,budjet=buy_guns(areas,p.event.Event(p.MOUSEMOTION,{'pos':(drag[1],drag[2]),'rel':(0,0)}),drag,dt,guns,sound_invalid,sound_tower_place2,sound_UI_button,budjet,cost_guns,soldiers)
    is_waze_changing=is_waze_changing or f
    # updates
    # time, music
    t1=t.time()
    dt=t1-t0
    t0=t1
    tmusic=tmusic-dt
    if tmusic<0:
        music.play()
        tmusic=music.get_length()
    nframes=nframes+1
    while int(t1)!=int(t2):
        t2=t2+1
        print('Frame Rate:',nframes,'fps')
        nframes=0
    if dt>0.1:
        dt=0.1
    if ffwd:
        dt=5*dt
    if pause:
        dt=0
    # enter soldiers
    (time_remaining_to_enter_soldier,soldiers,_round)=enter1(time_remaining_to_enter_soldier,dt,b,areas,entrance,joon_soldiers,soldiers,_round)
    # updating soldiers
    if is_waze_changing:
        waze=waze_v(areas)
    update(dt,20*dt,soldiers,sorat_soldiers,waze,areas[0][0][0],areas[0][0][1],areas[0][0][2],(a-16*areas[0][0][2])/2,is_waze_changing)
    is_waze_changing=False
    # guns, arrows, joon
    gun_for_upgrade=tir(a,b,areas,dt,gun_for_upgrade,guns,sc,soldiers,sound_explosion_large_01,tirha,zaman)
    angle_gun(areas,guns,soldiers)
    reduce_joon_soldiers(soldiers,tirha)
    budjet,joon_karbar,scr=budjet_joon(a,b,budjet,scr,soldiers,joon_karbar)
    #
    if _round>100:
        _round=100
        if run//2==0:
            run=run+2
    if joon_karbar<=0:
        joon_karbar=0
    # DDDD      RRRRRR         AAAA    WW             WW
    # DD  DD    RRR RRR        AA AA    WW           WW
    # DD   DD   RR  RR        AA  AA    WW           WW
    # DD    DD  RRRR          AAAAAAA    WW         WW
    # DD    DD  RR RR        AA    AA    WW   WWW   WW
    # DD   DD   RR  RR       AA     AA    WW WW WW WW
    # DD  DD    RR   RR     AA      AA    WW WW WW WW
    # DDDD      RR    RR    AA       AA    WWW   WWW
    sc.blit(gndpic,(0,0))
    for i in range(len(tirha)):
        p.draw.circle(sc,(0,0,0),(int(tirha[i][1]),int(tirha[i][2])),3)
    for i in range(len(soldiers)):
        p.draw.circle(sc,color_soldiers[int(soldiers[i][0][1])-1],(int(soldiers[i][1]),int(soldiers[i][2])),10)
    draw_guns(sc,guns,gunpics)
    # laser
    for i in range(len(guns)):
        if guns[i][0]==4 and guns[i][7]!=-1:
            s=soldiers[guns[i][7]]
            p.draw.line(sc,(255,0,0),(guns[i][1],guns[i][2]),(s[1],s[2]))
    # joon_soldiers
    for i in range(len(soldiers)):
        if soldiers[i][9]>0:
            p.draw.rect(sc,(255,0,0),(soldiers[i][1]-0.4*areas[0][0][2],soldiers[i][2]-20,0.8*areas[0][0][2],5))
            p.draw.rect(sc,(0,255,0),(soldiers[i][1]-0.4*areas[0][0][2],soldiers[i][2]-20,0.8*areas[0][0][2]*soldiers[i][7]/soldiers[i][6],5))
    draw_gun_for_upgrade(sc,areas,gun_for_upgrade,guns,icon_sell,icon_upgrade,icon_upgrade_disabled)
    menu_guns(a,b,cost_guns,budjet,areas)
    if drag[0]!=0:
        sc.blit(gunpics[drag[0]-1][0],(drag[3]*areas[0][0][2]+areas[0][0][0],drag[4]*areas[0][0][2]+areas[0][0][1]))
    # kharbar
    if ffwd:
        sc.blit(ffwd_img,(int(0.16875*a),int(0.90835*b)))
    else:
        sc.blit(ffwd_disabled_img,(int(0.16875*a),int(0.90835*b)))
    if pause:
        sc.blit(hud_play,(int(0.02775*a),int(0.90835*b)))
    else:
        sc.blit(hud_pause,(int(0.02775*a),int(0.90835*b)))
    if audio:
        sc.blit(hud_audio_on,(int(0.24875*a),int(0.90835*b)))
    else:
        sc.blit(hud_audio_off,(int(0.24875*a),int(0.90835*b)))
    # texts
    sc.blit(joon_img,(0.93875*a,0.001665*b))
    text=font.render(str(joon_karbar),True,(255,191,0))
    sc.blit(text,(0.93875*a-40,0.04*b-text.get_height()/2))
    text=font.render(str(scr),True,(255,191,0))
    sc.blit(text,((a-text.get_width())//2,10))
    if pause:
        text=font.render('Paused',True,(255,191,0))
    elif _round>0:
        text=font.render('Round '+str(_round),True,(255,191,0))
    else:
        text=font.render('GAME WILL BEGIN IN '+str(1+int(time_remaining_to_enter_soldier)),True,(255,191,0))
    sc.blit(text,((a-text.get_width())//2,40))
    sc.blit(budjet_img,(0.00125*a,0.001665*b))
    text=font.render(str(budjet),True,(255,191,0))
    sc.blit(text,(0.05875*a,0.04*b-text.get_height()/2))
    p.display.update()
_round=_round-1
entrance.close()
music.stop()
sound_invalid.stop()
sound_tower_place2.stop()
sound_UI_button.stop()
f=True
if run==3:
    p.mixer.Sound('sounds\\victory.wav').play()
    endimg=p.image.load('UserInterface\\text_victory.png')
elif run==1 and joon_karbar<=0:
    p.mixer.Sound('sounds\\failure_tune.wav').play()
    endimg=p.image.load('UserInterface\\text_defeat.png')
else:
    f=False
if f:
    x,y=endimg.get_size()
    sc.blit(endimg,((a-x)/2,(b-y)/2))
while f:
    for e in p.event.get():
        if e.type==p.QUIT:
            f=False
    p.display.update()
p.quit()
