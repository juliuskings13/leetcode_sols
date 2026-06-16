import pytest
from arr_hash.sol_49_groupAnagrams import Solution
from pytest_unordered import unordered

@pytest.fixture
def tester():
	return Solution()

@pytest.mark.parametrize ("strs, expected", [
	([""],[[""]]),
	(["a"], [["a"]]),
	(["eat", "tea", "tan"], [["eat", "tea"],["tan"]]),
	(["eat","tea","tan","ate","nat","bat"], [["bat"],["nat","tan"],["ate","eat","tea"]])

	])

def test_groupAnagrams(tester, strs, expected):
	assert tester.groupAnagrams(strs) == unordered([unordered(group) for group in expected])