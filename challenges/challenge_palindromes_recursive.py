def is_palindrome_recursive(word, low_index, high_index):
    if not isinstance(word, str) or word == "":
        return False

    if low_index == high_index:
        return True

    if low_index + 1 == high_index:
        return word[low_index] == word[high_index]

    if word[low_index] == word[high_index]:
        return True and is_palindrome_recursive(
            word, low_index + 1, high_index - 1
        )


if __name__ == "__main__":
    word = "OiiO"
    print(is_palindrome_recursive(word, 0, len(word) - 1))
