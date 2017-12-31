def grep(lines):
    for line in lines:
        for c in line:
            characters = ['a','b','c','d','e','f','g',
                          'h','i','j','k','l','m','n'
                          'o','p','q','r','s','t','u'
                          'v','w','x','y','z']
            if c in characters:
                yield c

with ("strings.txt", "r") as f:
    list = []
    for c in grep(f):
        list.append(c)
print(" ".join(list))
