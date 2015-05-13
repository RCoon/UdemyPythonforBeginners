while True:
    gender = input('What\'s your gender?\n> ').lower()
    if (gender == 'm' or gender == 'f'):
        break
    else:
        print('Please try again')
        continue
print('You entered {}.'.format(gender))
