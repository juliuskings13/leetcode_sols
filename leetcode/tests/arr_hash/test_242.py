from sol_242_validAnagram import Solution

solver = Solution()

#not needed as strings cannot be empty
#assert solver.isAnagram("", "") , "test 1 fail"

assert solver.isAnagram("", "a") == False, "test 2 fail"

assert solver.isAnagram("anagram", "nagaram") == True, "test 3 fail"

assert solver.isAnagram("rat", "car") == False, "test 4 fail"