def is_palindrome():
    word = input("Enter a word to see if it's a palindrome: ")
    if word == sorted(word, key=None, reverse=True):
        print("Output: True")
        print(f"Explanation: {word} reads the same forward and backward, making it a palindrome.")
    else:
        print("Output: False")
        print(f"Explanation: {word} does not read the same forward and backward, making it not a palindrome.")

is_palindrome()
