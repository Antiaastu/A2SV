class Solution:
    def freqAlphabets(self, s: str) -> str:
        result = []
        i = 0
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == '#':
                result.append(chr(96 + int(s[i:i + 2])))
                i += 3
            else:
                result.append(chr(96 + int(s[i])))
                i += 1

        return ''.join(result)
