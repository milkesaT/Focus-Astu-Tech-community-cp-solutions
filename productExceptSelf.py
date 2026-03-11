class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = []
        product = 1
        zero_count = 0

        for n in nums:
            if n == 0:
                zero_count += 1
            else:
                product *= n

        for i in range(len(nums)):
            if zero_count > 1:
                arr.append(0)
            elif zero_count == 1:
                if nums[i] == 0:
                    arr.append(product)
                else:
                    arr.append(0)
            else:
                arr.append(product // nums[i])

        return arr
