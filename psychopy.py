
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