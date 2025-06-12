import pytest
from prime import generate_prime_factors

def test_non_integer_input_raises_value_error():
    with pytest.raises(ValueError):
        generate_prime_factors("not an int")
    with pytest.raises(ValueError):
        generate_prime_factors(3.14)


def test_prime_factors_of_one_returns_empty_list():
    assert generate_prime_factors(1) == []