print("Welcome to Palindrome Checker!\n")

word = input("Please enter a word to check if it is a Palindrome: ")
# print(word[0], word[1], word[2], word[3])

# Remove spaces and convert to lowercase for case-insensitive comparison
word = word.replace(" ", "").lower()
# print(word)

# Create a reversed copy of the word
reverse_word = word[::-1]
# print(reverse_word)

if word == reverse_word:
    print("Congratulations. You found a palindrome!")
else:
    print("You failed :( . Please try again.")
