class Solution:

    """
    Given an array of integers nums and an integer target, return indices of the two numbers 
    such that they add up to target. You may assume that each input would have exactly one 
    solution, and you may not use the same element twice. You can return the answer in any order.
    """

    def twoSum1(self, nums: list[int], target: int) -> list[int]:
        # with prints
        for i in range(len(nums) - 1):
            print(nums[i])
            for j in range(i+1, len(nums)):
                print(nums[j])
                print("sum of nums[i] + nums[j] =", nums[i] + nums[j])
                if nums[i] + nums[j] == target:
                    return [i, j]
                    break

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            
            for j in range(i + 1, len(nums)):
                
                if nums[i] + nums[j] == target:
                    return [i, j]
                    break

if __name__=="__main__":
    a = Solution()
    # print(a.twoSum([7, 8, 2, 11, 3, 4, 5], 6))
    print(a.twoSum([3, 2, 4], 6))