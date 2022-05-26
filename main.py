# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram():
    # [assignment] Add your code here
    
    firstString = str(input("Enter your first string here: "))
    secondString = str(input("Enter your second string here: "))
    
    if(sorted(firstString.upper()) == sorted(secondString.upper())):
        return True
        
    else:
        return False
        
checkAnagram = find_anagram()

print(checkAnagram)