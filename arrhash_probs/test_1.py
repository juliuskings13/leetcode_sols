from sol_1_twoSum import Solution

solver = Solution()

assert 	set(solver.twoSum([2,7,11,15], 9)) == {0,1}, "test 1 fail"

assert set(solver.twoSum([3,2,4], 6)) == {1,2}, "test 2 fail"

assert set(solver.twoSum([3,3],6)) == {0,1}, "test 3 fail"