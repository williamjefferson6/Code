class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while True:
            if val in nums:
                i = nums.index(val)
                nums.remove(nums.index(val))
            else:
                break

        return (len(nums))