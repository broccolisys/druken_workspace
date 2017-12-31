""" 1.1 시퀀스를 개별 변수로 나누기
N개의 요소를 가진 tuple 이나 sequence 가 있다. 이를 변수 N개로 나뉘어야 한다.
모든 sequence(or can iterating)는 간단한 할당문을 사용해서 개별 변수로 나눌 수 있다.
단 주의해야 할 것은 변수의 개수 =sequence 에 일치
"""
p = (4,5)
x,y = p
print(x)
print(y)

# Unpacking 은 사실 tuple, list 뿐만 아니라 순환 가능한 모든 객체에 적용할 수 있다.
# 여기에는 문자열, 파일, iterator, generator 가 포함된다

s = 'Hello'
a,b,c,d,e = s
print(a)
print(b)
print(e)

# Unpacking 할때 특정 값을 무시하는 방법도 있다. 즉 단순히 버릴 변수명을 지정할 수 있다.

data = ['ACME', 50, 91.1, (2012, 12, 21)]
_, shares, price, _ = data
print(shares)
print(price)