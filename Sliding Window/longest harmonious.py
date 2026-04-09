class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        long=0
        v=0
        for i in range(len(nums)):
            while(nums[i]-nums[v]>1):
                v+=1
            if(nums[i]-nums[v]==1):
                long=max(long,i-v+1)
        return long
                     
            
