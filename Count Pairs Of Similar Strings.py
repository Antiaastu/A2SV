class Solution:
    def similarPairs(self, words: List[str]) -> int: 
        di= defaultdict(int)
        for i in range(len(words)):
            ww = "".join(sorted(set(words[i])))
            if ww in di:
                di[ww]+=1
            else:
                di[ww]=1

        ans = 0
        for i in di:
            n=di[i]
            ans+=(n*(n-1))//2
        
        return ans
