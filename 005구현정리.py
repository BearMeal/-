# 구현정리
def sig(x):
  return 1/(1+np.exp(-x))

def init_network():
  network={}
  network['w1']= np.array([[.1,.3,.5],[.2,.4,.6]])
  network['b1']=np.array([.1,.2,.3])
  network['w2']=np.array([[.1,.4],[.2,.5],[.3,.6]])
  network['b2']=np.array([.1,.2])
  network['w3']=np.array([[.1,.3],[.2,.4]])
  network['b3']=np.array([.1,.2])

  return network

def forward(network,x):
  w1,w2,w3= network['w1'],network['w2'],network['w3']
  b1,b2,b3= network['b1'],network['b2'],network['b3']

  a1=np.dot(x,w1)+b1
  z1=sig(a1)
  a2=np.dot(z1,w2)+ b2
  z2=sig(a2)
  a3=np.dot(z2,w3)+b3
  y= a3

  return y

network= init_network()

x=np.array([1,.5])
y=forward(network,x)

print(y)
