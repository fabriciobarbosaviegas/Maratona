def binSearch(nums, target):
    min = 0
    max = len(nums) - 1

    while min <= max:
        mid = (min + max) // 2
        guess = nums[mid]

        if target == guess:
            return mid
        if target < guess:
            max = mid - 1
        else: 
            min = mid + 1
    
    return min

nums = [1,3,5,6]
target1 = 5
target2 = 2
target3 = 7

print(binSearch(nums, target1))
print(binSearch(nums, target2))
print(binSearch(nums, target3))