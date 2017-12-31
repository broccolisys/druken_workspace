input_list = input("입력 : ").split()

rotation_position = int(input_list[0]) % (len(input_list) - 1)
del(input_list[0])
print(' '.join(input_list[-rotation_position:] + input_list[0:-rotation_position]))
