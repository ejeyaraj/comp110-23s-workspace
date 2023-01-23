"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730569503"

word = input("Enter a 5-character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
character = input("Enter a single character: ")
if len(character) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + character + " in " + word)

instance_count = 0
if character == word[0]:
    print(character + " found at index 0")
    instance_count = instance_count + 1
if character == word[1]:
    print(character + " found at index 1")
    instance_count = instance_count + 1
if character == word[2]:
    print(character + " found at index 2")
    instance_count = instance_count + 1
if character == word[3]:
    print(character + " found at index 3")
    instance_count = instance_count + 1
if character == word[4]:
    print(character + " found at index 4")
    instance_count = instance_count + 1
else:
    instance_count = instance_count + 0

if instance_count == 1:
    print(str(instance_count) + " instance of " + character + " found in " + word)
if instance_count == 0:
    print("No instances of " + character + " found in " + word)
if instance_count > 1:
    print(str(instance_count) + " instances of " + character + " found in " + word)

