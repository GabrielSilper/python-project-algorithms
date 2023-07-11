def merge_sort_str(array, start=0, end=None):
    if end is None:
        end = len(array)
    if end - start > 1:
        mid = (end + start) // 2
        merge_sort_str(array, start, mid)
        merge_sort_str(array, mid, end)
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


def is_anagram(first_string, second_string):
    is_equal = False
    if not isinstance(first_string, str) or not isinstance(second_string, str):
        return first_string, second_string, is_equal

    first_string = list(first_string.lower())
    second_string = list(second_string.lower())

    merge_sort_str(first_string)
    merge_sort_str(second_string)
    first_string = "".join(first_string)
    second_string = "".join(second_string)
    if first_string != "" and second_string != "":
        is_equal = first_string == second_string

    return first_string, second_string, is_equal


if __name__ == "__main__":
    print(is_anagram("", ""))
