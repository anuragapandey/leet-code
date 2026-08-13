# Given a string s, find the length of the longest substring without duplicate characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:

# 0 <= s.length <= 105
# s consists of English letters, digits, symbols and spaces.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}  # Maps character -> its most recent index
        left = 0
        max_length = 0
        
        for right, char in enumerate(s):
            # If char is repeated AND inside the current window, skip past its previous index
            if char in char_map and char_map[char] >= left:
                left = char_map[char] + 1
            
            # Store/update the last seen index of the character
            char_map[char] = right
            
            # Update the maximum length found so far
            max_length = max(max_length, right - left + 1)
            
        return max_length