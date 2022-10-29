def search(target,list):
    l = 0 
    r = len(list) - 1
    while (l<=r) :
        mid = l + int((r-l)/2)
        if target == list[mid] : return mid
        elif target > list[mid] : l = mid + 1
        else : r = mid - 1
    return -1

def two_sum(numbers , target) :
    l = len(numbers) 
    for i in range(l) :
        search_tg = target - numbers[i]
        temp = numbers[i]
        numbers.remove(temp)
        index = search(search_tg,numbers)
        numbers.insert(i,temp)
        if index != -1 : return sorted([i+1,index+2])
        
def two_sum_2(numbers,  target) :
    l, r = 0 , len(numbers) - 1
    while(numbers[l] + numbers[r] != target) :
        if numbers[l] + numbers[r] < target : l += 1
        else : r -= 1
    return [l+1,r+1]

numbers = [1,2,3,4,4,9,56,90]
target = 8
print(two_sum(numbers,target))
        
