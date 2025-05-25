def searchRange(nums, target):
    first = -1
    second = -1
    
    min = 0 
    max = len(nums) - 1

    while min <= max:
        mid = (min + max) // 2
        guess = nums[mid]

        if(target == guess):
            return [mid-1, mid]
        if(target < guess):
            max = mid - 1
        else:
            min = mid + 1
            
    return [-1, -1]

nums = [5,7,7,8,8,10]
target1 = 8
target2 = 6
target3 = 0

print(searchRange(nums, target1))
print(searchRange(nums, target2))
print(searchRange(nums, target3))