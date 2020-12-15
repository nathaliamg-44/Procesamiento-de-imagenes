# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 10:01:50 2020

@author: na_th
"""

import tkinter as tk
from tkinter import ttk
import numpy as np
from PIL import Image, ImageTk
from tkinter import filedialog
import cv2

#MOSTRAR IMAGEN EN ESCALA GRISES Y SU ESPECTRO DE FRECUENCIA
#cv2.imshow("IMAGEN ORIGINAL",i_gray)
#cv2.imshow("ESPECTRO DE FOURIER",np.uint8(255*Fuv_log/np.max(Fuv_log)))


def tf():
    global file_name
    global img3
    imagen= cv2.imread(file_name)
    imagen=cv2.resize(imagen,(300,250))
    i_gray = np.asarray(imagen)
    i_gray=cv2.cvtColor(i_gray,cv2.COLOR_RGB2GRAY)
    i_grayd=np.float64(i_gray) 
    Fuv=np.fft.fft2(i_grayd)
    Fuv=np.fft.fftshift(Fuv)
    Fuv_abs=np.abs(Fuv)
    Fuv_log=20*np.log(Fuv_abs)
    espe= np.uint8(255*Fuv_log/np.max(Fuv_log))
    img = Image.fromarray(espe)
    img3=ImageTk.PhotoImage(img)
    lblim2.config(image=img3)
    
def tfin():
    global filename1
    global img2
    imagen = Image.open(filename1)
    imagen =imagen.resize((300,250))
    Guv = np.asarray(imagen)
    gxy=np.fft.ifft2(Guv)
    gxy=np.abs(gxy)
    gxy=np.uint8(gxy)
    img = Image.fromarray(gxy)
    img2=ImageTk.PhotoImage(img)
    lblim.config(image=img2)
    
def open1():
    global img2
    global imgeopen1
    global file_name
    file_name=filedialog.askopenfilename(title='UpLoad', filetypes=[('PNG FILES', '*.png')])   
    imgeopen1= Image.open(file_name)
    imgeopen1 =imgeopen1.resize((300,250))
    img2=ImageTk.PhotoImage(imgeopen1)
    lblim.config(image=img2) 
    return file_name

def open2():
    global img3
    global imgeopen2
    global filename1
    filename1=filedialog.askopenfilename(title='UpLoad', filetypes=[('PNG FILES', '*.png')])   
    imgeopen2= Image.open(filename1)
    imgeopen2 =imgeopen2.resize((300,250))
    img3=ImageTk.PhotoImage(imgeopen2)
    lblim2.config(image=img3)  
    
def save():
    global img2
    file_name=filedialog.asksaveasfilename(title='UpLoad', filetypes=[('PNG FILES', '.png')])
    img2.save(str(file_name)+ '.png', 'PNG')
    print(file_name)
    
def quit():
    window.destroy()    

imge2= Image.open("tras.png")
imge2 = imge2.resize((300,250))
imgeopen1= None
imgeopen2= None
imgfin=None
window = tk.Tk()
window.title("Transformada de Fourier")
window.geometry ("920x370")
#lbl = tk.Label(window, text = "Original").grid(column=0, row=1)
#lbl2 = tk.Label(window, text = "Nueva").grid(column=1, row=1)
lblin = tk.Label(window, text = "Operación").grid(column=0, row=3)
lblax = tk.Label(window, text = "Formato").grid(column=1, row=3)
yy= tk.Label(window, text = "")
#txt1= tk.Entry(window,   width = 7)
#txt1.insert(0,"0.2")
#txt2= tk.Entry(window, width = 7) 
#txt2.insert(0,"0.8")
bcerrar = tk.Button(window, text= "Cerrar", 
                 command = quit)
btf = tk.Button(window, text= "Transformada de Fourier", 
                 command = tf)
btfin= tk.Button(window, text= "Transformada Inversa", 
                command = tfin)
bopen1 = tk.Button(window, text= "Abrir imagen 1", 
                 command = open1)
bopen2 = tk.Button(window, text= "Abrir imagen 2", 
                 command = open2)
bsave = tk.Button(window, text= "Guardar", 
                 command = save)
img2= ImageTk.PhotoImage(imge2)
lblim=tk.Label(window,image=img2)
img3= None
lblim2= tk.Label(window,image=img3)
img4= None
lblim3= tk.Label(window,image=img4)
bcerrar.grid(column=2, row=4)
btf.grid(column=2, row=1)
btfin.grid(column=2, row=3)
bopen1.grid(column=0, row=1)
bopen2.grid(column=1, row=1)
bsave.grid(column=1, row=4)
#txt1.grid(column= 1, row =3)
#txt2.grid(column= 1, row =4)
yy.grid(column=3, row=0)
lblim.grid(column=0, row=2)
lblim2.grid(column=1, row=2)
lblim3.grid(column=2, row=2)

window.mainloop()