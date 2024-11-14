def is_palindrome(word):
    word = "".join(
        [char for char in word.lower() if char.isalnum()]
    )  # Clean up the input
    reversed_word = word[::-1]  # Reverse the cleaned word
    return (
        word == reversed_word
    )  # Check if original and reversed word are the same


palindrome_check = is_palindrome("racecar")
print(palindrome_check)  # Should print True
