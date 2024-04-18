class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result=[]
        for i in range(len(nums)):
            count=0
            for j in range(len(nums)):
                if i!=j and nums[i]>nums[j]:
                    count+=1
            result.append(count)   
        return result
