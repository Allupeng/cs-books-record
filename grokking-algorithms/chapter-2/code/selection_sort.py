# selection sort using array
def find_min_num(nums):
    min_value = nums[0]
    min_index = 0
    for i in range(1, len(nums)):
        if nums[i] < min_value:
            min_value = nums[i]
            min_index = i
    return min_index


def selection_sort(nums):
    new_array = list()
    for i in range(len(nums)):
        min_index = find_min_num(nums)
        new_array.append(nums.pop(min_index))
    print(new_array)
    return new_array

if __name__ == '__main__':
    nums = [5, 3, 6, 2, 10]
    selection_sort(nums)


