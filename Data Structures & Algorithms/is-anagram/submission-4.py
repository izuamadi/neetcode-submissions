class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        "if the strings do not have the same length they cannot be anagrams"

        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)
        