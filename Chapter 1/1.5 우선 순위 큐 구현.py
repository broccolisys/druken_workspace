"""1.5 우선 순위 큐 구현
주어진 우선 순위에 따라 아이템을 정렬하는 큐를 구현하고 항상 우선 순위가
가장 높은 아이템을 먼저 팝 하도록 한다
다음에 나온 코드에서 heapq 모듈을 사용해 간단한 우선 순위 큐를 구현한다"""

import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self): # __repr__  는 '문자열'을 return 하면서 출력한다
        return 'Item({!r})'.format(self.name)

q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())

# heapq.heappop() 은 list_queue의 첫 번째 아이템이 가장 작은 우선 순위를 가진 것처럼
# 아이템을 삽입하거나 제거한다.
# heappop() 메소드는 항상 가장 작은 아이템을 반환해서 queue의 pop 이 올바른 아이템에
# 적용될 수 있도록 한다. 힙의 크기가 N일 때 푸시와 팝의 시간복잡도가 0(logN)이므로 N이
# 아주 커진다 해도 상당히 효율적이다.
# queue 가 tuple 로 구성되어있고,(-priority, index, item)
# priority 값은 큐 내부 아이템을 가장 높은 우선 순위에서 낮은 우선 순위로 정렬하기 위해 무효화된다
# index 변수는 우선 순위가 동일한 아이템의 순서를 정할 때 사용한다.
# 일정하게 증가하는 인덱스값을 유지하기 때문에 힙에 아이템이 삽입된 순서대로 정렬할 수 있다.
# 인덱스는 우선 순위 값이 동일할 때도 중요한 역할을 한다(왜냐하면 들어온 순서대로 출력할 수 있기 때문)

a = Item('foo')
b = Item('bar')
print(a < b ) # 에러남

a = (1,Item('foo'))
b = (5, Item('bar'))
print(a < b) # True 값 나옴
# 즉 우선 순위 값이 달라서 비교가 가능 하지만,
# 우선 순위 값이 같은 두 아이템의 비교는 실패!
c = (1, Item('grok'))
print(a < c) # 에러남

# example 1 여기 인덱스 값을 추가해서 tuple(priority, index, item) 을 만들면
# 어떠한 튜플도 동일한 인덱스 값을 가질 수 없으므로 이 문제를 원칙적으로 해결 할 수 있다.

a = (1, 0, Item('foo'))
b = (5, 1, Item('bar'))
c = (1, 2, Item('grok'))

print(a < b) # True
print(a < c) # True



