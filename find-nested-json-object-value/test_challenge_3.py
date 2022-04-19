import pytest
from challenge_3 import find_key_value

@pytest.mark.parametrize("dict_object,input_key,expected_value",[({"a":{"b":{"c":"d"}}},"a/b",None)])
def test_case_1(dict_object,input_key,expected_value):
    """
    Test case for passing valid object key, return None if input key is not a/b/c
    """
    assert find_key_value(dict_object,input_key) == expected_value

@pytest.mark.parametrize("dict_object,input_key,expected_value",[({"a":{"b":{"c":"d"}}},"a/b/c","d")])
def test_case_2(dict_object,input_key,expected_value):
    """
    Test case for passing valid object key, return value d if input key is a/b/c
    """
    assert find_key_value(dict_object,input_key) == expected_value

@pytest.mark.parametrize("dict_object,input_key,expected_value",[({"a":{"b":{"c":"d"}}},"d","Key Not Found")])
def test_case_3(dict_object,input_key,expected_value):
    """
    Test case for passing object value, return key Not Found message  if input key is d
    """
    assert find_key_value(dict_object,input_key) == expected_value

@pytest.mark.parametrize("dict_object,input_key,expected_value",[({"a":{"b":{"c":"d"}}},"","Key Not Found")])
def test_case_4(dict_object,input_key,expected_value):
    """
    Test case for passing object value, return key Not Found message  if input key is empty
    """
    assert find_key_value(dict_object,input_key) == expected_value

@pytest.mark.parametrize("dict_object,input_key,expected_value",[({"a":{"b":{"c":"d"}}},"x","Key Not Found")])
def test_case_5(dict_object,input_key,expected_value):
    """
    Test case for passing object value, return key Not Found message  if input key is unknown value(x)
    """
    assert find_key_value(dict_object,input_key) == expected_value

@pytest.mark.parametrize("dict_object,input_key,expected_value",[({"a":{"b":{"c":"d"}}}," ","Key  Found")])
def test_case_6(dict_object,input_key,expected_value):
    """
    Test case for handling AssertionError exception in test,
    """
    with pytest.raises(AssertionError):
        assert find_key_value(dict_object,input_key) == expected_value

