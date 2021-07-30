import pytest
from binary_search import search


def test_binarysearch():
    array = [1,1,2,3,5,8,13,21,34,55] # len array = 10

    assert search(array, 8) == 5
    assert search(array, 5) == 4
    assert search(array, 55) == 9
    assert (search(array, 1) == 1) or (search(array, 1) == 0)
    assert search(array, 10) == None
