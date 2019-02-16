nums = [4,2,1]
flag = True
for i in range(len(nums)):
    print i
    if nums[i] > nums[i + 1]:
        if not flag:
            print False
        flag = False
        if len(nums) - i < 2:
            break
        else:
            if nums[i] > nums[i + 2]:
                nums[i] = nums[i + 1]
            nums[i + 1] = nums[i]
            i -= 1
print True
