def search(nums,target) :
    l = 0
    r = len(nums)-1
    mid = 0
    while(l<=r) :
        mid = l + int((r-l)/2)
        if target == nums[mid] : return mid
        elif target > nums[mid] : l = mid + 1
        else : r = mid - 1
    if target > nums[mid] : return mid + 1
    else : return mid
    
if __name__ == '__main__':
    nums = [-1,0,3,5,9,12]
    target = 4
    print(search(nums,target))
    