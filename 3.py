import re

# Function to count the vowels
def count_vowels(Input):
    vowels = re.findall("[aiueo]",Input)
    Output = len(vowels)
    return Output

# Main program
Input = str(input("Input\t\t:"))
Output = count_vowels(Input)
print("Count Vowels\t:",Output)
