def docstring():"""
예로 10 ~ 15 까지의 각 숫자의 개수를 구해보자
10 = 1, 0
11 = 1, 1
12 = 1, 2
13 = 1, 3
14 = 1, 4
15 = 1, 5
그러므로 이 경우의 답은 0:1개, 1:7개, 2:1개, 3:1개, 4:1개, 5:1개

    """

store = [0 for i in range(10)]

for x in range(10,16):
    for t in str(x):
        store[int(t)] += 1

for g in range(10):
    print(g,store[g])
