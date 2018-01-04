"""1.13. 일반 키로 딕셔너리 리스트 정렬
딕셔너리 리스트가 있고, 하나 혹은 그 이상의 딕셔너리 값으로 정렬하고싶다.
"""

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

# example 1. operator 모듈의 itemgetter 함수를 사용하면 쉽게 정렬이 가능
# 모든 딕셔너리에 포함된 필드를 기준으로 데이터를 정렬해 출력한다

from operator import itemgetter

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))

print(rows_by_fname)
#[{'fname': 'Big', 'lname': 'Jones', 'uid': 1004},
# {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
# {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
# {'fname': 'John', 'lname': 'Cleese', 'uid': 1001}]
print(rows_by_uid)
#[{'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
# {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
# {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
# {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}]

# example 2. itemgetter 함수에 키를 여러 개 전달할 때
rows_by_lframe = sorted(rows, key=itemgetter('lname','fname'))
print(rows_by_lframe)
#[{'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
# {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
# {'fname': 'Big', 'lname': 'Jones', 'uid': 1004},
# {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003}]

# example 3. min() 과 max() 함수 적용
print(min(rows, key=itemgetter('uid')))
# {'fname': 'John', 'lname': 'Cleese', 'uid': 1001}
print(max(rows, key=itemgetter('uid')))
# {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}