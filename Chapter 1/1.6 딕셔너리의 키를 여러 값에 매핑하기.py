"""1.6 딕셔너리의 키를 여러 값에 매핑하기
딕셔너리의 키를 하나 이상의 값에 매핑하고 싶다(소위 "multidict"라 불린다).
하나의 키에 하나의 값이 매핑되어 있는 것을 딕셔너리라 부른다.
키에 여러값을 매핑하려면, 그 여러 값을 리스트나 세트와 같은 컨테이너에 따로 저장해야한다.
"""
from collections import defaultdict

# example 1

d = {
    'a':[1, 2, 3],
    'b':[4, 5]
}


e = {
    'a':{1, 2, 3},
    'b':{4, 5}
}

# 딕셔너리를 쉽게 만들기 위해서 collections 모듈의 defaultdict 를 사용한다.
# defaultdict의 기능 중에는 첫 번째 값을 자동으로 초기화 하는 기능이 있어서
# 사용자는 아이템 추가에만 집중할 수 있다.

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

# print(d)
# defaultdict(<class 'list'>, {'a': [1, 2], 'b': [4]})

# set 인 경우
d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
# print(d)
# defaultdict(<class 'set'>, {'a': {1, 2}, 'b': {4}})

# defaultdict를 사용할 때는 dictionary 에 존재하지 않는 값이라도 한번이라도 접근했던
# 키의 엔트리를 자동으로 생성한다.
# 이런 동작성이 마음에 들지 않으면 일반 딕셔너리의 setdefault()를 사용한다
d = {} # 일반 dictionary
d.setdefault('a',[]).append(1)
d.setdefault('a',[]).append(2)
d.setdefault('b',[]).append(4)
# print(d)
# {'a': [1, 2], 'b': [4]}
# 근데 많은 프로그래머들은 setdefult()가 자연스럽지 않다고 생각한다.

# 여러 값을 가지는 딕셔너리를 만드는 것이 복잡하지는 않다. 하지만 첫번째 값에 대한
# 초기화를 스스로 하려면 복잡한 과정을 거쳐야 한다

# example 2.
d = {}
for key, value in pairs:
    if key not in d:
        d[key] = []
    d[key].append(value)

# defaultdict를 사용하면, 좀 더 깔끔한 코드가 된다.
d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)

