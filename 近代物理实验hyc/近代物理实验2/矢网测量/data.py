# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 23:11:19 2018

@author: cyc
"""

import matplotlib.pyplot as plt
import math
import numpy as np

lam_c=0.0456
c=3*10**8
l=0.00196

"""以下为读取文件"""

file=open('s11.dat','r')
data=(file.read()).split()
frequency=[]
s11_real=[]
s11_img=[]
s11=[]
for n in range(0,len(data),1):
    if n%3==0:
        frequency.append(data[n])
    elif n%3==1:
        s11_real.append(data[n])
    else:
        s11_img.append(data[n])
for i in range(len(frequency)):
    frequency[i]=float(frequency[i])
    s11_real[i]=float(s11_real[i])
    s11_img[i]=float(s11_img[i])
    s11.append(complex(s11_real[i],s11_img[i]))
file.close()

file=open('s21.dat','r')
data=(file.read()).split()
s21_real=[]
s21_img=[]
s21=[]
for n in range(0,len(data),1):   
    if n%3==1:
        s21_real.append(data[n])
    elif n%3==2:
        s21_img.append(data[n])
for i in range(len(frequency)):
    s21_real[i]=float(s21_real[i])
    s21_img[i]=float(s21_img[i])
    s21.append(complex(s21_real[i],s21_img[i]))
file.close()

file=open('s12.dat','r')
data=(file.read()).split()
s12_real=[]
s12_img=[]
s12=[]
for n in range(0,len(data),1):   
    if n%3==1:
        s12_real.append(data[n])
    elif n%3==2:
        s12_img.append(data[n])
for i in range(len(frequency)):
    s12_real[i]=float(s12_real[i])
    s12_img[i]=float(s12_img[i])
    s12.append(complex(s12_real[i],s12_img[i]))
file.close()

file=open('s22.dat','r')
data=(file.read()).split()
s22_real=[]
s22_img=[]
s22=[]
for n in range(0,len(data),1):   
    if n%3==1:
        s22_real.append(data[n])
    elif n%3==2:
        s22_img.append(data[n])
for i in range(len(frequency)):
    s22_real[i]=float(s22_real[i])
    s22_img[i]=float(s22_img[i])
    s22.append(complex(s22_real[i],s22_img[i]))
file.close()

"""以下为数据处理"""

epsilon_real=[]
epsilon_img=[]
mu_real=[]
mu_img=[]
for i in range(len(frequency)):
    K=((s11[i]**2)-(s21[i]**2)+1)/(s11[i]*2)
    gamma_1=K+(K**2-1)**0.5
    gamma_2=K-(K**2-1)**0.5
    if abs(gamma_1)<=1:
        gamma=gamma_1
    else:
        gamma=gamma_2
    T=(s11[i]+s22[i]-gamma)/(1-(s11[i]+s22[i])*gamma)
    gam=-(math.log((T.real**2+T.imag**2)**0.5)+math.atan(T.imag/T.real)*1j)/l
    lam_0=c/frequency[i]
    temp_1=(1+gamma)/(1-gamma)
    temp_2=(1-(lam_0/lam_c)**2)**0.5
    mu=-(lam_0*gam*temp_1*1j)/(2*math.pi*temp_2)
    epsilon=(-(gam**2)*(0.5*lam_0/math.pi)**2+(lam_0/lam_c)**2)/mu
    epsilon_real.append(epsilon.real)
    epsilon_img.append(epsilon.imag)
    mu_real.append(mu.real)
    mu_img.append(mu.imag)
    
"""作图"""
"""
plt.figure()
a1=plt.scatter(frequency[:],epsilon_img[:],5,"red")
a2=plt.scatter(frequency[:],epsilon_real[:],5,"blue")
plt.xlabel('frequency')
plt.ylabel('epsilon')
plt.legend([a1,a2],['epslion_imag','epslion_real'])
plt.show()
"""
plt.figure()
a1=plt.scatter(frequency[:],mu_img[:],5,"red")
a2=plt.scatter(frequency[:],mu_real[:],5,"blue")
plt.xlabel('frequency')
plt.ylabel('mu')
plt.legend([a1,a2],['mu_imag','mu_real'])
plt.show()