class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        use a hashset to store the numbers we have seen
        if number in hashset return true; else we add the number to the hashset
        if we go through array and do not find any numbers we have already seen return false
        """

        seen = set()

        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            else:
                seen.add(nums[i])

        return False