import numpy as np 
x= np.array([-1., 1.,2.])

y=x>0

y=y.astype(np.int)  #넘파이 배열을 부등호를 써서나누고 그값들은 불리언 자료형이 되는데
# 이떄 그 불리언 자료형을 가진 y배열을 np.int으로 형변환한다
y

#astype(np.int) 넘파이의 애즈타입 메서드 : 불리언 자료형 True =1 False=0 으로 바꿔준다