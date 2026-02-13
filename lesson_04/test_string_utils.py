import pytest
from string_utils import StringUtils

string_utils = StringUtils()

# утилита 1
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

# утилита 2
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("  gohome", "gohome"), (" hello ", "hello "),
    ("  Hello world", "Hello world"),
    ("   abc   ", "abc   ")
])

def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("   ", "   "),
    ("no leading spaces", "no leading spaces")
])

def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected

# утилита 3
@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Gohome", "o", True), ("Привет", "р", True),
    ("Hello, world", "H", True),
    ("aaaaa", "a", True)
])

def test_contains_positive(input_str, symbol, expected):
        assert string_utils.contains(input_str, symbol) == expected
  
@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Hello", "K", False), ("abc", None, False),
    ("", "a", False),("", "", False),
    (None, "abc", False)
])

def test_contains_negative(input_str, symbol, expected):
    if input_str is None:
        with pytest.raises(TypeError):
            string_utils.contains(input_str, symbol)
    else:
        assert string_utils.contains(input_str, symbol) == expected

# утилита 4
@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Game", "m"), ("Привет", "рив"),
    ("banana", "a"), ("", "a"), ("Hello World", " "),
    ("Hello", "X"), ("aaaaaa", "a"), ("SkyPro", "S")
])

def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.del_sym(input_str, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    (None, "K"), ("abc", None),
    (123, "k"),("", "", False),
    (None, "abc", False)
])

def test_delete_symbol_negative(input_str, symbol, expected):
     with pytest.raises(TypeError):
        string_utils.delete_symbol(input_str, symbol)

