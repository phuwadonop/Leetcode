from typing import List


def move_zeroes(nums : List[int]) :
    j = 0
    for i in range(len(nums)) :
        if nums[i] != 0 and nums[j] == 0 :
            nums[i] , nums[j] = nums[j] , nums[i]
        if nums[j] != 0 : j += 1 

def move_zeroes_2(nums : List[int]) :
    j = 0
    for i in range(len(nums)) :
        if nums[i] != 0 :
            nums[j] = nums[i]
            j += 1
            
    for i in range(j,len(nums),1) :
        nums[i] = 0
                
nums = [0,1,0,3,12]
move_zeroes_2(nums)
print(nums)