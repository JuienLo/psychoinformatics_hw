#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 17:58:47 2017

@author: JuienLo

1. 用numpy.max()猜測實驗允許之最長反應時間。
2. 剔除無效資料後(RT=-1),由平均正確率和 反應時間猜測 3 實驗條件中,何者最易何者最難
3. 寫一個威力彩號碼產生器。
4. 寫一個 useless program 把自己的視窗關掉。 ( 提示 : pyauto, pyautogui, sikuli, etc.)
"""
import numpy as np

data=np.loadtxt('exp_subj0.txt')
valid=(data[:,2]>0)
data=data[valid,:]
print("實驗允許之最長反應時間為：", np.max(data[:,2]))

Ngroups=np.unique(data[:,0]).size
groups=[0]*Ngroups
for i in range(Ngroups):
    selector=(data[:,0]==i) 
    groups[i]=data[selector,:]

easy=0
hard=0
for i in range(Ngroups):
    if np.mean(groups[i][:,1])<=np.mean(groups[hard][:,1]) and np.mean(groups[i][:,2])>=np.mean(groups[hard][:,2]):
        hard=i
    if np.mean(groups[i][:,1])>=np.mean(groups[easy][:,1]) and np.mean(groups[i][:,2])<=np.mean(groups[easy][:,2]):
        easy=i

print("三個實驗條件中",str(easy),"最易，",str(hard),"最難")

'''
for i in range(Ngroups):
    print(np.mean(groups[i][:,1]),np.mean(groups[i][:,2]))

0.895 0.730734945
0.571428571429 2.20274374534
0.70202020202 1.48642789899
'''