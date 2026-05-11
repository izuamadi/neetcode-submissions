class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        nums = [1,2,3,4]
        
                
        output: false
        '''
        i = 0
        while i < len(nums):
            x = nums.pop(i)
            if x in nums:
                return True
        return False

        


        