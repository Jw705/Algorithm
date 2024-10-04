def solution(A):
    detected_nums = dict()
    for num in A:
        if num in detected_nums:
            detected_nums[num] += 1
        else:
            detected_nums[num] = 1
    for num in detected_nums.keys():
        if detected_nums[num] % 2 == 1:
            return num