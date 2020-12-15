# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 11:18:51 2020

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
    
def open1():
    global img2
    global imgeopen1
    file_name=filedialog.askopenfilename(title='UpLoad', filetypes=[('PNG FILES', '*.png')])   
    imgeopen1= Image.open(file_name)
    imgeopen1 =imgeopen1.resize((300,250))
    img2=ImageTk.PhotoImage(imgeopen1)
    lblim.config(image=img2) 

def open2():
    global img3
    global imgeopen2
    file_name=filedialog.askopenfilename(title='UpLoad', filetypes=[('PNG FILES', '*.png')])   
    imgeopen2= Image.open(file_name)
    imgeopen2 =imgeopen2.resize((300,250))
    img3=ImageTk.PhotoImage(imgeopen2)
    lblim2.config(image=img3) 

def quit():
    window.destroy()
    
def save():
    global imgfin
    file_name=filedialog.asksaveasfilename(title='UpLoad', filetypes=[('PNG FILES', '.png')])
    imgfin.save(str(file_name)+ '.png', 'PNG')
    print(file_name)
    
def mostrar(img_f):
    global imgfin
    global img4
    imgfin= img_f
    img_f= img_f.resize((300,250))
    img4=ImageTk.PhotoImage(img_f)
    lblim3.config(image=img4)

   

def filtre():
    formato=combo.get()
    operacion = combo2.get()
    if operacion=="Suma" and formato== "RGB-Promediado":
        cuasi_suma11()
    elif operacion=="Suma" and formato== "RGB-Clampeado":
        cuasi_suma12()
    elif operacion=="Suma" and formato== "YIQ-Promediado":
        cuasi_suma13()
    elif operacion=="Suma" and formato== "YIQ-Clampeado":
        cuasi_suma14()
    elif operacion=="Resta" and formato== "RGB-Promediado":
        cuasi_resta21()
    elif operacion=="Resta" and formato== "RGB-Clampeado":
        cuasi_resta22()
    elif operacion=="Resta" and formato== "YIQ-Promediado":
        cuasi_resta23()
    elif operacion=="Resta" and formato== "YIQ-Clampeado":
        cuasi_resta24()
    elif operacion=="If-lighter":
        if_lig()
    elif operacion=="If-darker":
        if_dar() 

def plus_clamp(rgb,efv):
    r = int(rgb[0])
    g = int(rgb[1])
    b = int(rgb[2])
    e = int(efv[0])
    f = int(efv[1])
    v = int(efv[2])
    rc= r+e
    gc= g+f
    bc= b+v
    rc = in_range(rc, 0, 255)
    gc = in_range(gc, 0, 255)
    bc = in_range(bc, 0, 255)
    return [rc,gc,bc]

def subt_clamp(rgb,efv):
    r = int(rgb[0])
    g = int(rgb[1])
    b = int(rgb[2])
    e = int(efv[0])
    f = int(efv[1])
    v = int(efv[2])
    rc= r-e
    gc= g-f
    bc= b-v
    rc = in_range(rc, 0, 255)
    gc = in_range(gc, 0, 255)
    bc = in_range(bc, 0, 255)
    return [rc,gc,bc]

def plus_pro(rgb,efv):
    r = int(rgb[0])
    g = int(rgb[1])
    b = int(rgb[2])
    e = int(efv[0])
    f = int(efv[1])
    v = int(efv[2])
    rc= (r+e)/2
    gc= (g+f)/2
    bc= (b+v)/2
    rc = in_range(rc, 0, 255)
    gc = in_range(gc, 0, 255)
    bc = in_range(bc, 0, 255)
    return [rc,gc,bc]

def subt_pro(rgb,efv):
    r = int(rgb[0])
    g = int(rgb[1])
    b = int(rgb[2])
    e = int(efv[0])
    f = int(efv[1])
    v = int(efv[2])
    rc= (r-e)/2
    gc= (g-f)/2
    bc= (b-v)/2
    rc = in_range(rc, 0, 255)
    gc = in_range(gc, 0, 255)
    bc = in_range(bc, 0, 255)
    return [rc,gc,bc]

def plusclam_yiq(rgb, efv):
    cy = [0.299000, 0.587000, 0.114000]
    ci = [0.595716,-0.274453,-0.321263]
    cq = [0.211456,-0.522591, 0.311135]
    r = rgb[0]/255.0
    g = rgb[1]/255.0
    b = rgb[2]/255.0
    e = efv[0]/255.0
    f = efv[1]/255.0
    v = efv[2]/255.0
    ya = cy[0]*r+cy[1]*g+cy[2]*b
    ia = ci[0]*r+ci[1]*g+ci[2]*b
    qa = cq[0]*r+cq[1]*g+cq[2]*b
    yb = cy[0]*e+cy[1]*f+cy[2]*v
    ib = ci[0]*e+ci[1]*f+ci[2]*v
    qb = cq[0]*e+cq[1]*f+cq[2]*v
    yc= (ya+yb)
    yc = in_range(yc, 0, 1)
    ic =((ya*ia)+(yb*ib))/(ya+yb)
    qc =((ya*qa)+(yb*qb))/(ya+yb)
    ic = in_range(ic, -0.5957, 0.5957)
    qc = in_range(qc, -0.5226, 0.5226)
    return [yc,ic,qc]

def pluspro_yiq(rgb, efv):
    cy = [0.299000, 0.587000, 0.114000]
    ci = [0.595716,-0.274453,-0.321263]
    cq = [0.211456,-0.522591, 0.311135]
    r = rgb[0]/255.0
    g = rgb[1]/255.0
    b = rgb[2]/255.0
    e = efv[0]/255.0
    f = efv[1]/255.0
    v = efv[2]/255.0
    ya = cy[0]*r+cy[1]*g+cy[2]*b
    ia = ci[0]*r+ci[1]*g+ci[2]*b
    qa = cq[0]*r+cq[1]*g+cq[2]*b
    yb = cy[0]*e+cy[1]*f+cy[2]*v
    ib = ci[0]*e+ci[1]*f+ci[2]*v
    qb = cq[0]*e+cq[1]*f+cq[2]*v
    yc= (ya+yb)/2
    yc = in_range(yc, 0, 1)
    ic =((ya*ia)+(yb*ib))/(ya+yb)
    qc =((ya*qa)+(yb*qb))/(ya+yb)
    ic = in_range(ic, -0.5957, 0.5957)
    qc = in_range(qc, -0.5226, 0.5226)
    return [yc,ic,qc]

def subtclam_yiq(rgb, efv):
    cy = [0.299000, 0.587000, 0.114000]
    ci = [0.595716,-0.274453,-0.321263]
    cq = [0.211456,-0.522591, 0.311135]
    r = rgb[0]/255.0
    g = rgb[1]/255.0
    b = rgb[2]/255.0
    e = efv[0]/255.0
    f = efv[1]/255.0
    v = efv[2]/255.0
    ya = cy[0]*r+cy[1]*g+cy[2]*b
    ia = ci[0]*r+ci[1]*g+ci[2]*b
    qa = cq[0]*r+cq[1]*g+cq[2]*b
    yb = cy[0]*e+cy[1]*f+cy[2]*v
    ib = ci[0]*e+ci[1]*f+ci[2]*v
    qb = cq[0]*e+cq[1]*f+cq[2]*v
    yc= (ya-yb)
    yc = in_range(yc, 0, 1)
    ic =((ya*ia)-(yb*ib))/(ya+yb)
    qc =((ya*qa)-(yb*qb))/(ya+yb)
    ic = in_range(ic, -0.5957, 0.5957)
    qc = in_range(qc, -0.5226, 0.5226)
    return [yc,ic,qc]

def subtpro_yiq(rgb, efv):
    cy = [0.299000, 0.587000, 0.114000]
    ci = [0.595716,-0.274453,-0.321263]
    cq = [0.211456,-0.522591, 0.311135]
    r = rgb[0]/255.0
    g = rgb[1]/255.0
    b = rgb[2]/255.0
    e = efv[0]/255.0
    f = efv[1]/255.0
    v = efv[2]/255.0
    ya = cy[0]*r+cy[1]*g+cy[2]*b
    ia = ci[0]*r+ci[1]*g+ci[2]*b
    qa = cq[0]*r+cq[1]*g+cq[2]*b
    yb = cy[0]*e+cy[1]*f+cy[2]*v
    ib = ci[0]*e+ci[1]*f+ci[2]*v
    qb = cq[0]*e+cq[1]*f+cq[2]*v
    yc= (ya-yb)/2
    yc = in_range(yc, 0, 1)
    ic =((ya*ia)-(yb*ib))/(ya+yb)
    qc =((ya*qa)-(yb*qb))/(ya+yb)
    ic = in_range(ic, -0.5957, 0.5957)
    qc = in_range(qc, -0.5226, 0.5226)
    return [yc,ic,qc]

def if_lighter(rgb, efv):
    cy = [0.299000, 0.587000, 0.114000]
    ci = [0.595716,-0.274453,-0.321263]
    cq = [0.211456,-0.522591, 0.311135]
    r = rgb[0]/255.0
    g = rgb[1]/255.0
    b = rgb[2]/255.0
    e = efv[0]/255.0
    f = efv[1]/255.0
    v = efv[2]/255.0
    ya = cy[0]*r+cy[1]*g+cy[2]*b
    ia = ci[0]*r+ci[1]*g+ci[2]*b
    qa = cq[0]*r+cq[1]*g+cq[2]*b
    yb = cy[0]*e+cy[1]*f+cy[2]*v
    ib = ci[0]*e+ci[1]*f+ci[2]*v
    qb = cq[0]*e+cq[1]*f+cq[2]*v
    if ya>yb:
        yc=ya 
        ic=ia
        qc=qa
    else:
        yc=yb
        ic=ib
        qc=qb
    return [yc,ic,qc]

def if_darker(rgb, efv):
    cy = [0.299000, 0.587000, 0.114000]
    ci = [0.595716,-0.274453,-0.321263]
    cq = [0.211456,-0.522591, 0.311135]
    r = rgb[0]/255.0
    g = rgb[1]/255.0
    b = rgb[2]/255.0
    e = efv[0]/255.0
    f = efv[1]/255.0
    v = efv[2]/255.0
    ya = cy[0]*r+cy[1]*g+cy[2]*b
    ia = ci[0]*r+ci[1]*g+ci[2]*b
    qa = cq[0]*r+cq[1]*g+cq[2]*b
    yb = cy[0]*e+cy[1]*f+cy[2]*v
    ib = ci[0]*e+ci[1]*f+ci[2]*v
    qb = cq[0]*e+cq[1]*f+cq[2]*v
    if ya<yb:
        yc=ya 
        ic=ia
        qc=qa
    else:
        yc=yb
        ic=ib
        qc=qb
    return [yc,ic,qc]


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

def cuasi_suma11():
    
    global imgeopen1
    global imgeopen2
    imgrgb = numpy.asarray(imgeopen1)
    imgrgb2 = numpy.asarray(imgeopen2)
    
    impluspro=[]
    for i in range(len(imgrgb)):
        impluspro.append([])
        for j in range(len(imgrgb[i])):
           impluspro[i].append(plus_pro(imgrgb[i][j],imgrgb2[i][j]))
           
    px2=numpy.array(impluspro, dtype=numpy.uint8)
    img_f= Image.fromarray(px2, 'RGB')
    mostrar(img_f)
    return img_f

def cuasi_suma12():
    global imgeopen1
    global imgeopen2
    imgrgb = numpy.asarray(imgeopen1)
    imgrgb2 = numpy.asarray(imgeopen2)
    
    
    impluscla=[]
    for i in range(len(imgrgb)):
        impluscla.append([])
        for j in range(len(imgrgb[i])):
           impluscla[i].append(plus_clamp(imgrgb[i][j],imgrgb2[i][j]))

    px2=numpy.array(impluscla, dtype=numpy.uint8)
    img_f= Image.fromarray(px2, 'RGB')
    mostrar(img_f)
    return img_f       
def cuasi_suma13():
    
    global imgeopen1
    global imgeopen2
    imgrgb = numpy.asarray(imgeopen1)
    imgrgb2 = numpy.asarray(imgeopen2)
    
    
    plusproyiq=[] 
    for i in range(len(imgrgb)):
        plusproyiq.append([])
        for j in range(len(imgrgb[i])):
            plusproyiq[i].append(pluspro_yiq(imgrgb[i][j],imgrgb2[i][j]))
            
    implusproyiq=[]
    for i in range(len(plusproyiq)):
        implusproyiq.append([])
        for j in range(len(plusproyiq[i])):
            implusproyiq[i].append(yiq_to_rgb(plusproyiq[i][j]))
            
    px2=numpy.array(implusproyiq, dtype=numpy.uint8)
    img_f= Image.fromarray(px2, 'RGB')
    mostrar(img_f)
    return img_f 

def cuasi_suma14():
    global imgeopen1
    global imgeopen2
    imgrgb = numpy.asarray(imgeopen1)
    imgrgb2 = numpy.asarray(imgeopen2)
    
    plusclamyiq=[] 
    for i in range(len(imgrgb)):
        plusclamyiq.append([])
        for j in range(len(imgrgb[i])):
            plusclamyiq[i].append(plusclam_yiq(imgrgb[i][j],imgrgb2[i][j]))
            
    impluscamyiq=[]
    for i in range(len(plusclamyiq)):
        impluscamyiq.append([])
        for j in range(len(plusclamyiq[i])):
            impluscamyiq[i].append(yiq_to_rgb(plusclamyiq[i][j]))
            
    px2=numpy.array(impluscamyiq, dtype=numpy.uint8)
    img_f= Image.fromarray(px2, 'RGB')
    mostrar(img_f)
    return img_f 
def cuasi_resta21():
    
    global imgeopen1
    global imgeopen2
    imgrgb = numpy.asarray(imgeopen1)
    imgrgb2 = numpy.asarray(imgeopen2)
    
    imsubpro=[]
    for i in range(len(imgrgb)):
        imsubpro.append([])
        for j in range(len(imgrgb[i])):
           imsubpro[i].append(subt_pro(imgrgb[i][j],imgrgb2[i][j]))  
    
    px2=numpy.array(imsubpro, dtype=numpy.uint8)
    img_f= Image.fromarray(px2, 'RGB')
    mostrar(img_f)
    return img_f 

def cuasi_resta22():
 
    global imgeopen1
    global imgeopen2
    imgrgb = numpy.asarray(imgeopen1)
    imgrgb2 = numpy.asarray(imgeopen2)
    
    
    imsubcla=[]
    for i in range(len(imgrgb)):
        imsubcla.append([])
        for j in range(len(imgrgb[i])):
           imsubcla[i].append(subt_clamp(imgrgb[i][j],imgrgb2[i][j]))
    
    px2=numpy.array(imsubcla, dtype=numpy.uint8)
    img_f= Image.fromarray(px2, 'RGB')
    mostrar(img_f)
    return img_f 

def cuasi_resta23():
    
    global imgeopen1
    global imgeopen2
    imgrgb = numpy.asarray(imgeopen1)
    imgrgb2 = numpy.asarray(imgeopen2)
    
    
    subtproyiq=[]
    for i in range(len(imgrgb)):
        subtproyiq.append([])
        for j in range(len(imgrgb[i])):
            subtproyiq[i].append(subtpro_yiq(imgrgb[i][j],imgrgb2[i][j]))
            
    imsubproyiq=[]
    for i in range(len(subtproyiq)):
        imsubproyiq.append([])
        for j in range(len(subtproyiq[i])):
            imsubproyiq[i].append(yiq_to_rgb(subtproyiq[i][j]))
    
    px2=numpy.array(imsubproyiq, dtype=numpy.uint8)
    img_f= Image.fromarray(px2, 'RGB')
    mostrar(img_f)
    return img_f 

def cuasi_resta24():
   
    global imgeopen1
    global imgeopen2
    imgrgb = numpy.asarray(imgeopen1)
    imgrgb2 = numpy.asarray(imgeopen2)
    
    
    subtclamyiq=[] 
    for i in range(len(imgrgb)):
        subtclamyiq.append([])
        for j in range(len(imgrgb[i])):
            subtclamyiq[i].append(subtclam_yiq(imgrgb[i][j],imgrgb2[i][j]))
            
    imsubclamyiq=[]
    for i in range(len(subtclamyiq)):
        imsubclamyiq.append([])
        for j in range(len(subtclamyiq[i])):
            imsubclamyiq[i].append(yiq_to_rgb(subtclamyiq[i][j]))
    
    px2=numpy.array(imsubclamyiq, dtype=numpy.uint8)
    img_f= Image.fromarray(px2, 'RGB')
    mostrar(img_f)
    return img_f 

def if_lig():
    global imgeopen1
    global imgeopen2
    imgrgb = numpy.asarray(imgeopen1)
    imgrgb2 = numpy.asarray(imgeopen2)
    
    
    if_ligh=[] 
    for i in range(len(imgrgb)):
        if_ligh.append([])
        for j in range(len(imgrgb[i])):
            if_ligh[i].append(if_lighter(imgrgb[i][j],imgrgb2[i][j]))
            
    imif_lighter=[]
    for i in range(len(if_ligh)):
        imif_lighter.append([])
        for j in range(len(if_ligh[i])):
            imif_lighter[i].append(yiq_to_rgb(if_ligh[i][j])) 
    
    px2=numpy.array(imif_lighter, dtype=numpy.uint8)
    img_f= Image.fromarray(px2, 'RGB')
    mostrar(img_f)
    return img_f 

def if_dar():
    
    global imgeopen1
    global imgeopen2
    imgrgb = numpy.asarray(imgeopen1)
    imgrgb2 = numpy.asarray(imgeopen2)
    
    
    if_dark=[] 
    for i in range(len(imgrgb)):
        if_dark.append([])
        for j in range(len(imgrgb[i])):
            if_dark[i].append(if_darker(imgrgb[i][j],imgrgb2[i][j]))
            
    imif_darker=[]
    for i in range(len(if_dark)):
        imif_darker.append([])
        for j in range(len(if_dark[i])):
            imif_darker[i].append(yiq_to_rgb(if_dark[i][j])) 
    
    px2=numpy.array(imif_darker, dtype=numpy.uint8)
    img_f= Image.fromarray(px2, 'RGB')
    mostrar(img_f)
    return img_f 

imge2= Image.open("tras.png")
imge2 = imge2.resize((300,250))
imgeopen1= None
imgeopen2= None
imgfin=None
window = tk.Tk()
window.title("Arimética de Pixeles")
window.geometry ("920x370")
combo2 = ttk.Combobox(window)
combo2['values']=("Suma","Resta","If-lighter","If-darker")
combo2.set('Suma')
combo= ttk.Combobox(window)
combo['values']=("RGB-Promediado","RGB-Clampeado","YIQ-Promediado", "YIQ-Clampeado")
combo.set('RGB-Promediado')
lblin = tk.Label(window, text = "Operación").grid(column=0, row=3)
lblax = tk.Label(window, text = "Formato").grid(column=1, row=3)
yy= tk.Label(window, text = "")

bcerrar = tk.Button(window, text= "Cerrar", 
                 command = quit)
bapply = tk.Button(window, text= "Aplicar", 
                 command = filtre)
bsave = tk.Button(window, text= "Guardar", 
                 command = save)
bopen1 = tk.Button(window, text= "Abrir imagen 1", 
                 command = open1)
bopen2 = tk.Button(window, text= "Abrir imagen 2", 
                 command = open2)
img2= ImageTk.PhotoImage(imge2)
lblim=tk.Label(window,image=img2)
img3= None
lblim2= tk.Label(window,image=img3)
img4= None
lblim3= tk.Label(window,image=img4)
bcerrar.grid(column=2, row=3)
bapply.grid(column=2, row=1)
bsave.grid(column=2, row=0)
bopen1.grid(column=0, row=1)
bopen2.grid(column=1, row=1)
yy.grid(column=3, row=0)
lblim.grid(column=0, row=2)
lblim2.grid(column=1, row=2)
lblim3.grid(column=2, row=2)
combo.grid(column=1, row=4)
combo2.grid(column=0, row=4)
time2 = time.time()
print ("Demora: ", time2-time1, "segundos")
window.mainloop()

