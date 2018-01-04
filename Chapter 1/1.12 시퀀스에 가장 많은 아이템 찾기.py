"""1.12 시퀀스에 가장 많은 아이템 찾기
시퀀스에 가장 많이 나타난 아이템을 찾고 싶은 경우"""



words = [
   'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
   'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
   'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
   'my', 'eyes', "you're", 'under'
]

morewords = ['why','are','you','not','looking','in','my','eyes']

# example 1. collections.Counter와 most_common()메소드를 이용해서
# 가장 자주 나타나는 단어를 찾아보자

from collections import Counter
word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)
#[('eyes', 8), ('the', 5), ('look', 4)]

# example 2. Counter 는 아이템이 나타난 횟수 가리키는 딕셔너리를 말한다.
print(word_counts['not']) # 1
print(word_counts['eyes']) # 8

# example 3. Counter 인스턴스에 잘 알려지지 않은 기능으로 여러 가지 수식을
# 사용할 수 있다는 점이 있다.
a = Counter(words)
b = Counter(morewords)
print(a)
#Counter({'eyes': 8, 'the': 5, 'look': 4, 'into': 3, 'my': 3, 'around': 2, 'not': 1, "don't": 1, "you're": 1, 'under': 1})
print(b)
#Counter({'why': 1, 'are': 1, 'you': 1, 'not': 1, 'looking': 1, 'in': 1, 'my': 1, 'eyes': 1})
c = a + b
print(c) #카운터 합치기
#Counter({'eyes': 9, 'the': 5, 'look': 4, 'my': 4, 'into': 3, 'not': 2, 'around': 2, "don't": 1, "you're": 1, 'under': 1, 'why': 1, 'are': 1, 'you': 1, 'looking': 1, 'in': 1})
d= a - b
print(d) #카운터 빼기
#Counter({'eyes': 7, 'the': 5, 'look': 4, 'into': 3, 'my': 2, 'around': 2, "don't": 1, "you're": 1, 'under': 1})
