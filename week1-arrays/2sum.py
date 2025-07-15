# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for val in nums:
#             print(val)
        
def twoSum(nums,target):
    for i in range(len(nums)):
        for k in range(i+1,len(nums)):
            if nums[i] == target - nums[k]:
                return[i,k]
        return [] 
solution = twoSum([3,4,5,7,],10)
print(solution)       
