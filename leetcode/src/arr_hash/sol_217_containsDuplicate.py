class Solution:
	def containsDuplicate(self, nums: List[int]) -> bool:
		#array is empty
		if not nums:
			return False

		#store seen numbers for comparison
		seen = set()

		#iterate through give nums list and add to set
		for num in nums:
			#list contains duplicate
			if num in seen:
				return True
			#add to set
			seen.add(num)

		#no duplicate was found
		return False
	