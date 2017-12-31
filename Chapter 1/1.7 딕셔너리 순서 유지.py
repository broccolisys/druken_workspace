"""1.7 딕셔너리 순서 유지
딕셔너리를 만들고, 순환이나 직렬화 할 때 순서를 조절할려고 할때
딕셔너리 내부 아이템의 순서를 조절하려면 collections 모듈의
OrderedDict를 사용한다
이 모듈을 사용하면 삽입 초기의 순서를 그대로 기억한다
"""
from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

# print(d)
# OrderedDict([('foo', 1), ('bar', 2), ('spam', 3), ('grok', 4)])
for key in d:
    print(key,d[key])
""" foo 1
    bar 2
    spam 3
    grok 4 """

# OrderedDict 는 나중에 직렬화하거나 다른 포맷으로 인코딩할 다른 매핑을 만들 때
# 특히 유용하다. 예를 들어, JSON 인코딩에 나타나는 특정 필드의 순서를 조절하기 위해서
# OrderedDict에 다음과 같이 데이터를 생성한다

import json #javascript object notation 으로써 json의 library를 이용한다
print(json.dumps(d))
# {"foo": 1, "bar": 2, "spam": 3, "grok": 4}

# OrderedDict 는 내부적으로 doubly linked list 로 삽입 순서와 관련 있는 키를 기억한다
# 즉, 새로운 아이템을 처음으로 삽입하면 리스트의 제일 끝에 위치시킨다.
# 기존 키에 재할당을 한다 해도 순서에는 변화가 생기지 않는다.
# doubly linked list 이기 때문에 크기가 일반적인 dictionary 에 비해 두배로 크다
# 많은 라인의 csv파일을 읽어드릴대 메모리 소비가 유용한지 확인해봐야 한다.

