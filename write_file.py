input = open('text.txt', 'r')
output = open('new.txt', 'w')
 
for line in input:
    print(line, file= output, end='')
    
input.close()
output.close()

# buffersize = 100000
# input = open('bigfile.txt', 'r')
# output = open('newbigfile.txt', 'w')
# 
# buffer = input.read(buffersize)
# bufferlimit = 1000000
# 
# while bufferlimit > 0:
#     output.write(buffer)
#     print('.',end='')
#     bufferlimit = bufferlimit - buffersize

# Another way to loop through
# while len(buffer):
#     output.write(buffer)
#     print('.', end='')
#     buffer = input.read(buffersize)

# Limit reading/writing based on a buffer