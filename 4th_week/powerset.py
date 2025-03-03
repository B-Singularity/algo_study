def powerset(nums):
    result = []

    def backtrack(index, current):
        if index == len(nums):
            result.append(list(current.copy()))
            return

        current.append(nums[index])
        backtrack(index + 1, current)
        current.pop()

        backtrack(index + 1, current)

    backtrack(0, [])
    return result