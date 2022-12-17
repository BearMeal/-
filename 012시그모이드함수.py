#시그모이드 함수 그려보기
import numpy as np
def sig(x):
  return 1/(1+np.exp(-x))  #시그모이드함수를 파이썬으로 표현하이음, 넘파이배열 처리가능

x=np.arange(-50,50,.1)
y=sig(x)


import matplotlib.pyplot as plt 

def sf(a):
  return np.array(a>0,dtype=np.int)

a= x
b=sf(a)*3


plt.plot(x,y)
plt.plot(a,b)
plt.show()