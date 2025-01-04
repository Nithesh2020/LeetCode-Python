class Solution:
    def twoSum(self, nums: list[int], target: int):
        numMap = {}
        n = len(nums)
        for i in range(n):
            comp = target - nums[i]
            if comp in numMap:
                return [numMap[comp],i]
            numMap[nums[i]] = i
                
s = Solution()
nums = list(map(int,(input().strip("[]")).split(",")))
target = int(input())
x = s.twoSum(nums,target)
