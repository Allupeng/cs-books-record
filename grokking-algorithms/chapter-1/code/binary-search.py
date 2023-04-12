# binary-search
# nums is a sorted array,target is the vaule which you want to search
# value set is [left, right]
# if nums contains the target, return it's position
# if nums don't contains the target, return 
# implement by iterative
def binary_search_iterative(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + mid) // 2
        guess = nums[mid]
        if guess < target:
            low = mid + 1
        elif guess > target:
            high = mid - 1
        else:
            return mid
    return None



        