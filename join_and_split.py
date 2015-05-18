string = '-'
#string = '//'
sequence = ['a', 'b', 'c', 'd', 'e', 'f']
print(string)
string = string.join(sequence)
print(string)

# Splits a string and returns a list of each of the elements that were
# separated by the separator argument you give it.
letters = string.split('-')

for letter in letters:
    print(letter)
    
print(letters[2])

new_sequence = string.split('-',2)
print(new_sequence)