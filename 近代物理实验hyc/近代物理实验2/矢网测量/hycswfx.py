# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 00:02:06 2021

@author: hyc
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from scipy import constants as const

os.chdir('C:\\Users\\hyc\\Desktop\\近代物理实验2\\矢网测量')

#实验数据

lam_c=0.014
c=const.c
l=0.002
pi=const.pi

#读取非标准格式csv文件
df11=pd.read_csv(r"C:\Users\hyc\Desktop\近代物理实验2\矢网测量\s11.csv",\
                 sep=r"\s+", engine='python')
df12=pd.read_csv(r"C:\Users\hyc\Desktop\近代物理实验2\矢网测量\s12.csv",\
                 sep=r"\s+", engine='python')
df21=pd.read_csv(r"C:\Users\hyc\Desktop\近代物理实验2\矢网测量\s21.csv",\
                 sep=r"\s+", engine='python')
df22=pd.read_csv(r"C:\Users\hyc\Desktop\近代物理实验2\矢网测量\s22.csv",\
                 sep=r"\s+", engine='python')

#原始数据s**虚/实值-频率关系图
ax=df11.plot(x='Frequency',y=['Real','Image'], title=r'$s_{11}$') 
fig = ax.get_figure()
fig.savefig('s11.svg')

ax=df12.plot(x='Frequency',y=['Real','Image'], title=r'$s_{12}$') 
fig = ax.get_figure()
fig.savefig('s12.svg')

ax=df21.plot(x='Frequency',y=['Real','Image'] , title=r'$s_{21}$') 
fig = ax.get_figure()
fig.savefig('s21.svg')

ax=df22.plot(x='Frequency',y=['Real','Image'], title=r'$s_{22}$') 
fig = ax.get_figure()
fig.savefig('s22.svg')

#代入公式计算
Frequency=df11['Frequency'].values  #每组数据对应的频率记录都一样
lambda_0=c/Frequency  #空气中的工作波长
s11=df11['Real'].values + 1j*df11['Image'].values
s12=df12['Real'].values + 1j*df12['Image'].values
s21=df21['Real'].values + 1j*df21['Image'].values
s22=df22['Real'].values + 1j*df22['Image'].values

#将s11，s22和s12，s21取平均
s11=(s11+s22)/2
s21=(s12+s21)/2

##########################################
K=(s11**2-s21**2+1)/(s11*2)


gamma_1=K+(K**2-1)**0.5
gamma_2=K-(K**2-1)**0.5
gamma=[]
len_temp=gamma_1.size
for i in range(len_temp):
    if(np.abs(gamma_1[i])<1):
        gamma.append(gamma_1[i])
    else:
        gamma.append(gamma_2[i])
gamma=np.array(gamma)

Tl=s21/(1-gamma*s11)

#np.angle()返回弧度制
# gamma_prop_const=-(np.log(np.abs(Tl))+np.angle(Tl)*1j)/l #传播常数
Lam_squared= -(-np.log(Tl)/(2*pi*l))**2
Lam=[]
for i in Lam_squared :
    Lam_temp=np.sqrt(i)
    if Lam_temp.real>0:
        Lam.append(Lam_temp)
    else:
        Lam.append(-Lam_temp)

lam_c_t=1/lam_c**2
mu=(1+gamma)*Lam/((1-gamma)*np.sqrt(1/lambda_0**2-lam_c_t))
epsilon=(Lam_squared+lam_c_t)*lambda_0**2/mu



#介电常数/磁导率-频率曲线图

plt.clf()
plt.plot(Frequency, epsilon.real)
plt.xlabel(r'Frequency/Hz', fontdict={'size':'medium'})
plt.ylabel(r'$Re\{\epsilon_r\}$',fontdict={'size':'medium'})
plt.savefig('epsilonRe.svg')

plt.clf()
plt.plot(Frequency, epsilon.imag)
plt.xlabel(r'Frequency/Hz', fontdict={'size':'medium'})
plt.ylabel(r'$Im\{\epsilon_r\}$',fontdict={'size':'medium'})
plt.savefig('epsilonIm.svg')

plt.clf()
plt.plot(Frequency, mu.real)
plt.xlabel(r'Frequency/Hz', fontdict={'size':'medium'})
plt.ylabel(r'$Re\{\mu_r\}$',fontdict={'size':'medium'})
plt.savefig('muRe.svg')

plt.clf()
plt.plot(Frequency, mu.imag)
plt.xlabel(r'Frequency/Hz', fontdict={'size':'medium'})
plt.ylabel(r'$Im\{\mu_r\}$',fontdict={'size':'medium'})
plt.savefig('muIm.svg')