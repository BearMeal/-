import sys, os
sys.path.append('/content/drive/MyDrive/Colab Notebooks') #부모 디렉토리에서 어떤 파일을 가져오게 설정
from dataset.mnist import load_mnist #부모 디렉토리의 아래 dataset 폴더에서 mnist파일을 가져올수 있도록 설정하고 
#dataset/mnist.py의 load_mnist 함수를 임포트해온다 


#처음엔 좀 걸림
(x_train,t_train),(x_test,t_test)= load_mnist(flatten=True, normalize=False)
#그런다음 load_mnist 함수로 mnist 데이터셋을 읽는다

#load_mnist함수는 읽은 데이터를 (훈련이미지,훈련레이블 ),(시험이미지,시험레이블) 형식으로 반환한다.

#각 데이터의 형상 출력 
print(x_train.shape)
print(t_train.shape)
print(x_test.shape)
print(t_test.shape)