class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #anagram will contain same characters (same number of each individual character) but just different numbers

        if len(s) != len(t):
            return False

        if sorted(s) == sorted(t):
            return True
        else:
            return False
    