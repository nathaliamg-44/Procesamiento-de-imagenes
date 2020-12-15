# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 10:43:09 2020

@author: na_th
"""
import statistics as stats
import tkinter as tk
from tkinter import ttk, filedialog
import numpy
from PIL import Image, ImageTk
import time


time1 = time.time()

def in_range(num, mi, ma):
    if num > ma:
        return ma
    elif num < mi:
        return mi
    return num  


def rgb_to_y(rgb):
    cy = [0.299000, 0.587000, 0.114000]
    r = rgb[0]/255.0
    g = rgb[1]/255.0
    b = rgb[2]/255.0
    y = cy[0]*r+cy[1]*g+cy[2]*b
    return [y]

def y_to_rgb(yiq):
    cr = [1, 0.9563, 0.6210]
    cg = [1,-0.2721,-0.6474]
    cb = [1,-1.1070, 1.7046]
    y = yiq
    r = cr[0]*y
    g = cg[0]*y
    b = cb[0]*y
    r = in_range(int(round(r*255)), 0, 255)
    g = in_range(int(round(g*255)), 0, 255)
    b = in_range(int(round(b*255)), 0, 255)
    return [r, g, b]

def y2_to_rgb(yiq):
    cr = [1, 0.9563, 0.6210]
    cg = [1,-0.2721,-0.6474]
    cb = [1,-1.1070, 1.7046]
    y = yiq[0]
    r = cr[0]*y
    g = cg[0]*y
    b = cb[0]*y
    r = in_range(int(round(r*255)), 0, 255)
    g = in_range(int(round(g*255)), 0, 255)
    b = in_range(int(round(b*255)), 0, 255)
    return [r, g, b]

def conversion(imgy,imgy2):
    imgg=[]
    for i in range(len(imgy)):
        imgg.append([])
        for j in range(len(imgy[i])):
            imgg[i].append(y2_to_rgb(imgy[i][j]))   
            
    imgmorf=[]
    for i in range(len(imgy2)):
        imgmorf.append([])
        for j in range(len(imgy2[i])):
            imgmorf[i].append(y_to_rgb(imgy2[i][j]))
        
    imggr=numpy.array(imgg, dtype=numpy.uint8)
    imgris=Image.fromarray(imggr, 'RGB')
    morf=numpy.array(imgmorf, dtype=numpy.uint8)
    img=Image.fromarray(morf, 'RGB')
    mostrar(img, imgris)
    
def open1():
    global img2
    global imgeopen1
    file_name=filedialog.askopenfilename(title='UpLoad', filetypes=[('PNG FILES', '*.png')])   
    imgeopen1= Image.open(file_name)
    imgeopen1 =imgeopen1.resize((300,250))
    img2=ImageTk.PhotoImage(imgeopen1)
    lblim.config(image=img2) 


def quit():
    window.destroy()
    
def save():
    global imgfin
    file_name=filedialog.asksaveasfilename(title='UpLoad', filetypes=[('PNG FILES', '.png')])
    imgfin.save(str(file_name)+ '.png', 'PNG')
    print(file_name)
    
def mostrar(img, imgris):
    global imgfin
    global imgfin2  
    global img4
    global img3
    imgfin= img
    img= img.resize((300,250))
    img4=ImageTk.PhotoImage(img)
    lblim3.config(image=img4)
    imgfin2= imgris
    imgris= imgris.resize((300,250))
    img3=ImageTk.PhotoImage(imgris)
    lblim2.config(image=img3)

def copy():
    global imgfin
    global img2
    global imgeopen1  
    imgeopen1= imgfin
    imgeopen1 =imgeopen1.resize((300,250))
    img2=ImageTk.PhotoImage(imgeopen1)
    lblim.config(image=img2)

def more():
    global imgeopen1
    img= imgeopen1
    imgrgb = numpy.asarray(img)
    imgy=[]
    for i in range(len(imgrgb)):
        imgy.append([])
        for j in range(len(imgrgb[i])):
            imgy[i].append(rgb_to_y(imgrgb[i][j]))
    k=3        
    imgy2=[]
    for i in range(len(imgy)):
        imgy2.append([])
        for j in range(len(imgy[i])):
            n1= int( i-(k-1)/2 )
            m1= int(j-(k-1)/2) 
            n2= int(i+(k-1)/2 )
            m2= int(j+(k-1)/2 )
            av = []
            if n1>=0 and m1>=0 and n2<len(imgy) and m2<len(imgy[i]):
                for x in range(n1 ,n2+1):
                    for y in range(m1, m2+1):
                         av.extend(imgy[x][y])
                mini= sorted(av)
                an= mini[0]
                imgy2[i].append(an)
            else:
                an=0
                imgy2[i].append(an)      
    conversion(imgy,imgy2)   
    
    
def mord():
    global imgeopen1
    img= imgeopen1
    imgrgb = numpy.asarray(img)
    imgy=[]
    for i in range(len(imgrgb)):
        imgy.append([])
        for j in range(len(imgrgb[i])):
            imgy[i].append(rgb_to_y(imgrgb[i][j]))
    k=3        
    imgy2=[]
    for i in range(len(imgy)):
        imgy2.append([])
        for j in range(len(imgy[i])):
            n1= int( i-(k-1)/2 )
            m1= int(j-(k-1)/2) 
            n2= int(i+(k-1)/2 )
            m2= int(j+(k-1)/2 )
            av = []
            if n1>=0 and m1>=0 and n2<len(imgy) and m2<len(imgy[i]):
                for x in range(n1 ,n2+1):
                    for y in range(m1, m2+1):
                         av.extend(imgy[x][y])
                mini= sorted(av)
                an= mini[8]
                imgy2[i].append(an)
            else:
                an=0
                imgy2[i].append(an)      
    conversion(imgy,imgy2)   
    
    
def mora():
    global imgeopen1
    img= imgeopen1
    imgrgb = numpy.asarray(img)
    imgy=[]
    for i in range(len(imgrgb)):
        imgy.append([])
        for j in range(len(imgrgb[i])):
            imgy[i].append(rgb_to_y(imgrgb[i][j]))
    k=3 
    imgye=[]
    for i in range(len(imgy)):
        imgye.append([])
        for j in range(len(imgy[i])):
            n1= int( i-(k-1)/2 )
            m1= int(j-(k-1)/2) 
            n2= int(i+(k-1)/2 )
            m2= int(j+(k-1)/2 )
            av = []
            if n1>=0 and m1>=0 and n2<len(imgy) and m2<len(imgy[i]):
                for x in range(n1 ,n2+1):
                    for y in range(m1, m2+1):
                         av.extend(imgy[x][y])
                mini= sorted(av)
                an= mini[0]
                imgye[i].append(an)
            else:
                an=0
                imgye[i].append(an)         
    imgy2=[]
    for i in range(len(imgye)):
        imgy2.append([])
        for j in range(len(imgye[i])):
            n1= int( i-(k-1)/2 )
            m1= int(j-(k-1)/2) 
            n2= int(i+(k-1)/2 )
            m2= int(j+(k-1)/2 )
            av = []
            if n1>=0 and m1>=0 and n2<len(imgye) and m2<len(imgye[i]):
                for x in range(n1 ,n2+1):
                    for y in range(m1, m2+1):
                         av.append(imgye[x][y])
                mini= sorted(av)
                an= mini[8]
                imgy2[i].append(an)
            else:
                an=0
                imgy2[i].append(an)   
    conversion(imgy,imgy2)   
    

def morc():
    global imgeopen1
    img= imgeopen1
    imgrgb = numpy.asarray(img)
    imgy=[]
    for i in range(len(imgrgb)):
        imgy.append([])
        for j in range(len(imgrgb[i])):
            imgy[i].append(rgb_to_y(imgrgb[i][j]))
    k=3 
    imgye=[]
    for i in range(len(imgy)):
        imgye.append([])
        for j in range(len(imgy[i])):
            n1= int( i-(k-1)/2 )
            m1= int(j-(k-1)/2) 
            n2= int(i+(k-1)/2 )
            m2= int(j+(k-1)/2 )
            av = []
            if n1>=0 and m1>=0 and n2<len(imgy) and m2<len(imgy[i]):
                for x in range(n1 ,n2+1):
                    for y in range(m1, m2+1):
                         av.extend(imgy[x][y])
                mini= sorted(av)
                an= mini[8]
                imgye[i].append(an)
            else:
                an=0
                imgye[i].append(an)         
    imgy2=[]
    for i in range(len(imgye)):
        imgy2.append([])
        for j in range(len(imgye[i])):
            n1= int( i-(k-1)/2 )
            m1= int(j-(k-1)/2) 
            n2= int(i+(k-1)/2 )
            m2= int(j+(k-1)/2 )
            av = []
            if n1>=0 and m1>=0 and n2<len(imgye) and m2<len(imgye[i]):
                for x in range(n1 ,n2+1):
                    for y in range(m1, m2+1):
                         av.append(imgye[x][y])
                mini= sorted(av)
                an= mini[0]
                imgy2[i].append(an)
            else:
                an=0
                imgy2[i].append(an)  
                
    conversion(imgy,imgy2)   
    
    
def morbe():
    global imgeopen1
    img= imgeopen1
    imgrgb = numpy.asarray(img)
    imgy=[]
    for i in range(len(imgrgb)):
        imgy.append([])
        for j in range(len(imgrgb[i])):
            imgy[i].append(rgb_to_y(imgrgb[i][j]))
    k=3        
    imgye=[]
    for i in range(len(imgy)):
        imgye.append([])
        for j in range(len(imgy[i])):
            n1= int( i-(k-1)/2 )
            m1= int(j-(k-1)/2) 
            n2= int(i+(k-1)/2 )
            m2= int(j+(k-1)/2 )
            av = []
            if n1>=0 and m1>=0 and n2<len(imgy) and m2<len(imgy[i]):
                for x in range(n1 ,n2+1):
                    for y in range(m1, m2+1):
                         av.extend(imgy[x][y])
                mini= sorted(av)
                an= mini[8]
                imgye[i].append(an)
            else:
                an=0
                imgye[i].append(an) 
    
    imgy2=[] 
    for i in range(len(imgye)):
        imgy2.append([])
        for j in range(len(imgye[i])):
            dil=imgye[i][j]
            ori=imgy[i][j]
            resta=dil-ori[0]
            imgy2[i].append(resta)            
                
    conversion(imgy,imgy2)   
    
    
def morbi():
    global imgeopen1
    img= imgeopen1
    imgrgb = numpy.asarray(img)
    imgy=[]
    for i in range(len(imgrgb)):
        imgy.append([])
        for j in range(len(imgrgb[i])):
            imgy[i].append(rgb_to_y(imgrgb[i][j]))
    k=3        
    imgyi=[]
    for i in range(len(imgy)):
        imgyi.append([])
        for j in range(len(imgy[i])):
            n1= int( i-(k-1)/2 )
            m1= int(j-(k-1)/2) 
            n2= int(i+(k-1)/2 )
            m2= int(j+(k-1)/2 )
            av = []
            if n1>=0 and m1>=0 and n2<len(imgy) and m2<len(imgy[i]):
                for x in range(n1 ,n2+1):
                    for y in range(m1, m2+1):
                         av.extend(imgy[x][y])
                mini= sorted(av)
                an= mini[0]
                imgyi[i].append(an)
            else:
                an=0
                imgyi[i].append(an) 


    imgy2=[] 
    for i in range(len(imgyi)):
        imgy2.append([])
        for j in range(len(imgyi[i])):
            ero=imgyi[i][j]
            ori=imgy[i][j]
            resta=ori[0]-ero
            imgy2[i].append(resta)            
                
    conversion(imgy,imgy2)   
    
 
def morm():
    global imgeopen1
    img= imgeopen1
    imgrgb = numpy.asarray(img)
    imgy=[]
    for i in range(len(imgrgb)):
        imgy.append([])
        for j in range(len(imgrgb[i])):
            imgy[i].append(rgb_to_y(imgrgb[i][j]))
    k=3        
    imgy2=[]
    for i in range(len(imgy)):
        imgy2.append([])
        for j in range(len(imgy[i])):
            n1= int( i-(k-1)/2 )
            m1= int(j-(k-1)/2) 
            n2= int(i+(k-1)/2 )
            m2= int(j+(k-1)/2 )
            av = []
            if n1>=0 and m1>=0 and n2<len(imgy) and m2<len(imgy[i]):
                for x in range(n1 ,n2+1):
                    for y in range(m1, m2+1):
                         av.extend(imgy[x][y])
                mini= stats.median(av)
                imgy2[i].append(mini)
            else:
                an=0
                imgy2[i].append(an)      
    conversion(imgy,imgy2)   
       

def morth():
    global imgeopen1
    img= imgeopen1
    imgrgb = numpy.asarray(img)
    imgy=[]
    for i in range(len(imgrgb)):
        imgy.append([])
        for j in range(len(imgrgb[i])):
            imgy[i].append(rgb_to_y(imgrgb[i][j]))
    k=3 
    imgye=[]
    for i in range(len(imgy)):
        imgye.append([])
        for j in range(len(imgy[i])):
            n1= int( i-(k-1)/2 )
            m1= int(j-(k-1)/2) 
            n2= int(i+(k-1)/2 )
            m2= int(j+(k-1)/2 )
            av = []
            if n1>=0 and m1>=0 and n2<len(imgy) and m2<len(imgy[i]):
                for x in range(n1 ,n2+1):
                    for y in range(m1, m2+1):
                         av.extend(imgy[x][y])
                mini= sorted(av)
                an= mini[0]
                imgye[i].append(an)
            else:
                an=0
                imgye[i].append(an)         
    imgyd=[]
    for i in range(len(imgye)):
        imgyd.append([])
        for j in range(len(imgye[i])):
            n1= int( i-(k-1)/2 )
            m1= int(j-(k-1)/2) 
            n2= int(i+(k-1)/2 )
            m2= int(j+(k-1)/2 )
            av = []
            if n1>=0 and m1>=0 and n2<len(imgye) and m2<len(imgye[i]):
                for x in range(n1 ,n2+1):
                    for y in range(m1, m2+1):
                         av.append(imgye[x][y])
                mini= sorted(av)
                an= mini[8]
                imgyd[i].append(an)
            else:
                an=0
                imgyd[i].append(an)  
    imgy2=[]
    for i in range(len(imgyd)):
        imgy2.append([])
        for j in range(len(imgyd[i])):
            aper=imgyd[i][j]
            ori=imgy[i][j]
            resta=aper-ori[0]
            imgy2[i].append(resta) 
    
    conversion(imgy,imgy2)   
    
    
    
def morfologia():
    
    morfo = combo.get()
    if morfo=="Erosión":
        more()
    elif morfo == "Dilatación":
        mord()
    elif morfo == "Apertura":
        mora()
    elif morfo == "Cierre":
        morc()
    elif morfo == "Borde Exterior":
        morbe()
    elif morfo == "Borde Interior":
        morbi()
    elif morfo == "Mediana":
        morm()
    elif morfo == "Top Hat":
        morth()
 
       
imge2= Image.open("tras.png")
imge2 = imge2.resize((300,250))
imgeopen1= None
imgeopen2= None
imgfin=None
imgfin2=None
window = tk.Tk()
window.title("Procesamiento Morfológico")
window.geometry ("1100x370")
combo = ttk.Combobox(window)
combo['values']=("Erosión","Dilatación","Apertura","Cierre","Borde Exterior","Borde Interior","Mediana","Top Hat")
combo.set('Erosión')
#lbl = tk.Label(window, text = "Original").grid(column=0, row=1)
lbl2 = tk.Label(window, text = "Imagen Filtrada").grid(column=3, row=3)
lblin = tk.Label(window, text = "Operaciones").grid(column=2, row=3)
lblax = tk.Label(window, text = "Imagen Escala de Grises").grid(column=1, row=3)
lblor = tk.Label(window, text = "Imagen Original").grid(column=0, row=3)
lker = None
yy= tk.Label(window, text = "")
#txt1= tk.Entry(window,   width = 7)
#txt1.insert(0,"0.2")
#txt2= tk.Entry(window, width = 7) 
#txt2.insert(0,"0.8")
bcerrar = tk.Button(window, text= "Cerrar", 
                 command = quit)
bapply = tk.Button(window, text= "Aplicar", 
                 command = morfologia)
bsave = tk.Button(window, text= "Guardar", 
                 command = save)
bopen1 = tk.Button(window, text= "Abrir imagen 1", 
                 command = open1)
bcopy = tk.Button(window, text= "Copiar", 
                 command = copy)
img2= ImageTk.PhotoImage(imge2)
lblim=tk.Label(window,image=img2)
img3= None
lblim2= tk.Label(window,image=img3)
img4= None
lblim3= tk.Label(window,image=img4)
bcerrar.grid(column=4, row=4)
bapply.grid(column=2, row=1)
bsave.grid(column=3, row=0)
bopen1.grid(column=0, row=1)
bcopy.grid(column=2, row=4)
#txt1.grid(column= 1, row =3)
#txt2.grid(column= 1, row =4)
yy.grid(column=3, row=0)
lblim.grid(column=0, row=2)
lblim2.grid(column=1, row=2)
lblim3.grid(column=3, row=2)
combo.grid(column=2, row=2  )
time2 = time.time()
print ("Demora: ", time2-time1, "segundos")
window.mainloop()
