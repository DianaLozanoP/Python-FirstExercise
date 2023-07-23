def any7(nums):
    """Are any of these numbers a 7? (True/False)"""

    # YOUR CODE HERE
    y = 0
    for x in nums:
        if x == 7:
            y += 1
    if y >= 1:
        return "True"
    return "False"

print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))

