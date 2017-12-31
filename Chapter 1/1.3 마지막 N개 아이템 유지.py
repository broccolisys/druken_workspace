"""1.3 마지막 N개 아이템 유지
순환이나 프로세싱 중 마지막으로 발견한 N개의 아이템을 유지하고 싶다
collections.deque를 사용하자"""

# example 1, 여러 줄에 대해서 간단한 텍스트 매칭을 수행하고 처음으로 발견한 N 라인을 찾는다.

from  collections import deque
def search(lines, pattern, history = 5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

if __name__ == '__main__':
    with open('somefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)

# 아이템을 찾는 coding을 할때 주로 yield 를 포함한 제너레이터 함수를 만들곤 한다.
# 이렇게 하면 검색 과정과 결과를 사용하는 코드를 분리할 수 있다.


# example 2, deque(maxlen=N)으로 고정 크기 큐를 생성한다.
# 큐가 꽉찬 상태에서 새로운 아이템을 넣으면 가장 마지막 아이템이 자동으로 삭제된다

q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
print(q)
q.append(5)
print(q)

# example 3, 큐 구조체가 필요할 때 deque를 사용할 수 있다.
# 최대 크기를 지정하지 않으면 제약없이 양쪽에 아이템을 넣거나 빼는 작업을 할 수 있다.

q = deque()
q.append(1)
q.append(2)
q.append(3)
print(q)
q.appendleft(4)
print(q)
q.pop()
print(q)
q.popleft()
print(q)