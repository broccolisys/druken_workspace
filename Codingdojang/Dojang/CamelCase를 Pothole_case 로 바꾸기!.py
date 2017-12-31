def docstring():"""
파이썬과 같은 몇몇 프로그래밍 언어는 Pothole_case 를 더 선호하는 언어라고 합니다.
Example:
codingDojang --> coding_dojang
numGoat30 --> num_goat_3_0
위 보기와 같이 CameleCase를 Pothole_case 로 바꾸는 함수를 만들어요!
출처: UT past test
    """
def summary ():"""
대문자를 따로 모으고, 숫자도 따로 모아서
하나씩 뽑을때 , 대문자나 숫자를 인식할 경우 
따로 붙여서 출력
    """
sentence = input("CameleCase를 입력하시오: ")
upper_list = ['A','B','C','D','E','F','G','H','I','J','K','L','N','M','O','P','G','R','S','T'
              ,'U','V','W','X','Y','Z']
number_list = ['1','2','3','4','5','6','7','8','9','0']
store = []
for i in sentence:
    if i in upper_list:
        store.append("_"), store.append(i.lower())
    elif i in number_list:
        store.append("_"), store.append(i)
    else:
        store.append(i)
        continue
finish = ''.join(store)
print(finish)