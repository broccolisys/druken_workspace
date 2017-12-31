def docstring():"""
1차원의 점들이 주어졌을 때, 그 중 가장 거리가 짧은 것의 쌍을 출력하는 함수를 작성하시오. 
(단 점들의 배열은 모두 정렬되어있다고 가정한다.)
예를들어 S={1, 3, 4, 8, 13, 17, 20} 이 주어졌다면, 결과값은 (3, 4)가 될 것이다.
"""
f
def summury():"""

    """

import random
# points = list({1, 3, 4, 8, 13, 17, 20})
points = list(set(random.randint(1,100) for i in range(10)))
points.sort()
print("수직선 위 점들은 ", points)

# 최소 거리의 점쌍을 모음
distances = [[points[0], points[1], points[1]-points[0]]]
for p1 in range(1,len(points)-1): # 1로 시작하는 이유는 이미 distances에서 0값을 잡아기때문
    left = points[p1]
    right = points[p1+1]
    distance = right - left
    if distances[0][2] > distance:
        distances = [[left, right, distance]]
    elif distances[0][2] == distance:
        distances += [[left, right, distance]]

print("가장 짧은 거리는", distances[0][2], ": ", end='')
for i in range(len(distances)):
    if i == len(distances)-1:
        print(distances[i][0],"~",distances[i][1],end='')
    else:
        print(distances[i][0],"~",distances[i][1],end=', ')


def expert_coding():"""
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# 다음 입사문제 중에서
# 1차원의 점들이 주어졌을 때, 그 중 가장 거리가 짧은 것의 쌍을 출력하는 함수를 작성하시오. (단 점들의 배열은 모두 정렬되어있다고 가정한다.)

import random
# points = list({1, 3, 4, 8, 13, 17, 20})
points = list(set([random.randint(1,100) for i in range(10)]))
points.sort()
print("수직선 위 점들은 ", points)

# 최소 거리의 점쌍을 모음
distances = [[points[0], points[1], points[1]-points[0]]]
for p1 in range(1,len(points)-1):
    left = points[p1]
    right = points[p1+1]
    distance = right - left
    if distances[0][2] > distance:
        distances = [[left, right, distance]]
    elif distances[0][2] == distance:
        distances += [[left, right, distance]]

print("가장 짧은 거리는", distances[0][2], ": ", end='')
for i in range(len(distances)):
    if i == len(distances)-1:
        print(distances[i][0],"~",distances[i][1],end='')
    else:
        print(distances[i][0],"~",distances[i][1],end=', ')


     
    """
