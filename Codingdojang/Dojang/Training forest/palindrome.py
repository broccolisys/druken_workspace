def docstring():
    """
앞에서부터 읽을 때나 뒤에서부터 읽을 때나 모양이 같은 수를 대칭수(palindrome)라고
부릅니다. 두 자리 수를 곱해 만들 수 있는 대칭수 중 가장 큰 수는 9009 (= 91 × 99)
입니다. 세 자리 수를 곱해 만들 수 있는 가장 큰 대칭수는 얼마입니까?

    :return:
    """
best_number = 1 * 2

for i in range(99, 1000):
    for x in range(99,1000):
        total_number = i * x
        if str(total_number) == str(total_number)[::-1] and total_number > best_number:
            best_number = total_number
print(best_number)

def expert_coding():
    """
stop = False
for i in range(999, 100, -1):
    for j in range(999, i - 1, -1):
        if str(i * j) == str(i * j)[::-1]:
            print("{0} * {1} = {2}".format(i, j, i * j))
            stop = True
            break
    if stop:
        break

    :return:
    """