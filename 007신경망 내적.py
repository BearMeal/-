#신경망의 내적
#편향과 활성화 함수를 생략하고 가중치만 갖는다
#행렬의 곱으로 신경만의 계산을 수행한다

x= np.array([1,2])
print(x)
print(x.shape)
w=np.array([[1,3,5],[2,4,6]])
print( w)
print(w.shape)
y=np.dot(x,w)
print(y)