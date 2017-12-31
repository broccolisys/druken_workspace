"""1.4 N 아이템의 최대 혹은 최소값 찾기
Collection 내부에서 가장 크거나 작은 N개의 아이템을 찾아야 한다.
heapq 모듈의 nlargest() nsmallest() 두 함수가 있다
"""
import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3,nums))

portfolio = [
   {'name': 'IBM', 'shares': 100, 'price': 91.1},
   {'name': 'AAPL', 'shares': 50, 'price': 543.22},
   {'name': 'FB', 'shares': 200, 'price': 21.09},
   {'name': 'HPQ', 'shares': 35, 'price': 31.75},
   {'name': 'YHOO', 'shares': 45, 'price': 16.35},
   {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3,portfolio,key=lambda  s:s['price'])
expensive = heapq.nlargest(3,portfolio,key=lambda s:s['price'])
print(cheap)
print(expensive)

# example 1, 가장 작은 or 가장 큰 값 아이템만 맨 앞으로 보낼 때
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heap = list(nums)
heapq.heapify(heap)
print(heap)
# 반대는
# heapq._heapify_max(heap)
# print(heap)
# heap[0] 가 가장 작은 아이템이 된다.

# example 2, 가장 작은 아이템을 순서대로 찾을려면
print(heapq.heappop(heap))
# 반대는
# heapq._heappop_max(heap)

# nlargest() 와 nsmallest() 함수는 찾고자 하는 아이템의 개수가 상대적으로 작을때 좋다
# 만약 최소값이나 최대값을 구하려할때, (갯수가 1개 일 경우) min()과 max()를 사용하는게 빠르다
# N의 크기가 Collection 크기와 비슷하면 sorted(items)[:N]나 sorted(items)[N:]을 사용하자

import random
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
min_nums = sorted(nums)[:2] # 앞에서 작은 수 2개
max_nums = sorted(nums)[-2:] # 뒤에서 큰수 2개
print(min_nums)
print(max_nums)