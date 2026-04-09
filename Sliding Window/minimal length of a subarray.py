class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        cur = 0
        minm_len = len(nums) + 1  
        for i in range(len(nums)):
            cur += nums[i]
            
            while cur >= target:
                minm_len = min(minm_len, i - l + 1)
                cur -= nums[l]
                l += 1
        
        return 0 if minm_len == len(nums) + 1 else minm_len
