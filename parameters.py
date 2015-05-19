list1 = [1,2,3,4]

def function_name(lists):
    "This will simply demonstrate by reference"
    end = [5,6,7,8]
    #lists.extend(end)  # Adds each of the values to the end of the list
    lists.append([5,6,7,8])  # Creates a nested list
    return

print("The values are: ",list1)
function_name(list1)
print("The values are: ",list1)