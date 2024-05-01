class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans=[]
        n=len(arr)
        for i in range(n,0,-1):
            index=arr.index(i)
            if index==i-1:
                continue
            if index!=0:
                arr[:index+1]=reversed(arr[:index+1])
                ans.append(index + 1)
            arr[:i]=reversed(arr[:i])
            ans.append(i)
        return ans
