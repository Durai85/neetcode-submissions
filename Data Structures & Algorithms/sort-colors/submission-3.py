class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.mergeSort(nums,0,len(nums)-1)
        return nums

    def mergeSort(self,nums,left,right):
        if left >= right:
            return

        mid = (left + right) // 2
        self.mergeSort(nums,left,mid)
        self.mergeSort(nums,mid+1,right)
        self.merge(nums,left,mid,right)

    def merge(self,nums,left,mid,right):
        leftArr = nums[left:mid+1]
        rightArr = nums[mid+1:right+1]

        n1 = len(leftArr)
        n2 = len(rightArr)

        i = j = 0
        k = left

        while i < n1 and j < n2:
            if leftArr[i] <= rightArr[j]:
                nums[k] = leftArr[i]
                i += 1
                k += 1

            else:
                nums[k] = rightArr[j]
                j += 1
                k += 1


        while i < n1:
            nums[k] = leftArr[i]
            i += 1
            k += 1

        while j < n2:
            nums[k] = rightArr[j]
            j += 1
            k += 1

            