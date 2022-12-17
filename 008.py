import numpy as np

a=np.array([[1,2],[3,4],[5,6]])
print(a.shape)

b=np.array([[7,8],[9,8]])
print(b.shape)


print(np.dot(a,b))