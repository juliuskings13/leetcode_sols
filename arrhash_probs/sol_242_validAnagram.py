class Solution:
	def isAnagram(self, s:str, t: str) -> bool:
		#create char freq map for each string
		sCharCount, tCharCount = [0]*26, [0]*26

		#strings aren't same length
		if len(s) != len(t):
			return False

		#fill freq map for each string	
		for chr in s:
			sCharCount[ord(chr) - ord('a')] += 1

		for chr in t:
			tCharCount[ord(chr) -ord('a')] +=1

		#compare freq maps
		if tCharCount == sCharCount:
			return True
		else:
			return False

		#jfc, ill j use Counter class next time
		#return Counter(s) == Counter (t)