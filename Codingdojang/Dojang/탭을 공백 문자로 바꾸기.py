def docstring():"""
A씨는 개발된 소스코드를 특정업체에 납품하려고 한다. 
개발된 소스코드들은 탭으로 들여쓰기가 된것, 공백으로 들여쓰기가 된 것들이 섞여 있다고 
한다. A씨는 탭으로 들여쓰기가 된 모든 소스를 공백 4개로 수정한 후 납품할 예정이다.
A씨를 도와줄 수 있도록 소스코드내에 사용된 탭(Tab) 문자를 공백 4개(4 space)로 바꾸어 
주는 프로그램을 작성하시오.
 """

def summary():"""
0. 파일 주소 입력
1. 파일을 읽어온다.
2. 읽어온 파일에서 tab 문자를 공백 4개로 바꾸어주는 coding 
3. 저장한 후 종료    
    """
file_address = input(":")
# f = open(file_address, "r")
# line = f.read()
# line = line.replace("\t","    ")
# f.close()
# f = open(file_address,"w")
# f.write(line)
# f.close()


if __name__ == "__main__":
    f = open(file_address, "r")
    test_line = f.readlines()
    print(test_line)

def expert_coding():
    """
import os               # os module 를 불러온다
import re               # re module 를 불러온다 (파이썬에서 정규 표현식을 지원)
filepath    = input('파일이 위치한 경로를 입력하세요:')   # filepath 를 입력해서 변수 filepath 저장
ext         = input('확장자를 입력하세요: '            )  # 확장자를 입력해서 변수 ext 저장


'''파일경로와 확장자를 파라메터로 받아서 하위디렉토리 모두 탐색해서 조건에
맞는 파일전체경로를 list 에 담아 리턴한다.'''
def getFileList(filepath,ext):   # 입력받은 filepath와 ext 를 입력값으로 받는 함수 만듬
    _filelist = [] # 파일의 경로 및 이름을 저장할 창고
    for root, dirs, files in os.walk(filepath): # 파일의 root에 있는 directory, file 검색을 통해, 파일들을 하나씩 뽑아낸다(경로에있는)
        for filename in files: # 파일 중 파일들을 하나씩 뽑아서
            if (filename.lower()).endswith(ext.lower()): # endswith 가 ext 로 끝나면 참!
                _filelist.append(root+"\\"+filename) # 그것을 root와 \와 이름과 함께 _filelist 저장 후

    return _filelist #_ 그 filelist를 return


for _path in getFileList(filepath,ext): # return  된 _filelist 에서 _path를 하나씩 뽑아 낸 후
    print(_path) # 출력
    os.system ("copy %s %s" % (_path, _path+".bak")) #백업파일 생성 # os.system을 불러와서 copy 를 통해 백업파일 생성

    with open( _path+".bak",'r') as f: # backup 파일 불러와서
        srcContent = f.read() #읽고
        with open(_path,"w") as writelist: # 쓴다
            writelist.write(srcContent.replace("\t","    ")) # 다음 내용을..
    """