# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 15:46:00 2020

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

def in_range_steps(num, mini, maxi):
    if num > maxi:
        return 1
    elif num < mini:
        return 0
    return num

def rgb_to_yiq(rgb):
    cy = [0.299000, 0.587000, 0.114000]
    ci = [0.595716,-0.274453,-0.321263]
    cq = [0.211456,-0.522591, 0.311135]
    r = rgb[0]/255.0
    g = rgb[1]/255.0
    b = rgb[2]/255.0
    y = cy[0]*r+cy[1]*g+cy[2]*b
    i = ci[0]*r+ci[1]*g+ci[2]*b
    q = cq[0]*r+cq[1]*g+cq[2]*b
    return [y,i,q]

def yiq_to_rgb(yiq):
    cr = [1, 0.9563, 0.6210]
    cg = [1,-0.2721,-0.6474]
    cb = [1,-1.1070, 1.7046]
    y = yiq[0]
    i = yiq[1]
    q = yiq[2]
    r = cr[0]*y+cr[1]*i+cr[2]*q
    g = cg[0]*y+cg[1]*i+cg[2]*q
    b = cb[0]*y+cb[1]*i+cb[2]*q
    r = in_range(int(round(r*255)), 0, 255)
    g = in_range(int(round(g*255)), 0, 255)
    b = in_range(int(round(b*255)), 0, 255)
    return [r, g, b]

def y_sqroot(yiq):
    y1 = yiq[0]
    i1 = yiq[1]
    q1 = yiq[2]
    py = in_range_steps(numpy.sqrt(y1), 0, 1)
    pi = in_range(i1, -0.5957, 0.5957)
    pq = in_range(q1, -0.5226, 0.5226)
    return [py,pi,pq]

def y_potencia(yiq):
    y1 = yiq[0]
    i1 = yiq[1]
    q1 = yiq[2]
    py = in_range(y1 * y1, 0, 1)
    pi = in_range(i1, -0.5957, 0.5957)
    pq = in_range(q1, -0.5226, 0.5226)
    return [py,pi,pq]

def y_shred(yiq,mini,maxi):
    y1 = yiq[0]
    i1 = yiq[1]
    q1 = yiq[2]
    py = in_range_steps(y1, mini, maxi)
    pi = in_range(i1, -0.5957, 0.5957)
    pq = in_range(q1, -0.5226, 0.5226)
    return [py,pi,pq]
        
def mostrar(img_2, tim3):
    global imge3
    global img3
    imge3= img_2
    img_2= img_2.resize((300,250))
    img3=ImageTk.PhotoImage(img_2)
    lblim2.config(image=img3)
    time4= time.time()
    print("El filtro se demora:", time4-tim3, "segundos")

def event():
    global imge3
    file_name=filedialog.asksaveasfilename(title='UpLoad', filetypes=[('PNG FILES', '.png')])
    imge3.save(str(file_name)+ '.png', 'PNG')
    print(file_name)
    
def quit():
    window.destroy()
    
def open1():
    global img2
    global imgeopen1
    file_name=filedialog.askopenfilename(title='UpLoad', filetypes=[('PNG FILES', '*.png')])   
    imgeopen1= Image.open(file_name)
    imgeopen1=imgeopen1.resize((300,250))
    img2=ImageTk.PhotoImage(imgeopen1)
    lblim.config(image=img2)
    
def filtre():
    op=combo.get()
    if op=="Raíz":
        sqroot()
    elif op=="Potencia":
        potencia()
    elif op=="Función a trozos":
        mini = float(txt1.get())
        maxi = float(txt2.get())
        print(type(mini), type(maxi))
        shred(mini,maxi)
        return (mini, maxi)
    
def sqroot():
    tim3 = time.time()
    global imgeopen1
    imgrgb = numpy.asarray(imgeopen1)
    
    imgyiq=[]
    for i in range(len(imgrgb)):
        imgyiq.append([])
        for j in range(len(imgrgb[i])):
            imgyiq[i].append(rgb_to_yiq(imgrgb[i][j]))
    
    imgyiq2=[]
    for i in range(len(imgyiq)):
        imgyiq2.append([])
        for j in range(len(imgyiq[i])):
            imgyiq2[i].append(y_sqroot(imgyiq[i][j]))
    
    imgrgb2=[]
    for i in range(len(imgyiq2)):
        imgrgb2.append([])
        for j in range(len(imgyiq2[i])):
            imgrgb2[i].append(yiq_to_rgb(imgyiq2[i][j]))
    
    px2=numpy.array(imgrgb2, dtype=numpy.uint8)
    img_2 = Image.fromarray(px2, 'RGB')
    mostrar(img_2,tim3)
    return img_2

def potencia():
    tim3 = time.time()
    global imgeopen1
    imgrgb = numpy.asarray(imgeopen1)
    
    
    imgyiq=[]
    for i in range(len(imgrgb)):
        imgyiq.append([])
        for j in range(len(imgrgb[i])):
            imgyiq[i].append(rgb_to_yiq(imgrgb[i][j]))
    
    imgyiq2=[]
    for i in range(len(imgyiq)):
        imgyiq2.append([])
        for j in range(len(imgyiq[i])):
            imgyiq2[i].append(y_potencia(imgyiq[i][j]))
    
    imgrgb2=[]
    for i in range(len(imgyiq2)):
        imgrgb2.append([])
        for j in range(len(imgyiq2[i])):
            imgrgb2[i].append(yiq_to_rgb(imgyiq2[i][j]))
    
    px2=numpy.array(imgrgb2, dtype=numpy.uint8)
    img_2 = Image.fromarray(px2, 'RGB')
    mostrar(img_2, tim3)
    return img_2

def shred(mini, maxi):
    tim3 = time.time()
    global imgeopen1
    imgrgb = numpy.asarray(imgeopen1)
    
    
    imgyiq=[]
    for i in range(len(imgrgb)):
        imgyiq.append([])
        for j in range(len(imgrgb[i])):
            imgyiq[i].append(rgb_to_yiq(imgrgb[i][j]))
    
    imgyiq2=[]
    for i in range(len(imgyiq)):
        imgyiq2.append([])
        for j in range(len(imgyiq[i])):
            imgyiq2[i].append(y_shred((imgyiq[i][j]),mini, maxi))
    
    imgrgb2=[]
    for i in range(len(imgyiq2)):
        imgrgb2.append([])
        for j in range(len(imgyiq2[i])):
            imgrgb2[i].append(yiq_to_rgb(imgyiq2[i][j]))
    
    px2=numpy.array(imgrgb2, dtype=numpy.uint8)
    img_2 = Image.fromarray(px2, 'RGB')
    mostrar(img_2, tim3)
    return img_2

imge2= Image.open("tras.png")
imge2 = imge2.resize((300,250))
imge3= None
imgeopen1= None
window = tk.Tk()
window.title("Filtros")
window.geometry ("700x350")
combo = ttk.Combobox(window)
combo['values']=("Raíz","Potencia","Función a trozos")
combo.set('Potencia')
lbl = tk.Label(window, text = "Original").grid(column=0, row=1)
lbl2 = tk.Label(window, text = "Nueva").grid(column=1, row=1)
lblin = tk.Label(window, text = "Valor mínimo").grid(column=2, row=6)
lblax = tk.Label(window, text = "Valor máximo").grid(column=2, row=7)
yy= tk.Label(window, text = "")
txt1= tk.Entry(window,   width = 7)
txt1.insert(0,"0.2")
txt2= tk.Entry(window, width = 7) 
txt2.insert(0,"0.8")
bcerrar = tk.Button(window, text= "Cerrar", 
                 command = quit)
bapply = tk.Button(window, text= "Aplicar", 
                 command = filtre)
bsave = tk.Button(window, text= "Guardar", 
                 command = event)
bopen1= tk.Button(window, text= "Abrir", 
                 command = open1)
img2= ImageTk.PhotoImage(imge2)
lblim=tk.Label(window,image=img2)
img3= None
lblim2= tk.Label(window,image=img3)
bcerrar.grid(column=2, row=0)
bapply.grid(column=2, row=5)
bsave.grid(column=1, row=0)
bopen1.grid(column=0, row=0)
txt1.grid(column= 1, row =6)
txt2.grid(column= 1, row =7)
yy.grid(column=3, row=0)
lblim.grid(column=0, row=5)
lblim2.grid(column=1, row=5)
combo.grid(column=0, row=6)
time2 = time.time()
print ("Demora:", time2-time1, "segundos")
window.mainloop()


