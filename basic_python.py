# -*- coding: utf-8 -*-
import time, random
t=0;
for i in range(1,4):
    print("Get ready...",flush=True)
    time.sleep(5+5*random.random())
    t0=time.time()
    input("Press [Enter] Now!")
    t1=time.time()-t0
    t+=t1;
    i=i+1
t=t1/3
print(t)
