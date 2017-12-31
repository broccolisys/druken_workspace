def docstring():"""
input은 int n을 입력 받아 첫번째 row는 (n-1)의 O와 X, 
두번째 row는 (n-2)의 O와 XX, 세번째 row는 (n-3)의 0와 XXX... 
n번째 row는 n의 X을 출력하시오.
입력 예시: 6
출력 예시:
OOOOOX
OOOOXX
OOOXXX
OOXXXX
OXXXXX
XXXXXX
"""

n = int(input("숫자를 입력하시오: "))
print("\n".join(["O" * (n-i-1)+ "X" * (i+1) for i in range(n)]))