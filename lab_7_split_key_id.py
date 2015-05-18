string = '82914656273523:a4edFea2786DGex'

sep = string.split(':', 1)

id = sep[0]
key = sep[1]

if (id.isdigit() and len(id) == 14 and len(key) > 10 and len(key) < 20):
    print('All is good.')
else:
    print('Re-enter the key or id.')