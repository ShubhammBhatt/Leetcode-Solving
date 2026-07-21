class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        zero_groups = []
        n = len(s)
        i = 0
        while i < n:
            if s[i] == '0':
                j = i
                while j < n and s[j] == '0':
                    j += 1
                zero_groups.append(j - i)
                i = j
            else:
                i += 1
                
        if len(zero_groups) < 2:
            return s.count('1')
            
        max_merge = 0
        for i in range(len(zero_groups) - 1):
            max_merge = max(max_merge, zero_groups[i] + zero_groups[i + 1])
            
        return s.count('1') + max_merge