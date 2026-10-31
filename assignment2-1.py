# Assignment 2 searching tasks both use binary search
# Task 1: find first and last position of target in a sorted array
# Task 2: search target in a 2D matrix


def search_range(nums, target):
    # find the first position O(log n)
    first = -1
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            first = mid
            right = mid - 1   # keep going left to find an earlier one
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # target is not in the array
    if first == -1:
        return [-1, -1]

    # find the last position
    last = -1
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            last = mid
            left = mid + 1    # keep going right to find a later one
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return [first, last]

# task 2: search target in a 2D matric. O(log(m × n))
def search_matrix(matrix, target):
    # empty matrix
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return False

    rows = len(matrix)
    cols = len(matrix[0])

    # treat the matrix like one long sorted list with rows * cols items
    left = 0
    right = rows * cols - 1
    while left <= right:
        mid = (left + right) // 2
        row = mid // cols
        col = mid % cols
        value = matrix[row][col]
        if value == target:
            return True
        elif value < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


#  tests
def test_search_range():
    assert search_range([4, 9, 10, 13, 17, 17, 19, 21], 17) == [4, 5]
    assert search_range([2, 4, 6, 8, 10, 14, 16], 12) == [-1, -1]
    assert search_range([], 0) == [-1, -1]
    assert search_range([5], 5) == [0, 0]
    assert search_range([5], 3) == [-1, -1]
    assert search_range([7, 7, 7, 7, 7], 7) == [0, 4]
    assert search_range([1, 2, 3, 4, 5], 1) == [0, 0]
    assert search_range([1, 2, 3, 4, 5], 5) == [4, 4]
    assert search_range([1, 2, 2, 2, 3], 2) == [1, 3]
    assert search_range([1, 2, 3], 0) == [-1, -1]
    assert search_range([1, 2, 3], 10) == [-1, -1]
    assert search_range([-5, -3, -3, 0, 2], -3) == [1, 2]
    print("Task 1 tests passed")


def test_search_matrix():
    m = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    assert search_matrix(m, 3) == True
    assert search_matrix(m, 13) == False
    assert search_matrix(m, 1) == True
    assert search_matrix(m, 60) == True
    assert search_matrix(m, 0) == False
    assert search_matrix(m, 100) == False
    assert search_matrix([[5]], 5) == True
    assert search_matrix([[5]], 4) == False
    assert search_matrix([[1, 3, 5]], 3) == True
    assert search_matrix([[1], [3], [5]], 5) == True
    assert search_matrix([[1], [3], [5]], 4) == False
    assert search_matrix([], 1) == False
    assert search_matrix([[]], 1) == False
    print("Task 2 tests passed")


test_search_range()
test_search_matrix()