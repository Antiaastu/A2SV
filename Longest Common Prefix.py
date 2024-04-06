class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = strs[0]
        pre_len = len(pre)

        for s in strs[1:]:
            while pre != s[0:pre_len]:
                pre_len -= 1
                if pre_len == 0:
                    return ""
                
                pre = pre[0:pre_len]
        
        return pre
