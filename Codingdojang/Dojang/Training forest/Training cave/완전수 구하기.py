def docstring():
    """
    자기 자신을 제외한 모든 양의 약수들의 합이 자기 자신이 되는 자연수를 완전수라고 한다.
    예를 들면, 6과 28은 완전수이다. 6=1+2+3 // 1,2,3은 각각 6의 약수 28=1+2+4+7+14 //
     1,2,4,7,14는 각각 28의 약수 입력으로 자연수 N을 받고, 출력으로 N 이하의
     모든 완전수를 출력하는 코드를 작성하라.
    """


n = int(input("n을 입력하세요 : "))

for i in range(2, n + 1):
#왜 2를 썼을까? range 1,1 이 되니까?
    temp = '+'.join([str(j) for j in range(1, i) if not(i % j)])

    if eval(temp) == i:
        print(i, "는 완전수 : ", i, "=", temp)


#
# number_ = int(input("숫자를 입력하시오: "))
# store = []
# for base in range(1,10):
#     if number_ % base == 0:
#         store += str(base)+str(number_//base)
#
# t= ",".join(sorted(list(set("".join(i for i in store)))))
# print(t)
#


