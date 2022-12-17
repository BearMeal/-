#렐루 함수 (Rectified Linear Unit)
#0 을 넘으면 그대로 출력하고 본지는 0으로 출력

def re(x):
  return np.maximum(0,x) 

#넘파이의 맥시멈함수는 두입력중 큰수만 출력하는 함수