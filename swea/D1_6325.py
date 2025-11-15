def num_find(nums, a, b):

    a_flag = False
    b_flag = False

    for i in range(len(nums)):
        if (nums[i] == a):
            a_flag = True
        if (nums[i] == b):
            b_flag = True

    print(f"{a} => {a_flag}")
    print(f"{b} => {b_flag}")


nums = [2, 4, 6, 8, 10]
print(nums)
num_find(nums, 5, 10)
