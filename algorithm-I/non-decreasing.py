


def sortedSquares(nums) :
    for i in range(len(nums)) : nums[i] = nums[i]**2
    return sorted(nums)

def rotate(nums,k) :
    k = k % len(nums)
    if ( k < len(nums)//2) :
        for i in range(k) : 
            temp = nums.pop()
            nums.insert(0,temp) 
    else :
        for i in range(len(nums)-k) : 
            temp = nums.pop(0)
            nums.append(temp)
        
    
    
        
        
        
nums = [1,2,3,4,5,6,7]
k = 6
# print(id(nums))
rotate(nums,k)
print(nums)

