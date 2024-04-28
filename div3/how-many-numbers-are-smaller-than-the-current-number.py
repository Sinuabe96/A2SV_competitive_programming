class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
         counts = [0] * 101  
         for num in nums:
             counts[num] += 1
        
         smaller_counts = [0] * len(nums)
         for i in range(len(nums)):
             smaller_counts[i] = sum(counts[:nums[i]])
        
         return smaller_counts
