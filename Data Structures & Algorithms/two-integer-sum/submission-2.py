class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        i = 0
        nums = [4,5,6]
        target = 10

        visited = {4:0 , 5:1 , 6 }

        """

        visited = {}

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in visited:
                return [visited[difference],i]
            else:
                visited[nums[i]] = i


        