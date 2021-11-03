#Лабораторная работа 4
#Монотонный список
def is_monotonic(nums):
    m = len(nums)
    n = True
    u = True
    for i in range (0, m - 1):
        if nums[i] - nums[i + 1] == 0:
            continue
        elif nums[i] - nums[i + 1] == -1:
            u = True
            break
        elif nums[i] - nums[i + 1] == 1:
            u = False
            break
        else:
            return False

    for i in range(0, m - 1):
        if u:
            if nums[i] - nums[i + 1] <= 0:
                continue
            else:
                n = False
        else:
            if nums[i] - nums[i + 1] >= 0:
                continue
            else:
                n = False

    return n
