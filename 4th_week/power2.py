def backtrack(nums, index, current, current_sum, target):
    result = []
    if current_sum == target:
        return [current.copy()]
    if index == len(nums) or current_sum > target:
        return []

    current.append(nums[index])
    result.extend(backtrack(nums, index + 1, current, current_sum + nums[index], target))
    current.pop()
    result.extend(backtrack(nums, index + 1, current, current_sum, target))
    return result


nums = [i for i in range(1, 11)]
result = backtrack(nums, 0, [],0, 10,)
print(*result)