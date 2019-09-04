def removeElement(nums, val):
    # new_nums = []
    # my code
    k = 0
    for i in nums:
        if i != val:
            nums[k] = i
            k = k+1
    return k
    # someone's code
    # nums[:] = list(filter(lambda x:x != val, nums))
    # return len(nums)

print(removeElement([1,2,2,3,3,2], 2))


