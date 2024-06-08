def binary_search(nums: list, target: int):
    left, right = 0, len(nums)-1
    loops = 0

    while left <= right:
        loops += 1
        mid = left + (right - left) // 2
        print(f"loops: {loops},left: {left}, mid: {mid}, right: {right}")

        if nums[mid] == target:
            return mid

        elif target > nums[mid]:
            left = mid + 1

        elif target < nums[mid]:
            right = mid - 1

    return -1


if __name__ == '__main__':

    nums = [2, 5, 6, 8, 9, 10, 13, 20, 25, 27]
    target = 27

    index = binary_search(nums, target)

    if index != -1:
        print('Element found at index', index)
    else:
        print('Element not found in the list')
