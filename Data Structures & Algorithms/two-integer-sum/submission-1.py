class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        nums = [3,4,5,6]. target = 7
        seen = {
        3 : 0;
        4 : 1;
        5 : 2;
        6 : 3;
        }


        hashmap to s
        """

        seen = {}
        for i in range(len(nums)):
            targetMinusNums = target - nums[i]
            if targetMinusNums in seen:
                return [seen[targetMinusNums], i]
            else:
                seen[nums[i]] = i
        return "No pair found"

            


        