def solution(number):
    nums = []
    for i in range(number):
        if i % 3 == 0 and i % 5 == 0:
            nums.append(i)
        elif i % 3 == 0 or i % 5 == 0:
            nums.append(i)
    return sum(nums)
