#NAND와 OR게이트를 구현한다

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

print(NAND(1,0))
print(NAND(0,1))
print(NAND(1,0))
print(NAND(1,1))

print(OR(0,1))
print(OR(0,0))
print(OR(1,0))
print(OR(1,1))


'''
     가중치 편향
AND   +    -(가중치보다 큼)
NAND  -    +
OR    +    -(가중치보다 작음) 
'''