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