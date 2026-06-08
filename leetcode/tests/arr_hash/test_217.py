from sol_217_containsDuplicate import Solution

solver = Solution()

assert solver.containsDuplicate([1,2,3,1]) == True, "test 1 fail"

assert solver.containsDuplicate([1,2,3,4]) == False, "test 2 fail"

assert solver.containsDuplicate([1,1,1,3,3,4,3,2,4,2]) == True, "test 3 fail"

assert solver.containsDuplicate([]) == False, "test 4 fail"

assert solver.containsDuplicate([1]) == False, "test 5 fail"