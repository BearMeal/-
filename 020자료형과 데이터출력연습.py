#파이썬 의 자료형 type()

print(type(12),
type(1.42),
type('heelo'))

#int 정수 float 실수 str 문자열 클래스는 자료형 
'''
a = [1, 2, 3, 4, 5]

print(len(a))
a[3]=50
print(a) #a의 길이와 a의 4번째르 50으로 바꿈
'''

#리스트 슬라이싱 
'''
a[1:5]
a[2:]
a[:4]
print(a[:-1]) #뒤에서 까지 첫번째 출력
'''
#딕셔너리

me={'height':180} #키를 딕셔에리에 추가, key and value 값이다.
me['height']  #딕셔너리에 접근 
me['weight']=67 # 딕셔너리에 추가

print(me) # 딕셔너리에 추가됨을 확인


# bool 불리언 자료형, True, False 나타냄  , and or not 사용가능

hungry =True
sleepy= False
print(type(hungry))
print(not hungry)

print(hungry and sleepy)
print(hungry or sleepy)

# if  조건문 
if hungry:
  print('i\'m hungry')

else:
  print('sleepy')

#for 반복문 
'''
for i in range(4):
  print(i,end='')
'''
#함수 function 특정 기능을 수행하는 일련의 명령들을 묶어 하나의 함수(function)로 정의
'''
def hello():
  print('hello world!')

hello()
'''

def hello(obje):    # 함수안에자인자를 넣을수 있음
  print('hello'+obje)

hello('cat')

#새로운 클래스(자료형) 만들기, 새로운 함수(메서드) 만들수있음
# 이해안됨 패스

'''
class kimchi :
  def __init__(self,name):
    self.name=name
    print('initialized')
  def hi(self):
    print('hello'+self.name)
  def bye(self):
    print('bye'+self.name)

m= kimchi('dad')

m.hi()
m.bye()

'''
#넘파이 가져오기 
#넘파이라이브러리에서 함수(메서드)를 가져와 사용할 수 있다.

#import numpy as np

#넘파이 배열 생성하기 
'''
x= np.array([1.0,2.0,3.0])  # 파이썬의 리스트형태를 인수로 받아 넘파이의 특별한 배열로 반환함, 자료형이 특이함 
print(x)
print(type(x)) #numpy.ndarray 라는 클래스(자료형이 됨)
'''

#넘파이 배열로 산술연산 
'''
x=np.array([1,2,3])
y=np.array([2,4,6])

print(x+y) #넘파이 배열 자료형의 결과가 나온다 원소별 곱셈
print(x/2) #이것도 가능                 브로드캐스트기능 연산  
'''

#넘파이의 다차원 배열 한줄 뿐만아니라 여러줄이 가능하다
'''
A = np.array([[2,3],[4,5]])
print(A)
print(A.shape)  # A 넘파이 배열의 행렬구조이다.
print(A.dtype)  # A 원소의 자료형 
'''
#행렬의 연산
'''
B=np.array([[3,0],[0,6]])

print(A+B);print(A*B)
'''
#주석 수학에서 1차원 배열을 벡터, 2차원 배열을 행렬(matrix), 벡터와 행렬을 일반화 한것을 텐서라고 함

#넘파이 배열에서의 원소 접근 
'''
X = np.array([[51, 55], [14, 19], [0, 4]])
print(X)

print(X[2][1]) #X의 3행 2열 =4

for i in X:
  print(i)      # 한차원의 배열=벡터 로 뽑는다.

X=X.flatten()  # 다차원 배열을 일차원 배열로 평탄화해서 뽑아줄수있다.
print(X)  
print(X[1],X[-2])

print(X[X>15])
'''

#matplotlib떼이터 시각화 및 그래프 그리기
#단순한 그래프를 그려보기

#import numpy as np
#import matplotlib.pyplot as plt #matplotlib의 pyplot 모듈ㄹ 사용한다.

#데이터 준비
'''
x= np.arange(0,50,.1) # 0에서 6까지 0.1간격으로
y=np.sin(x)

plt.plot(x,y) #그래프에 x와y값을 넣는다
plt.show() #그래를 보인다.
'''

#import numpy as np
#import matplotlib.pyplot as plt
'''
#데이터 준비
x=np.arange(0,40,.1)
y1=np.sin(x)
y2=np.cos(x)

#그래프 그리기
plt.plot(x,y1,label='SIN')  #그래프에 들어갈 데이터+ 그 선의 이름
plt.plot(x,y2,label='COS')
plt.xlabel('period')   # x축의 이름
plt.ylabel('height')   # y축의 이름
plt.title('SIN&COS')   # 그래프의 제목
plt.legend()           # 데이터값 선의 범례를 그래위에 표시하기
plt.show()
'''


#이미지 표시하기
#pyplot의 메서드 imshow()를 사용해서 이미지를 표시
#matplotlib.image의 모듈의 imread()메서드 사용해서 읽어온다
 
import matplotlib.pyplot as plt
from matplotlib.image import imread	

img = imread('/content/drive/MyDrive/kong.jpg')

plt.imshow(img)
plt.show()