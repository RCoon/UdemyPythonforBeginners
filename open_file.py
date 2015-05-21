file = open('text.txt')

for line in file:
    print(line, end = '')
    
file.close()