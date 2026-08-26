class Solution:
    def search(self, nums, target):
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            
            if nums[mid] == target:
                return True

            # Left half is sorted
            if nums[lo] < nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            # Right half is sorted
            elif nums[lo] > nums[mid]:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
            else:
                lo += 1

        return False


# class Solution:
#     def search(self, nums: List[int], target: int) -> bool:
#         l, r = 0, len(nums) - 1
#         while l <= r:
#             m = l + (r - l) // 2
#             if nums[m] == target:
#                 return True

#             if nums[l] < nums[m]:  # Left portion
#                 if nums[l] <= target < nums[m]:
#                     r = m - 1
#                 else:
#                     l = m + 1
#             elif nums[l] > nums[m]:  # Right portion
#                 if nums[m] < target <= nums[r]:
#                     l = m + 1
#                 else:
#                     r = m - 1
#             else:
#                 l += 1

#         return False
