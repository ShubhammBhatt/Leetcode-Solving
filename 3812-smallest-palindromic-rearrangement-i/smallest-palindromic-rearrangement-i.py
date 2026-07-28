class Solution:
    def smallestPalindrome(self, s: str) -> str:
        half_len = len(s) // 2
        
        first_half = sorted(s[:half_len])
        
        if len(s) % 2 == 1:
            mid_char = s[half_len]
        else:
            mid_char = ""
            
        return "".join(first_half) + mid_char + "".join(first_half[::-1])