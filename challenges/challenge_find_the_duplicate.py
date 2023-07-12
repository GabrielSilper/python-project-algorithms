def merge_sort(array, start=0, end=None):
    if end is None:
        end = len(array)
    if end - start > 1:
        mid = (end + start) // 2
        merge_sort(array, start, mid)
        merge_sort(array, mid, end)
        merge(array, start, mid, end)


def merge(array, start, mid, end):
    left = array[start:mid]
    right = array[mid:end]

    left_index, right_index = 0, 0

    for index in range(start, end):
        if left_index >= len(left):
            array[index] = right[right_index]
            right_index += 1
        elif right_index >= len(right):
            array[index] = left[left_index]
            left_index += 1
        elif left[left_index] < right[right_index]:
            array[index] = left[left_index]
            left_index += 1
        else:
            array[index] = right[right_index]
            right_index += 1


def find_duplicate(nums):
    if not isinstance(nums, list) or len(nums) < 2:
        return False

    merge_sort(nums)  # O(n log n)

    for index in range(len(nums) - 1):  # O(n)
        if not isinstance(nums[index], int) or nums[index] < 0:
            return False
        if nums[index] == nums[index + 1]:
            return nums[index]
    return False


#  algoritmo de complexidade de tempo O(n log n) por ser a que mais pesa


if __name__ == "__main__":
    print(find_duplicate([9, 4, 5, 6, 3, 1, 2]))
