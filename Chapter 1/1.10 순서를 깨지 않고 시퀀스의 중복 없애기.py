"""1.10 순서를 깨지 않고 시퀀스의 중복 없애기
시퀀스에서 중복된 값을 없애고 싶지만, 아이템의 순서는 유지하고 싶을때
"""


# example 1 시퀀스의 값이 해시(hash) 가능하다면,
# (( hash 가능하다 = 대응관계를 나타내는 자료형이다 <-> hash 불가능 (dict))
# 이 문제는 세트와 generator를 사용해서 해결한다

def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a = [1, 5, 2, 1, 9, 1, 5, 10]

# print(list(dedupe(a)))

# example 2 해시 불가능한 타입(dict)의 중복을 없앨려면?
def dedupe2(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)  # is None null 객체를 확인할때
        if val not in seen:
            yield item
            seen.add(val)


b = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
print(list(dedupe2(b, key=lambda d: (d['x'], d['y']))))
# print(list(dedupe2(a, key=lambda  d: d['x'])))
# [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]
# [{'x': 1, 'y': 2}, {'x': 2, 'y': 4}]

# example 3, 중복을 없앨려면 대개 세트를 만드는게 좋다
c = [1, 5, 2, 1, 9, 1, 5, 10]
print(set(c))
# 이렇게 하면 기존 데이터의 순서가 훼손된다.
# 예를 들어 파일을 읽어 들일 때 중복된 라인을 무시하려면 다음과 같은 코드를 사용한다

with open("somefile", 'r') as f:
    for line in dedupe2(f):
        ...

