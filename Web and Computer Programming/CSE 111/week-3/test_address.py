from address import extract_city, extract_state, extract_zipcode
import pytest

def test_extract_city():
    """
    verify that extract_city works correctly
    parameters: none
    returns: none
    """
    
    # Test case 1
    assert extract_city("525 S Center St, Rexburg, ID 83460") == "Rexburg"
    
    # Test case 2
    assert extract_city("525 S Center St, Provo, UT 84602") == "Provo"


def test_extract_state():
    pass


def test_extract_zipcode():
    pass

# Run the tests
pytest.main(["-v", "--tb=line", __file__])