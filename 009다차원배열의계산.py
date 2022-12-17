#다차원 배열의 계산 
import numpy as np
a= np.array([[1,2],[3,4]])
b= np.array([[4,3],[2,1]])

print(a*b)
print(np.dot(a,b)) #행렬 내적구하기 dot()메서드 