class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Always binary search on the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        left = 0
        right = m

        while left <= right:
            partition1 = (left + right) // 2
            partition2 = (m + n + 1) // 2 - partition1

            # Values around the partitions
            max_left1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            min_right1 = float('inf') if partition1 == m else nums1[partition1]

            max_left2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            min_right2 = float('inf') if partition2 == n else nums2[partition2]

            # Correct partition
            if max_left1 <= min_right2 and max_left2 <= min_right1:

                # Odd total length
                if (m + n) % 2 == 1:
                    return max(max_left1, max_left2)

                # Even total length
                return (
                    max(max_left1, max_left2)
                    + min(min_right1, min_right2)
                ) / 2.0

            # Move binary search left
            elif max_left1 > min_right2:
                right = partition1 - 1

            # Move binary search right
            else:
                left = partition1 + 1
                
