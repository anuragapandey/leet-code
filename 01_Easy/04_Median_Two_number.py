# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

 

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

# Constraints:

# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106





class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Always binary search on the smaller array for O(log(min(m, n))) efficiency
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        half_len = (m + n + 1) // 2
        
        while low <= high:
            i = (low + high) // 2
            j = half_len - i
            
            # Boundary elements around partitions
            maxLeft1 = float('-inf') if i == 0 else nums1[i - 1]
            minRight1 = float('inf') if i == m else nums1[i]
            
            maxLeft2 = float('-inf') if j == 0 else nums2[j - 1]
            minRight2 = float('inf') if j == n else nums2[j]
            
            # Correct partition found
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # Odd total length: median is the maximum of the left partition
                if (m + n) % 2 == 1:
                    return float(max(maxLeft1, maxLeft2))
                # Even total length: median is average of middle two elements
                else:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
            
            # Too far right in nums1, shift binary search left
            elif maxLeft1 > minRight2:
                high = i - 1
            # Too far left in nums1, shift binary search right
            else:
                low = i + 1
                
        raise ValueError("Input arrays are not sorted.")