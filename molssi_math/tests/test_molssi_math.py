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


@pytest.fixture
def num_list_3():
    return [1, 2, 3, 4, 5]


@pytest.mark.parametrize("num_list, expected_mean", [
    ([1, 2, 3, 4, 5], 3),
    ([0, 2, 4, 6], 3),
    ([1, 2, 3, 4], 2.5),
    (list(range(1, 1000000)), 1000000/2)
])
def test_many(num_list, expected_mean):
    assert molssi_math.mean(num_list) == expected_mean


@pytest.mark.parametrize("x", [0, 1])
@pytest.mark.parametrize("y", [2, 3])
def test_foo(x, y):
    pass


def test_title_case_type_error():
    test_sentence = [1, 2, 3, 4]
    with pytest.raises(TypeError):
        molssi_math.title_case(test_sentence)


def test_title_case_empty_string_error():
    test_sentence = ''
    with pytest.raises(ValueError):
        molssi_math.title_case(test_sentence)


@pytest.mark.parametrize("test_sentence, expected", [
                         ("ThIs iS a STring to be ConverteD.",
                          "This Is A String To Be Converted."),
                         ("a", "A"),
                         ("hEllo WORLD!", "Hello World!")
                         ])
def test_title_case(test_sentence, expected):
    observed = molssi_math.title_case(test_sentence)
    assert observed == expected
