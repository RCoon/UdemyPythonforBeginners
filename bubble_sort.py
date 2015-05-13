list = [6,14,1,3,65,19,2,78,54,4]

def bubble_sort(list):
    changes = 0
    for i in range(len(list) - 1):
        if (list[i] > list[i+1]):
            changes += 1
            temp = list[i+1]
            list[i+1] = list[i]
            list[i] = temp
    if changes > 0:
        return bubble_sort(list)
    else:
        return list
    
print(bubble_sort(list))   