def find_duplicate(nums):
    if not isinstance(nums, list) or len(nums) < 2:
        return False

    for index in range(len(nums)):
        if not isinstance(nums[index], int) or nums[index] < 0:
            return False

    return True


if __name__ == "__main__":
    print(find_duplicate(["a", "b"]))
