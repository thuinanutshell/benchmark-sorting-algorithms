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
        "empty": [],
        "single": [42],
        "duplicates": [3, 1, 4, 1, 5, 9, 2, 6, 5],
    }


class TestCorrectness:
    def test_empty_array(self, sorting_algorithm):
        """Test with empty array - runs for ALL algorithms automatically"""
        result = sorting_algorithm([])
        assert result == []

    def test_single_element(self, sorting_algorithm):
        """Test with single element - runs for ALL algorithms automatically"""
        result = sorting_algorithm([42])
        assert result == [42]

    def test_duplicates(self, sorting_algorithm, test_data):
        """Test with duplicate elements"""
        result = sorting_algorithm(test_data["duplicates"].copy())
        expected = sorted(test_data["duplicates"])
        assert result == expected
