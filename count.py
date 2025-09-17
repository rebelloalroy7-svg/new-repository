# Python program to count vowels in a sentence

s = input("Enter a sentence: ")
vowels = "aeiouAEIOU"
count = sum(1 for char in s if char in vowels)

print("Number of vowels:", count)
