class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        looking = {} #[num] -> idx

        for idx, num in enumerate(nums):
            if num in looking:
                return [looking[num],idx]
            else:
                looking[target-num] = idx
        