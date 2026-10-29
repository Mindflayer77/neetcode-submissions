from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        key_to_anagrams = defaultdict(list)
        for s in strs:
            key_to_anagrams["".join(sorted(s))].append(s)
        return list(key_to_anagrams.values())
