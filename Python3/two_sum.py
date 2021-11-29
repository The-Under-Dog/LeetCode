class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}        
        for i in range(len(nums)):
            j = target - nums[i]
            if j not in d:
                d[nums[i]] = i
            else:
                return [d[j], i]
