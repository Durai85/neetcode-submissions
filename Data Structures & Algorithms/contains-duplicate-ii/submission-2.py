class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        win = set()
        i = 0
        for j in range(len(nums)):
            if nums[j] in win:
                return True
            win.add(nums[j])
            if len(win) > k:
                win.remove(nums[i])
                i += 1
        return False