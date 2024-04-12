class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n=len(nums)
        for i in range(n-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
        zero_index = 0
        for i in range(n):
            if nums[i] != 0:
                nums[zero_index] = nums[i]
                if zero_index != i:
                    nums[i] = 0
                zero_index += 1
        
        return nums
