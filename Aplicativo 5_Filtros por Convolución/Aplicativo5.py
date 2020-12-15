# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 18:06:04 2020

@author: na_th
"""

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
            
    imgfilcon=[]
    for i in range(len(imgy2)):
        imgfilcon.append([])
        for j in range(len(imgy2[i])):
            imgfilcon[i].append(y_to_rgb(imgy2[i][j]))
        
    imggr=numpy.array(imgg, dtype=numpy.uint8)
    imgris=Image.fromarray(imggr, 'RGB')
    filtrocon=numpy.array(imgfilcon, dtype=numpy.uint8)
    img=Image.fromarray(filtrocon, 'RGB')
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

def fil(k):
    global imgeopen1
    img= imgeopen1
    imgrgb = numpy.asarray(img)
    imgy=[]
    for i in range(len(imgrgb)):
        imgy.append([])
        for j in range(len(imgrgb[i])):
            imgy[i].append(rgb_to_y(imgrgb[i][j]))
            
    kl=len(k)
    imgy2=[]
    for i in range(len(imgy)):
        imgy2.append([])
        for j in range(len(imgy[i])):
            n1= int( i-(kl-1)/2 )
            m1= int(j-(kl-1)/2) 
            n2= int(i+(kl-1)/2 )
            m2= int(j+(kl-1)/2 )
            av = 0
            n=0
            if n1>=0 and m1>=0 and n2<len(imgy) and m2<len(imgy[i]):
                for x in range(n1 ,n2+1):
                    m=0
                    for y in range(m1, m2+1):
                         pel=imgy[x][y]
                         av += pel[0]*k[n][m]
                         m+=1
                    n+=1
                an= av 
                imgy2[i].append(an)
            else:
                an=0
                imgy2[i].append(an)      

    conversion(imgy,imgy2)  
    
def filsob(k):
    global lker
    lker=tk.Label(window, text = k).grid(column=2, row=4)
    global imgeopen1
    img= imgeopen1
    imgrgb = numpy.asarray(img)
    imgy=[]
    for i in range(len(imgrgb)):
        imgy.append([])
        for j in range(len(imgrgb[i])):
            imgy[i].append(rgb_to_y(imgrgb[i][j]))
            
    kl=len(k)
    imgy2=[]
    for i in range(len(imgy)):
        imgy2.append([])
        for j in range(len(imgy[i])):
            n1= int( i-(kl-1)/2 )
            m1= int(j-(kl-1)/2) 
            n2= int(i+(kl-1)/2 )
            m2= int(j+(kl-1)/2 )
            av = 0
            n=0
            if n1>=0 and m1>=0 and n2<len(imgy) and m2<len(imgy[i]):
                for x in range(n1 ,n2+1):
                    m=0
                    for y in range(m1, m2+1):
                         pel=imgy[x][y]
                         av += pel[0]*k[n][m]
                         m+=1
                    n+=1
                an= av 
                imgy2[i].append(an)
            else:
                an=0
                imgy2[i].append(an)      

    conversion(imgy,imgy2)    
    
def filtre():
    filtro = combo.get()
    if filtro=="Barlett 3x3":
        k=[(1/16,2/16,1/16),(2/16,4/16,2/16),(1/16,2/16,1/16)]
        fil(k)
    elif filtro =="Barlett 5x5":
        k=[(1/81,2/81,3/81,2/81,1/81),(2/81,4/81,6/81,4/81,2/81),(3/81,6/81,9/81,6/81,3/81),(2/81,4/81,6/81,4/81,2/81),(1/81,2/81,3/81,2/81,1/81)]
        fil(k)
    elif filtro == "Barlett 7x7":
        k=[(1/220,2/220,3/220,4/220,3/220,2/220,1/220),(2/220,4/220,6/220,8/220,6/220,4/220,2/220),(3/220,6/220,9/220,12/220,9/220,6/220,3/220),(4/220,8/220,12/220,16/220,12/220,8/220,4/220),(3/220,6/220,9/220,12/220,9/220,6/220,3/220),(2/220,4/220,6/220,8/220,6/220,4/220,2/220),(1/220,2/220,3/220,4/220,3/220,2/220,1/220)]
        fil(k)
    elif filtro == "Gaussiano":
        k=[(1/256,4/256,6/256,4/256,1/256),(4/256,16/256,24/256,16/256,4/256),(6/256,24/256,36/256,24/256,6/256),(4/256,16/256,24/256,16/256,4/256),(1/256,4/256,6/256,4/256,1/256)]
        fil(k)
    elif filtro == "Laplaciano v4 3x3":
        k=[(0,-1,0),(-1, 4,-1),(0, -1, 0)]
        fil(k)
    elif filtro == "Laplaciano v8 3x3":
        k=[(-1,-1,-1),(-1, 8,-1),(-1, -1, -1)]
        fil(k)
    elif filtro == "Sobel1":
        k=[(-1,0,1),(-2, 0,2),(-1,0,1)]
        filsob(k)
    elif filtro == "Sobe2":
        k=[(-2,-1,0),(-1, 0,1),(0,1,2)]
        filsob(k)
    elif filtro == "Sobel3":
        k=[(-1,-2,-1),(0, 0,0),(1,2,1)]
        filsob(k)
    elif filtro == "Sobel4":
        k=[(0,-1,-2),(1, 0,-1),(2,1,0)]
        filsob(k)
    elif filtro == "Sobel5":
        k=[(1,0,-1),(2, 0,-2),(1,0,-1)]
        filsob(k)
    elif filtro == "Sobel6":
        k=[(2,1,0),(1, 0,-1),(0,-1,-2)]
        filsob(k)
    elif filtro == "Sobel7":
        k=[(1,2,1),(0,0,0),(-1,-2,-1)]
        filsob(k)
    elif filtro == "Sobel8":
        k=[(0,1,2),(-1, 0,1),(-2,-1,0)]
        filsob(k)
       
imge2= Image.open("tras.png")
imge2 = imge2.resize((300,250))
imgeopen1= None
imgeopen2= None
imgfin=None
imgfin2=None
window = tk.Tk()
window.title("Filtros con Convolución")
window.geometry ("1100x370")
combo = ttk.Combobox(window)
combo['values']=("Barlett 3x3","Barlett 5x5","Barlett 7x7","Laplaciano v4 3x3","Laplaciano v8 3x3","Gaussiano", "Sobel1","Sobel2","Sobel3","Sobel4","Sobel5","Sobel6","Sobel7","Sobel8")
combo.set('Barlett 3x3')
#lbl = tk.Label(window, text = "Original").grid(column=0, row=1)
lbl2 = tk.Label(window, text = "Imagen Filtrada").grid(column=3, row=3)
lblin = tk.Label(window, text = "Filtro").grid(column=2, row=3)
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
                 command = filtre)
bsave = tk.Button(window, text= "Guardar", 
                 command = save)
bopen1 = tk.Button(window, text= "Abrir imagen 1", 
                 command = open1)
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


