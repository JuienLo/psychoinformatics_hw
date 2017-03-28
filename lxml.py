#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
1. index.html 右上角 [< 上頁 ] 中包含了總頁數資訊,
請用 LXML 抓出此經常變動的數字。

2. 請用 LXML 找出 index.html 中 [ 爆 ]文的標題與 URN 。

3. 請用 Selenium 在 index.html 往前翻三頁並拍照。

"""
import urllib, lxml.html, re
URL='http://www.ptt.cc'
URN='/bbs/Boy-Girl/index.html'
h={'User-Agent':'Mozilla/5.0'}
r=urllib.request.Request(URL+URN,headers=h)
data=urllib.request.urlopen(r).read()
t=lxml.html.fromstring(data.decode('utf-8'))
x=t.xpath('//a[contains(text(),"‹ 上頁")]')[0]
x=x.attrib.get('href')
x=re.findall('.([0-9]+).',x)
print("總頁數為：",x[0])

y=t.xpath('.//span[contains(text(),"爆")]')[0]
y=y.getparent().getnext().getnext().getchildren()
print("爆的標題為：",y[0].text,"\nURN為：",y[0].attrib.get('href'))

from selenium import webdriver 
URI='https://www.ptt.cc/bbs/Boy-Girl/index.html' 
driver=webdriver.Chrome() # Chrome, PhantomJS, etc. 
driver.get(URI)
driver.save_screenshot('before_click.png')
for i in range(3):
    btn=driver.find_element_by_link_text('‹ 上頁') 
    btn.click()
driver.save_screenshot('after_click.png')

"""
w4
"""
from psychopy import core,visual,event
import numpy as np
words=np.loadtxt('words.txt',dtype='string')
animals=words[:5]
aran=np.random.choice(animals,3,replace=False)
stuff=words[5:]
sran=np.random.choice(stuff,3,replace=False)
total=np.concatenate((aran,sran))
corAns=np.array(['y']*3+['n']*3)
ACC=np.array([]); RT=np.array([])
w=visual.Window(size=[800,600])
for i in range(2):
  keys=np.array([])
  trials=np.random.permutation(range(len(total)))
  for j in trials:
    core.wait(1)
    visual.TextStim(w,text=total[j],height=.5).draw()
    w.flip(); core.wait(0.2); w.flip()
    r=event.waitKeys(keyList=["y","n"],timeStamped=True)
    keys=np.append(keys,r[0][0]); RT=np.append(RT,r[0][1])
  ACC=np.append(ACC,keys==corAns[trials])
np.savetxt('data.txt',np.vstack([ACC,RT]).T,['%d','%f'])
