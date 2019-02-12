"""
Unit and regression test for the molssi_math package.
"""

# Import package, test suite, and other packages as needed
import molssi_math
import pytest
import sys


def test_molssi_math_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "molssi_math" in sys.modules


def test_mean():
    num_list = [1, 2, 3, 4, 5]
    observed = molssi_math.mean(num_list)
    expected = 3

    assert expected == observed


def test_mean_type_error():
    test_variable = 'This is a test string'

    with pytest.raises(TypeError):
        molssi_math.mean(test_variable)


@pytest.mark.my_test
# @pytest.mark.my_test
def test_zero_length():
    test_list = []

    with pytest.raises(ValueError):
        molssi_math.mean(test_list)
