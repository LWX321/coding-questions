from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """Solution using 2 pointer approach."""
        # take care of the base case
        if len(height) <= 2:
            return 0

        # first element is the highest elevation seen in the left
        left = 0
        left_max = height[left]

        # last element is the highest elevation seen in the right
        right = len(height) - 1
        right_max = height[right]

        # init total amount
        amt = 0

        # loop till left and right are not the same
        while (left != right):

            if height[left] <= height[right]:
                # if the left elevation is lower than the right elevation
                # then that's where water can be trapped
                # the amount of water that can be trapped is the difference of 
                # the max left height seen so far - current height of left.
                # move pointer 1 position ahead
                amt = amt + (left_max - height[left])
                left_max = max(left_max, height[left + 1])
                left = left + 1
            else:
                # if the right elevation is lower than the left elevation
                # then that's where water can be trapped
                # the amount of water that can be trapped is the difference of 
                # the max right height seen so far - current height of right.
                # move pointer 1 position ahead
                amt = amt + (right_max - height[right])
                right_max = max(right_max, height[right - 1])
                right = right - 1
        
        return amt
