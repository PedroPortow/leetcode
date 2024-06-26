# Retorna os indices dos numeros que somam o target


class Solution(object):
    
	# O(n^2)
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):        
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                
solution = Solution()
sum = solution.twoSum([2,7,11,15], 9)
print(sum)