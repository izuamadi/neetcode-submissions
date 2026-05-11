class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        nums = [1,2,3,4]
        
                
        output: false
        '''

        hashset = set()

        for i in range(len(nums)):
            if nums[i] in hashset:
                return True
            hashset.add(nums[i])
        return False

        


        