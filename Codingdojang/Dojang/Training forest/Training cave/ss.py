sentence = input("문장을 입력하시오: ")
n = int(input("숫자를 입력하시오: "))

total = ""
for i in range(len(sentence)):
    script = sentence[i]
    script_return = ord(script) + n
    total += chr(script_return)

print(total)





