import re

# Function to replace a character
def replaceword(Input):
    oldchar = str(input("Old Char\t:"))
    replace = str(input("Rplace\t\t:"))
    Output = re.sub(oldchar,replace,Input)
    return Output

#  Main program
Input = str(input("Input\t\t:"))
Output = replaceword(Input)
print("Output\t\t:",Output)
