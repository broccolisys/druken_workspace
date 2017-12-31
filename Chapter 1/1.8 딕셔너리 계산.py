"""1.8 딕셔너리 계산
딕셔너리 데이터에 여러 계산을 수행하고 싶을때 (최소값, 최대값, 정렬 등)
"""
# example 1 딕셔너리에 주식 이름과 가격이 들어 있을 때
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM' : 205.55,
    'HPQ' : 37.20,
    'FB' : 10.75
}
# Dictionary 내용에 대해 유용한 계산을 하려면  키와 값을 뒤집어 주는
# zip()를 이용해 주는 것이 좋다
min_price = min(zip(prices.values(), prices.keys()))
print(min_price)
# (10.75, 'FB')
max_price = max(zip(prices.values(), prices.keys()))
print(max_price)
# (612.78, 'AAPL')
# example 2 데이터의 순서를 매기려면 zip()과 sorted() 를 함께 사용한다
prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)
# [(10.75, 'FB'), (37.2, 'HPQ'), (45.23, 'ACME'), (205.55, 'IBM'), (612.78, 'AAPL')

# example 3 계산을 할 때, zip()
