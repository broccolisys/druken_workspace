def docstring():"""A씨는 게시판 프로그램을 작성하고 있다.

A씨는 게시물의 총 건수와 한 페이지에 보여줄 게시물수를 입력으로 주었을 때 총 페이지수를 리턴하는 프로그램이 필요하다고 한다.

입력 : 총건수(m), 한페이지에 보여줄 게시물수(n) (단 n은 1보다 크거나 같다. n >= 1)
출력 : 총페이지수

A씨가 필요한 프로그램을 작성하시오.

"""

def summary():
    """먼저 입력값을 m,n 을 받고 자체 계산한 후 총 페이지수를 보여준다"""

m = int(input("총 건수를 입력하시오: "))
n = int(input(" 한 페이지에 보여줄 게시물 수를 입력하시오: "))

def caculation_pages(m,n):
    x = m // n
    if m / n > x:
        print("m : %i n : %i 출력: %i" %(m,n,m//n+1))
    elif m / n <= x:
        print("m : %i n : %i 출력: %i" %(m,n,m//n))

caculation_pages(m,n)

def expert_coding():"""
def board(m,n):
    page = m // n
    if m % n != 0:
        page += 1
    print(page)"""