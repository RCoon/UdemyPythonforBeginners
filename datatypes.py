b = 'Ryan'
a = 'Welcome {}'.format(b)

print(a)

# tuple
x = (1,2,3,4,5)
# cannot append tuples
print(type(x),x)

y = [1,2,3,4,5]
y.append(6)
print(type(y),y)

z = [1,2,3,4,5]
# with lists you can declare a certain index within the list by using square brackets and an index value
print(type(z),z[2:4])

# dictionaries are like associated arrays or hashsets in java
d = {'one':1, 'two':2}
print(type(d),d)

# less times using the quote key, keys that are strings or numbers are automatically detected
dictionary = dict(
                  one = 1, two = 'two'
                  )

print(type(dictionary),dictionary)
print(dictionary.get('one'))

boolean = False
a,b = 0,1
if a == b:
    print(True)
else:
    print(False)
print(type(boolean),boolean)