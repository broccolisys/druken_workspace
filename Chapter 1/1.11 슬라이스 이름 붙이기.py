"""1.11 슬라이스 이름 붙이기
프로그램 코드에 슬라이스를 지시하는 하드코딩이 너무 많아 이해하기 어려운 상황일때
정리하고자 할 경우"""

# example 1, 내장 함수인 slice() 는 슬라이스 받는 모든 곳에 사용할 수 있는 조각을 생성한다

# items = [0, 1, 2, 3, 4, 5, 6]
# a = slice(2, 4)
# b = items[2:4]
# print(b) # [2, 3]
# c = items[a]
# print(c) # [2, 3]
# items[a] = [10, 11]
# print(items) # [0, 1, 10, 11, 4, 5, 6]
# del items[a]
# print(items) # [0, 1, 4, 5, 6]

# example 2, indices(size) 메소드를 사용하면, 특정 크기의 시퀀스를 슬라이스 매핑할 수 있다.
# tuple(start,stop,step)을 반환하는데, 모든 값은 경계를 넘지 않도록 제약이 걸려있다.
a = slice(10, 50, 2)
s = 'HelloWorld'
print(a.indices(len(s)))

for i in range(*a.indices(len(s))):
    print(s[i])

pyString = 'Python'
s0bject = slice(3)
print(pyString[s0bject])
s0bject2 = slice(1, 5, 2)
print(pyString[s0bject2])