def docstring():
    """
    피보나치 수열의 각 항은 바로 앞의 항 두 개를 더한 것이 됩니다.
    1과 2로 시작하는 경우 이 수열은 아래와 같습니다.
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
짝수이면서 4백만 이하인 모든 항을 더하면 얼마가 됩니까?

    :return:
    """
pibonacci = [1,2]
while pibonacci[-2] + pibonacci[-1] <=100:
    pibonacci.append(pibonacci[-2]+pibonacci[-1])

pibonacci_even = [pibonacci[i] for i in range(len(pibonacci)) if pibonacci[i] % 2]
print("짝수 피보나치 수열", pibonacci_even,"의 합은",sum(pibonacci_even))
