"""1.9 두 딕셔너리이 유사점 찾기
두 딕셔너리가 있고 여기서 유사점을 찾고 싶다 (동일한 키, 동일한 값)등"""

# example 1

a = {
    'x' : 1,
    'y' : 2,
    'z' : 3,
}

b = {
    'w' : 10,
    'x' : 11,
    'y' : 2
}

# 동일한 키 찾기
print(a.keys() & b.keys())

# a에만 있고 b에는 없는 키 찾기
print(a.keys() - b.keys())

# (키, 값)이 동일한 것 찾기
print(a.items() & b.items())

# 특정 키를 제거한 새로운 딕셔너리 만들기
c = {key:a[key] for key in a.keys() - {'z','w'}}
print(c) # {'x': 1, 'y': 2}