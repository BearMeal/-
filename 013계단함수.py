#계단함수의 그래프를 그려본다 

import numpy as np
import matplotlib.pylab as plt #파이랩 모듈?? pyplot과 유사한기능임 없어질기능

def step_function(x):
  return np.array(x>0,dtype=np.int)

x=np.arange(-5.,5.,.1) #넘파이 배열 생성 -5부터 5까지 .1 간격으로 
y=step_function(x)
plt.plot(x,y)
plt.ylim(-1,2)
plt.show()