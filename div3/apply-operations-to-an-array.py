class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
         n = len(nums)
         for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        
         zero_count = nums.count(0)
         non_zero_nums = [num for num in nums if num != 0]
         result = non_zero_nums + [0] * zero_count
        
         return result
