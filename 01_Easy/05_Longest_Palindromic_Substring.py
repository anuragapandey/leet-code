# Given a string s, return the longest palindromic substring in s.

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.



class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        start, max_len = 0, 0
        
        def expand(left: int, right: int) -> tuple[int, int]:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # After exiting, valid palindrome is between left + 1 and right - 1
            # Length = (right - 1) - (left + 1) + 1 = right - left - 1
            return left + 1, right - left - 1

        for i in range(len(s)):
            # Check odd-length palindrome centered at i
            l1, len1 = expand(i, i)
            if len1 > max_len:
                start, max_len = l1, len1
            
            # Check even-length palindrome centered at i and i + 1
            l2, len2 = expand(i, i + 1)
            if len2 > max_len:
                start, max_len = l2, len2
                
        return s[start:start + max_len]