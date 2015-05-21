buffersize = 100000
# Use \ to separate directories in Windows when opening a file in a different
# directory.
input = open('bigfile.txt', 'r')
output = open('newbigfile.txt', 'w')
 
buffer = input.read(buffersize)
bufferlimit = 1000000

while len(buffer):
    output.write(buffer)
    print('.', end='')
    buffer = input.read(buffersize)
    
input.close()
output.close()