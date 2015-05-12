# a = 0
# while a < 100:
#     print(a)
#     a += 1
# print('This is finished')

for key,data in enumerate('strings'):
    if key % 2 == 0:
        print('The letter {} is in an even location'.format(data))