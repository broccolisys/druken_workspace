def docstirng():"""

# A씨는 두 개의 버전을 비교하는 프로그램을 작성해야 한다.
# 버전은 다음처럼 "." 으로 구분된 문자열이다.
# 버전 예) 1.0.0, 1.0.23, 1.1
# 두 개의 버전을 비교하는 프로그램을 작성하시오.
# 다음은 버전 비교의 예이다.
# 0.0.2 > 0.0.1
# # 1.0.10 > 1.0.3
# 1.2.0 > 1.1.99
# 1.1 > 1.0.1
"""

def summury ():
    """
    1. max 함수 이용
    2. 0입력값 없을때 추가해주는것
    3. 비교
    """
version1 = input("버전을 입력하세요 :").split('.')
version2 = input("버전을 입력하세요 :").split('.')

compare = '='
for i in range(max(len(version1), len(version2))):
    if len(version1) == i:
        version1 += [0]
    if len(version2) == i:
        version2 += [0]

    if int(version1[i]) > int(version2[i]):
        compare = '>'
        break
    elif int(version1[i]) < int(version2[i]):
        compare = '<'
        break

print('.'.join(version1), compare, '.'.join(version2))