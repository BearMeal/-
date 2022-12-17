# 계단, 시그모드드, 렐루 함수 합친 그래프 그리기
import numpy as np
import matplotlib.pyplot as plt

def sig(x):
  return 1/(1+np.exp(-x))

x= np.arange(-10,10,.1)
y= sig(x)

def sf(x):
  return np.array(x>0,dtype=np.int)

u=sf(x)

def re(x):
  return np.maximum(0,x)

i=re(x)

plt.plot(x,y)
plt.plot(x,u)
plt.plot(x,i)

plt.show()