from collections import Counter

class Solution:
    def isAnagram(self, string1: str, string2: str) -> bool:
        return Counter(string1) == Counter(string2) 
        
