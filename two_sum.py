class Solution:
    def two_sum(self, nums, target):
	"""

	Args:
		nums:
		target:

	Returns:

	"""
	hashmap = {}
	for i in range (len(nums)):
		if (target - nums[i]) not in hashmap:
			hashmap[nums[i]] = i
		else:
			return [i, hashmap[target-nums[i]]]
