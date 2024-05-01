class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
         sort=sorted(nums)
         arr=[]
         for i in range(len(nums)):
            if sort[i]==target:
                arr.append(i)
         return arr
