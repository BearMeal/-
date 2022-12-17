#3층 신경망 구현하기
x= np.array( [1,.5])
w1=np.array([[.1,.3,.5],[.2,.4,.6]])
b1=np.array([.1,.2,.3])

print(w1.shape)
print(x.shape)
print(b1.shape)

a1=np.dot(x,w1) +b1
print(a1)

def sig(x):
  return 1/(1+np.exp(-x))

z1=sig(a1)
print(z1)

print(z1.shape)

w2=np.array([[.1,.4],[.2,.5],[.3,.6]])
b2= np.array([.1,.2])

print(w2.shape)
print(b2.shape)

a2=np.dot(z1,w2) +b2
z2=sig(a2)
print(sig(a2))

#identity_function() 항등함수: 입력을 그대로 출력하는 함수

def i_f(x):
  return x

w3=np.array([[.1,.3],[.2,.4]])
b3=np.array([.1,.2])

a3=np.dot(z2,w3) +b3

y= i_f(a3)

print(y)



