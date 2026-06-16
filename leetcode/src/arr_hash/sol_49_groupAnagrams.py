class Solution:
	def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
		
		if not strs or strs == [""]:
			return [[""]]

		ans = dict()

		for s in strs:
			freq = [0] * 26

			for c in s:
				freq[ord(c) - ord('a')] += 1

			ans.setdefault(tuple(freq), []).append(s)

		return list(ans.values())