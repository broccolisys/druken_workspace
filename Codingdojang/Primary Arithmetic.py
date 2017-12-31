def docstring():"""    
첫 번째 계산
아이들은 여러 자리 숫자들을 더하기 위해서 우에서 좌로 숫자를 하나씩 차례대로 
더 하라고 배웠다. 1을 한 숫자 위치에서 다음 자리로 더하기위해 이동하는 
"한자리올림"연산을 많이 발견하는 것은 중요한 도전이 된다. 
당신의 일은 교육자가 그들의 어려움을 평가하기 위하여, 덧셈 문제들의 
각 집합에 대해서 한자리올림 연산들의 수를 계산하는 것이다.

입력
입력의 각 라인은 10개의 숫자들보다 미만인 양의 정수들 두 개를 포함한다. 
입력의 마지막 라인은 0 0 을 포한한다.

출력
마지막을 제외한 입력의 각 라인에 대해서 당신은 두 숫자들을 더한 결과에서 
한자리올림 연산들의 수를 아래 처럼 보여지는 형식으로 계산하여 출력해야 한다.

입력 샘플
123 456 
555 555 
123 594 
0 0

출력 샘플
No carry operation. 
3 carry operations. 
1 carry operation.
"""

def primary(first,second):
    carry =0
    if first[0] == 0 or second[0] == 0:
        pass
    for i in range(1,4):
        if int(first[-i]) + int(second[-i]) >= 10:
            carry += 1
    if carry == 0:
        print("No carry operation.")
    elif carry == 1:
        print(carry, "carry operation.")
    else:
        print(carry, "carry operations.")

a, b = input("첫번째 숫자: ").split(" ")
c, d = input("두번째 숫자: ").split(" ")
e, f = input("세번째 숫자: ").split(" ")
g, h = input("마지막숫자: ").split(" ")
primary(a,b)
primary(c,d)
primary(e,f)

def expert_coding():"""
    while True:
        numbers = input("더할 두 수는 : ")
        if numbers == '0 0':
            break
        n1, n2 = numbers.split()

        n1_len = len(n1)
        n2_len = len(n2)
        if n1_len < n2_len:
            n1 = '0' * (n2_len - n1_len) + n1
        elif n1_len > n2_len
        :
            n2 = '0' * (n1_len - n2_len) + n2

        carry_num = sum([1 if int(n1[i]) + int(n2[i]) > 9 else 0 for i in range(len(n1))])
        if carry_num:
            print(carry_num, "carry operations.")
        else:
            print("None carry operation.")"""
