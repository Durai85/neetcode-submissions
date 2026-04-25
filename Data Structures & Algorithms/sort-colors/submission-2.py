class Solution:
    def sortColors(self, nums: List[int]) -> None:
        self.mergeSort(nums, 0, len(nums)-1)

    def mergeSort(self, nums, left, right):
        if left < right:
            mid = left + (right - left) // 2
            
            self.mergeSort(nums, left, mid)
            self.mergeSort(nums, mid+1, right)

            self.merge(nums, left, mid, right)
        
    def merge(self, nums, left, mid, right):
        
        nums1 = nums[left : mid+1]
        nums2 = nums[mid+1 : right+1]

        n1 = len(nums1)
        n2 = len(nums2)

        i = j = 0
        k = left

        while i < n1 and j < n2:
            if nums1[i] <= nums2[j]:
                nums[k] = nums1[i]
                i += 1
            else :
                nums[k] = nums2[j]
                j += 1
            k += 1

        while i < n1:
            nums[k] = nums1[i]
            k += 1
            i += 1

        while j < n2:
            nums[k] = nums2[j]
            k += 1
            j += 1

        