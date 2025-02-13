from collections import Counter

def findFirstUnique(s: str) -> int:
    counter = Counter(s)  # Count occurrences of each character

    for char in s:
      if counter[char] == 1:
        return s.index(char) + 1  # Return the 1-based index of the first unique character
    
    return -1


s = "statistics"
print(findFirstUnique(s))