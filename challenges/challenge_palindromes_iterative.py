def is_palindrome_iterative(word):
    if not isinstance(word, str) or word == "":
        return False

    mid = len(word) // 2

    for index in range(mid):
        if word[index] != word[len(word) - 1 - index]:
            return False
    return True


if __name__ == "__main__":
    print(is_palindrome_iterative("oiio"))
