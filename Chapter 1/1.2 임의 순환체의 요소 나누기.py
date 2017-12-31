"""1.2 임의 순환체의 요소나누기
순환체를 Unpacking 하려는데 요소가 N개 이상 포함되어 "값이 너무 많습니다"라는 예외가 발생한다.
이 문제 해결을 위해 파이썬 "별 표현식"을 사용한다. 예를 들어 학기 성적을 산출할 때 첫번째와
마지막 과제 점수를 무시하고 나머지의 평균을 사용할 경우, 그 과제가 24개 였다면 어떨까?"""

# example 1, 원하는 값이 가운데 있을 때
def drop_first_last(grades):
    first, *middle, last = grades
    return sum(middle)/len(middle)

# example 2, 원하는 값이 뒤에 있을 때
record = ('Dave', 'dave@example.com','773-555-1212','847-555-1212')
name, email, *phone_numbers = record
print(name)
print(email)
print(phone_numbers)

# example 3, 원하는 값이 앞에 있을 때
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(trailing)
print(current)

# example 4, 태킹이 되어 있는 튜플이 있다면
records = [
    ('foo', 1, 2),
    ('bar','hello'),
    ('foo', 3, 4),
]

def do_foo(x,y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

# example 5, 문자열 프로세싱에 편리한 문법
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname)
print(homedir)
print(sh)

# example 6, Unpacking 이후 특정 값을 버리고 싶다면?
# _ 이나 ign 를 이용해라
record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name)
print(year)

# example 7 꼬리와 머리 부분을 분리하고자 할 경우
items = [1, 10, 7, 4, 5, 9]
head, *tail = items
print(head)
print(tail)

