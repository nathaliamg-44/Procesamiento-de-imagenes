# -*- coding: utf-8 -*-
"""
Editor de Spyder


@author: na_th
"""
from PIL import Image
import numpy

def in_range(num, mi, ma):
    if num > ma:
        return ma
    elif num < mi:
        return mi
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

def yiq_luminance(yiq):
    a = 1.5
    y1 = yiq[0]
    i1 = yiq[1]
    q1 = yiq[2]
    py = in_range(y1 * a, 0, 1)
    pi = in_range(i1, -0.5957, 0.5957)
    pq = in_range(q1, -0.5226, 0.5226)
    return [py,pi,pq]

def yiq_saturacion(yiq):
    b = 1.5
    y1 = yiq[0]
    i1 = yiq[1]
    q1 = yiq[2]
    py = in_range(y1, 0, 1)
    pi = in_range(i1 * b, -0.5957, 0.5957)
    pq = in_range(q1 * b, -0.5226, 0.5226)
    return [py,pi,pq]

def yiq_lumi_satu(yiq):
    a = 2.5
    b = 2
    y1 = yiq[0]
    i1 = yiq[1]
    q1 = yiq[2]
    py = in_range(y1 * a, 0, 1)
    pi = in_range(i1 * b, -0.5957, 0.5957)
    pq = in_range(q1 * b, -0.5226, 0.5226)
    return [py,pi,pq]
    

#ruta= "C:/Users/na_th/Documents/tigre.jpg"
ruta = "C:/Users/na_th/Documents/Maptemp.jpg"
imag= Image.open(ruta)
imgrgb = numpy.asarray(imag)

rgb = [155, 30, 200]
yiq = rgb_to_yiq(rgb)
yiq2 = yiq_saturacion(yiq)
rgb2 = yiq_to_rgb(yiq2)
print(rgb, yiq, yiq2, rgb2)


imgyiq=[]
for i in range(len(imgrgb)):
    imgyiq.append([])
    for j in range(len(imgrgb[i])):
        imgyiq[i].append(rgb_to_yiq(imgrgb[i][j]))

imgrb=[]
for i in range(len(imgyiq)):
    imgrb.append([])
    for j in range(len(imgyiq[i])):
        imgrb[i].append(yiq_to_rgb(imgyiq[i][j]))

imgyiq2=[]
for i in range(len(imgyiq)):
    imgyiq2.append([])
    for j in range(len(imgyiq[i])):
        imgyiq2[i].append(yiq_lumi_satu(imgyiq[i][j]))

imgrgb2=[]
for i in range(len(imgyiq2)):
    imgrgb2.append([])
    for j in range(len(imgyiq2[i])):
        imgrgb2[i].append(yiq_to_rgb(imgyiq2[i][j]))

px2=numpy.array(imgrgb2, dtype=numpy.uint8)
img2 = Image.fromarray(px2, 'RGB')
img2.save("C:/Users/na_th/Documents/n.jpg","JPEG")
#imag.show()
img2.show()


