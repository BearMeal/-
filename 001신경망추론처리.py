#신경망 추론 처리
#데이터셋을 가지고 신경망을 구현한다
#입력층 뉴련 784개, 출력층 뉴련 10개,
#입력층이 784인 이유는 28*28=784 이고 출력층은 10개로 분류하기 떄문
#1번 은닉층 50개, 2번 은닉층100개 뉴런배치 


import sys, os
sys.path.append('/content/drive/MyDrive/Colab Notebooks')
import numpy as np
from dataset.mnist import load_mnist
import pickle

def sm(x):
  c=np.max(x)
  return np.exp(x-c)/np.sum(np.exp(x-c))

def sig(x):
  return  1/(np.exp(-x))


def get_data():
  (x_train,t_train),(x_test,t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=False)
  return x_test,t_test

def init_network():
  with open("/content/drive/MyDrive/Colab Notebooks/dataset/sample_weight.pkl",'rb') as f:
    network = pickle.load(f)

  return network

def predict(network,x):
  W1,W2,W3= network['W1'],network['W2'],network['W3']
  b1,b2,b3= network['b1'],network['b2'],network['b3']

  a1 =np.dot(x,W1) +b1
  z1= sig(a1)
  a2= np.dot(z1,W2) + b2
  z2= sig(a2) 
  a3=np.dot(z2,W3) + b3
  y=sm(a3)

  return y

x,t= get_data()
network = init_network()

accuracy_cnt = 0
for i in range(len(x)):
  y= predict(network,x[i])
  p= np.argmax(y) #확률이 가장 높은 원소의 인덱스를 얻는다.
  if p == t[i]:
    accuracy_cnt +=1

print('Accuracy:'+str(float(accuracy_cnt)/len(x)))