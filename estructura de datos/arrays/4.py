nums = [1,3,5,6]
target=7

def search_inser(lista,target):
    i=0
    if target in lista:
        
        while i < len(lista):
            if lista[i]==target:
                break
            else:
                i+=1
    else:
        while i < len(lista):
            if lista[i]<target:
                i+=1
            else:
                lista.insert(i,target)
                break
    return i

def search_insert(nums, target):
    i = 0
    while i < len(nums):
        if nums[i] >= target:
            return i
        i += 1
    return len(nums)


x=search_insert(nums,target)

print(x)