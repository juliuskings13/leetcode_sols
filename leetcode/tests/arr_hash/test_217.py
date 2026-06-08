import pytest
from arr_hash.sol_217_containsDuplicate import Solution

@pytest.fixture
def tester():
	return Solution()

@pytest.mark.parametrize("nums, trueFalse", [
	([1,2,3,1],True),
	([1,2,3,4], False),
	([1,1,1,3,3,4,3,2,4,2], True),
	([], False),
	([1], False)
])

def testContDupe(tester, nums, trueFalse):
	assert tester.containsDuplicate(nums) == trueFalse

