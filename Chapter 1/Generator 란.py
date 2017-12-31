# 먼저 Iterator 의 개념을 알아보자

# a = [0, 1, 2, 3, 4, 5]
# 여기서 a 는 list 의 형태이다 .

# b = iter(a)
# 그렇다면 여기서 b는 무슨 형태일까?
# print(b)
# <list_iterator object at 0x001F93D0>
# b를 print 하게 되면 iterator 라는 메시지가 출력되는데
# 즉, list iterator 객체가 0x001F93D0 라는 메모리 주소에 위치한다는 것을 말해준다.
# 공간 = iter(리스트) 라는 것으로 iterator 를 생성할 수 있다.

# iterator 를 생성하고 next()라는 함수를 사용하면
# c = iter(range(6))
# print(c)
# print(c.__next__())
# print(c.__next__())
# print(c.__next__())
# print(c.__next__())
# print(c.__next__())
# print(c.__next__())
# 똑같이 c.__next__() 라고 명령을 반복해서 주고 있는데 매번 출력되는 값들이 변화됨
# 자세히 보면 iterator 로 옮겨져 저장된 값들이 호출될 때마다 순차적으로 추출
# 이 것을 iteration(반복) 이라고 함

# Iterator : 명시된 공간 'b' or 'c' 가 Iterator
# Iteration : Iterator b로부터 순차적으로 요소를 가져오는 행위를 말함
# iterable : iteration 이 가능하다는 의미

# 그렇다면 List 는 iterator 일까 아닐까?
# list 는 iterator는 아니지만, iterable 하다.

# list = [0,1,2,3,4,5]
# list.__next__() # 에러 뜸
#
# for i in list:
#     print(i) # 하나씩 뽑아냄
# 이것을 봐서 list는 iterable하고 iteration 이 가능하다라고 알수있음
# 그렇다면 generator는(생성기)는?

def num_generator(n):
    print("Generator Start!!")
    while n < 3:
        print("Generator : I give control to the Main.")
        yield n
        print("Generator : I received a control")
        n +=1
        print("Generator : n+=1")
    print("Generator End!!")

for i in num_generator(0):
    print("Main : I received a control.")
    print(i)
    print("Main : I give control to the Generator")
