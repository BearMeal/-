#퍼셉트론의 한계 XOR게이트 불가

#도전 XOR게이트!(배타적 논리합이라는 논리회로,한쪽이 1일때만 1출력)
#선형적인 특성상 그래프상에서 배타적 논리합을 만들수없다 => 비선형적인그래프를 그리면 가능하다

#다층 펴셉트론은 아름답다 
#AND NAND OR트게이트를 조합하여 XOR게이트를 만든다.



def AND(x1,x2):
  x=np.array([x1,x2])
  w=np.array([.5,.5])
  b= -.7

  tmp=np.sum(w*x) +b
  if tmp <= 0:
    return 0
  elif tmp >0:
    return 1

def NAND(x1,x2):
  x=np.array([x1,x2])
  w=np.array([-.5,-.5])
  b=.7

  tmp=np.sum(w*x)+b

  if tmp<=0:
    return 0
  elif tmp>0:
    return 1

def OR(x1,x2):
  x=np.array([x1,x2])
  w=np.array([.5,.5])
  b=-.2
  tmp=np.sum(w*x)+ b

  if tmp <=0:
    return 0
  elif tmp >0:
    return 1


def XOR(x1,x2):
  s1=NAND(x1,x2)
  s2=OR(x1,x2)
  y=AND(s1,s2)
  return y

print(XOR(1,0)