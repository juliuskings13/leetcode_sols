import pytest
from arr_hash.sol_242_validAnagram import Solution

@pytest.fixture
def tester(): 
	return Solution()

@pytest.mark.parametrize("s, t, trueFalse", [
	("", "a", False),
	("anagram", "nagaram", True),
	("rat", "car", False)
])

def testIsAnagram(tester, s, t, trueFalse):
	assert tester.isAnagram(s, t) == trueFalse