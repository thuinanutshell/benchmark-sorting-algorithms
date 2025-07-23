import pytest
from algorithms import ALL_ALGORITHMS


@pytest.fixture(
    params=[alg[1] for alg in ALL_ALGORITHMS], ids=[alg[0] for alg in ALL_ALGORITHMS]
)
def sorting_algorithm(request):
    """Fixture that parametrizes tests across all sorting algorithms"""
    return request.param


# Fixture for test data
@pytest.fixture
def test_data():
    """Fixture providing various test cases"""
    return {
        "sorted": [1, 2, 3, 4, 5],
        "reverse": [5, 4, 3, 2, 1],
        "random": [64, 34, 25, 12, 22, 11, 90],
        "negative": [-3, -1, -4, -1, -5],
    }


class TestCorrectness:
    def test_sorted_array(self, sorting_algorithm, test_data):
        """Test with already sorted array"""
        result = sorting_algorithm(test_data["sorted"].copy())
        assert result == [1, 2, 3, 4, 5]

    def test_reverse_sorted(self, sorting_algorithm, test_data):
        """Test with reverse sorted array"""
        result = sorting_algorithm(test_data["reverse"].copy())
        assert result == [1, 2, 3, 4, 5]

    def test_negative_numbers(self, sorting_algorithm, test_data):
        """Test with negative numbers"""
        result = sorting_algorithm(test_data["negative"].copy())
        expected = sorted(test_data["negative"])
        assert result == expected

    @pytest.mark.parametrize("size", [10, 100, 1000])
    def test_random_data(self, sorting_algorithm, size):
        """Test with random data of different sizes"""
        import random

        data = [random.randint(1, 1000) for _ in range(size)]
        result = sorting_algorithm(data.copy())
        expected = sorted(data)
        assert result == expected
