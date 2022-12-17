#아주단순한 구현
def AND(x1,x2):
  w1,w2,theta=.5,.5,.7
  tmp=x1*w1+x2*w2
  if tmp<=theta:
    return 0
  elif tmp>theta:
    return 1
  
AND(1,0)