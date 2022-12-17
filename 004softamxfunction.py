#소프트 맥스 함수의 특징 
#소맥함수를 이용하면 신경망 출력을 다음과 같이 계산 가능

def sf(a):
  c=np.max(a)
  y=np.exp(a-c)/np.sum(np.exp(a-c))
  return y
a= np.array([.3,2.9,4.,5,.6])
y= sf(a)
print(y)
np.sum(y)  # 출력값의 모든 합이 1이됨을 알수있다.

#신경망 학습과정에서 출력층에 소맥함수를 사용하나, 추론의 과정(현업)에서는 생략한다.

#위를 기준으로 함수를 다시 구현한다.
def sf(a):
  c=np.max(a)
  ea=np.exp(a-c)
  sumea=np.sum(ea)
  y=ea/sumea
  return y

x=np.arange(-5,5,.1)
y=sf(x)

plt.plot(x,y)
plt.show()

#오버플로우 방지하기
a= np.array([1010,1000,990])
print(np.exp(a)/np.sum(np.exp(a)))
#nan 이 나온다. 제대로 계산되지 않는다.

c= np.max(a) #넘파이 배열에서의 최대값을 임의의 상수로 둔다
print(a-c)

print(np.exp(a-c)/np.sum(np.exp(a-c)))
# 상수를 빼준값을 취하면 제대로 나온다


#소프트맥스 함수 함수로 구현해놓기

import matplotlib.pyplot as plt
def sm(a):
  ea=np.exp(a)
  sumea=np.sum(ea)
  y=ea/sumea
  return y

x=np.arange(-6,10,.1)
y=sm(x)

plt.plot(x,y)
plt.show()
