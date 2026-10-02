# Ask for a word and print whether it's a palindrome using slicing

word = input("GIMME A WORD: ")

print(word[::] == word[::-1])