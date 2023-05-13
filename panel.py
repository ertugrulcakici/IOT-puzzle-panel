import os
from time import sleep, time

from machine import ADC, Pin

g1 = Pin(0, Pin.OUT, value = 0)
f1 = Pin(1, Pin.OUT, value = 0)
a1 = Pin(2, Pin.OUT, value = 0)
b1 = Pin(3, Pin.OUT, value = 0)
e1 = Pin(4, Pin.OUT, value = 0)
d1 = Pin(5, Pin.OUT, value = 0)
c1 = Pin(6, Pin.OUT, value = 0)

g2 = Pin(7, Pin.OUT, value = 0)
f2 = Pin(8, Pin.OUT, value = 0)
a2 = Pin(9, Pin.OUT, value = 0)
b2 = Pin(10, Pin.OUT, value = 0)
e2 = Pin(11, Pin.OUT, value = 0)
d2 = Pin(12, Pin.OUT, value = 0)
c2 = Pin(13, Pin.OUT, value = 0)

g3 = Pin(14, Pin.OUT, value = 0)
f3 = Pin(15, Pin.OUT, value = 0)
a3 = Pin(16, Pin.OUT, value = 0)
b3 = Pin(17, Pin.OUT, value = 0)
e3 = Pin(18, Pin.OUT, value = 0)
d3 = Pin(19, Pin.OUT, value = 0)
c3 = Pin(20, Pin.OUT, value = 0)



adc1 = ADC(26)
adc2 = ADC(28)
adc3 = ADC(27)

adcs = (adc1,adc2,adc3)






def blink(sayi: int,times: int):
    for i in range(times):
        sleep(0.1)
        sayi_yaz(sayi)
        sleep(0.1)
        sondur_all()

def sondur(segment: int):
        segmentler = ()
        if segment == 0:
                segmentler = (a1,b1,c1,d1,e1,f1,g1)
        elif segment == 1:
                segmentler = (a2,b2,c2,d2,e2,f2,g2)
        elif segment == 2:
                segmentler = (a3,b3,c3,d3,e3,f3,g3)
                
        for i in segmentler:
                i.value(0)

def sondur_all():
    sondur(0)
    sondur(1)
    sondur(2)

def rakam_yaz(rakam, segment):
        segmentler = ()
        if segment == 0:
                if rakam == 0: segmentler = (a1,b1,c1,d1,e1,f1)
                elif rakam == 1: segmentler = (f1,e1)
                elif rakam == 2: segmentler = (a1,b1,g1,e1,d1)
                elif rakam == 3: segmentler = (a1,b1,g1,c1,d1)
                elif rakam == 4: segmentler = (f1,g1,b1,c1)
                elif rakam == 5: segmentler = (a1,f1,g1,c1,d1)
                elif rakam == 6: segmentler = (a1,f1,g1,e1,c1,d1)
                elif rakam == 7: segmentler = (a1,b1,c1)
                elif rakam == 8: segmentler = (a1,b1,c1,d1,e1,f1,g1)
                elif rakam == 9: segmentler = (a1,b1,c1,d1,f1,g1)
        elif segment == 1:
                if rakam == 0: segmentler = (a2,b2,c2,d2,e2,f2)
                elif rakam == 1: segmentler = (f2,e2)
                elif rakam == 2: segmentler = (a2,b2,g2,e2,d2)
                elif rakam == 3: segmentler = (a2,b2,g2,c2,d2)
                elif rakam == 4: segmentler = (f2,g2,b2,c2)
                elif rakam == 5: segmentler = (a2,f2,g2,c2,d2)
                elif rakam == 6: segmentler = (a2,f2,g2,e2,c2,d2)
                elif rakam == 7: segmentler = (a2,b2,c2)
                elif rakam == 8: segmentler = (a2,b2,c2,d2,e2,f2,g2)
                elif rakam == 9: segmentler = (a2,b2,c2,d2,f2,g2)
        elif segment == 2:
                if rakam == 0: segmentler = (a3,b3,c3,d3,e3,f3)
                elif rakam == 1: segmentler = (f3,e3)
                elif rakam == 2: segmentler = (a3,b3,g3,e3,d3)
                elif rakam == 3: segmentler = (a3,b3,g3,c3,d3)
                elif rakam == 4: segmentler = (f3,g3,b3,c3)
                elif rakam == 5: segmentler = (a3,f3,g3,c3,d3)
                elif rakam == 6: segmentler = (a3,f3,g3,e3,c3,d3)
                elif rakam == 7: segmentler = (a3,b3,c3)
                elif rakam == 8: segmentler = (a3,b3,c3,d3,e3,f3,g3)
                elif rakam == 9: segmentler = (a3,b3,c3,d3,f3,g3)

        for i in segmentler:
                i.value(1)

def sayi_yaz(sayi: int):
        sondur(0)
        sondur(1)
        sondur(2)
        birler = sayi % 10
        onlar = (sayi // 10) % 10
        yuzler = (sayi // 100) % 10

        #print(f"{sayi} sayısının yüzler, onlar ve birler bölümleri: {yuzler}, {onlar}, {birler}")
        
        rakam_yaz(yuzler,0)
        rakam_yaz(onlar,1)
        rakam_yaz(birler,2)

def setup_values():
    print("setup mode")
    data = []
    for r in range(3):
        for c in range(3):
            sondur_all()
            
            rakam_yaz(r+1,0)
            rakam_yaz(c+1,2)
            sleep(5)
            blink((r+1)*100+(c+1),5)
            
            rakam_yaz(r+1,0)
            rakam_yaz(c+1,2)
            value = maxx = minn = adcs[r].read_u16() * (3.3/(65536))
            start_time = time()
            while True:
                if time() - start_time > 10:
                    break
                value =adcs[r].read_u16() * (3.3/(65536))
                if value > maxx:
                    maxx = value
                if value < minn:
                    minn = value
            blink((r+1)*100+(c+1),20)
            data.append(str(minn)+"-"+str(maxx))

    open("data.txt","w").write(",".join(data))
    for i in range(1,10):
        sayi_yaz(i)
        
    sondur_all()


def run_mode():
    data = open("data.txt","r").read().split(",")
    print("run mode")
    print(data)
    while True:
        sleep(0.4)
        value_1 = adc1.read_u16() * (3.3/(65536))
        value_2 = adc2.read_u16() * (3.3/(65536))
        value_3 = adc3.read_u16() * (3.3/(65536))
        print(f"{value_1},{value_2},{value_3}")
        if(value_1>float(data[0].split("-")[0]) and value_1 < float(data[0].split("-")[1])):
            sayi_yaz(223)
            sleep(0.1)
        elif (value_1>float(data[1].split("-")[0]) and value_1 < float(data[1].split("-")[1])):
            sayi_yaz(238)
            sleep(0.1)
        elif (value_1>float(data[2].split("-")[0]) and value_1 < float(data[2].split("-")[1])):
            sayi_yaz(98)
            sleep(0.1)
        elif (value_2>float(data[3].split("-")[0]) and value_2 < float(data[3].split("-")[1])):
            sayi_yaz(105)
            sleep(0.1)
        elif (value_2>float(data[4].split("-")[0]) and value_2 < float(data[4].split("-")[1])):
            sayi_yaz(290)
            sleep(0.1)
        elif (value_2>float(data[5].split("-")[0]) and value_2 < float(data[5].split("-")[1])):
            sayi_yaz(221)
            sleep(0.1)
        elif (value_3>float(data[6].split("-")[0]) and value_3 < float(data[6].split("-")[1])):
            sayi_yaz(331)
            sleep(0.1)
        elif (value_3>float(data[7].split("-")[0]) and value_3 < float(data[7].split("-")[1])):
            sayi_yaz(55)
            sleep(0.1)
        elif (value_3>float(data[8].split("-")[0]) and value_3 < float(data[8].split("-")[1])):
            sayi_yaz(197)
            sleep(0.1)
        else:
            sondur_all()

    
sleep(0.3)
first_value = adc1.read_u16() * (3.3 / 65535)
print("first value:",first_value)
if  first_value > 0.01 and first_value < 0.1: 
    setup_values()

run_mode()
