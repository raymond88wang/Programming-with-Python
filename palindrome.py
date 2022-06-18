def is_palindrome_iterative(str):
    str_len = len(str)
    for i in range(0, (int)((str_len + 1) / 2)):
        if str[i] != str[str_len - i - 1]:
            return False
    return True

print([is_palindrome_iterative(i) for i in ["aabbaa", "a", "", "aabba", "abcabc"]])

# def is_palindrome_recursive(str):
#     if str == "":
#         return True
#     elif str[0] != str[len(str) - 1]:
#         return False
#     else:
#         return True and is_palindrome_recursive(str[1:len(str) - 1])

#Memory optimized
def is_palindrome_recursive(str):
    def is_palindrome(str, left_index, right_index):
        if left_index >= right_index:
            return True
        elif str[left_index] != str[right_index]:
            return False
        else:
            return True and is_palindrome(str, left_index + 1, right_index - 1)
    return is_palindrome(str, 0, len(str) - 1)



print([is_palindrome_recursive(i) for i in ["aabbaa", "a", "", "aabba", "abcabc"]])
