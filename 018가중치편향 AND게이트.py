#가중치와 편향을 도입한 AND 게이트

def AND(x1,x2):
  x=np.array([x1,x2])
  w=np.array([.5,.5])
  b= -.7

  tmp=np.sum(w*x) +b
  if tmp <= 0:
    return 0
  elif tmp >0:
    return 1

print(AND(0,1))
print(AND(0,0))
print(AND(1,0))
print(AND(1,1))

## 가중치는 입력신호가 얼마나 중요한지 중요도의 기능, 편향은 뉴련이 얼마나 쉽게 활성화 되는지 조정하는 매개변수



#가중치와 편향을 도입한다
import numpy as np
x=np.array([0,1])
w=np.array([.5,.5])  #가중치
b=-.7           #편향

print(w*x)    #가중치를 적용한다

ns=np.sum(w*x)   #가중치가 곱해진 배열의 모든 원소값을 더한다  

print(ns+b)      #모든 더해진 원소값에 편향을 더한다