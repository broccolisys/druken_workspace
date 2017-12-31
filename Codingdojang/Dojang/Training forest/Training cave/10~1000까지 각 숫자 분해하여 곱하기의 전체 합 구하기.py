def docstring():
    """
    10~1000까지 각 숫자 분해하여 곱하기의 전체 합 구하기
10 = 1 * 0 = 0
11 = 1 * 1 = 1
12 = 1 * 2 = 2
13 = 1 * 3 = 3
14 = 1 * 4 = 4
15 = 1 * 5 = 5

그러므로, 이 경우의 답은 0+1+2+3+4+5 = 15
    """

print(eval("+".join(["*".join(str(i)) for i in range(10,16)])))