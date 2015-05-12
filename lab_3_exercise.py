# And truth Table
# a = 1
# b = 0
# if (a == 1 and b == 1):
#     print('1')
# elif ((a == 1 and b == 0) or (a == 0 and b == 1)):
#     print('0')
# elif (a == 0 and b == 0):
#     print('0')
# else:
#     print('Invalid Input')
#     
# # OR truth Table
# if (a == 1 or b == 1):
#     print('1')
# else:
#     print('0')
    
a = [1,1,1,1,0,0,0,0]

b = [1,0,1,0,1,0,0,1]

c = [1,1,0,0,0,1,0,1]

print('A B C Q')

for i in range(len(a)):

    q = ((a[i]&int(not(b[i])))|c[i])

print(a[i],' ',b[i],' ',c[i],' ',q,'(',bool(q),')')