def sortNums(a):
    i = 0
    j = 0
    k = len(a) - 1
    
    while j <= k:
        if a[j] == 0:
            a[i], a[j] = a[j], a[i]
            i += 1
            j += 1
        elif a[j] == 1:
            j += 1
        else:
            a[j], a[k] = a[k], a[j]
            k -= 1
    return a


print(sortNums([0,1,2,1,0,2,1,0]))
print(sortNums([2,2,2,2]))
print(sortNums([0,0,0,0]))
print(sortNums([1,1,1,1]))
print(sortNums([2,0,1]))
print(sortNums([]))
