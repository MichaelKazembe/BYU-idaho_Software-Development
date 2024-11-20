from names import make_full_name, extract_family_name, extract_given_name 
import pytest

def test_make_full_name():
    """
    Verify that the make_full_name function works correctly.
    Parameters: none
    Return: nothing
    """
    # Call the make_full_name function and verify that it returns a string.
    full_name = make_full_name("Karen", "Kazembe")
    assert isinstance(full_name, str), "make_full_name function must return a string"

    # Call the make_full_name function eight times and use an assert
    # statement to verify that the string returned by the
    # make_full_name function is correct each time.
    
    assert make_full_name("", "") == "; " # empty strings
    assert make_full_name("Karen", "Kazembe") == "Kazembe; Karen" # normal case
    assert make_full_name("Karen", "") == "; Karen" # empty family name
    assert make_full_name("", "Kazembe") == "Kazembe; " # empty given name
    assert make_full_name("Bob", "Smith") == "Smith; Bob" # short names
    assert make_full_name("Chilembalemba", "Zingwangwa") == "Zingwangwa; Chilembalemba" # long names
    assert make_full_name("Mwiza", "Kazembe-Kuluwani") == "Kazembe-Kuluwani; Mwiza" # hyphenated family name
    assert make_full_name("Mwiza-Theresa", "Kuluwani") == "Kuluwani; Mwiza-Theresa" # hyphenated given name  
    
    
def test_extract_family_name():
    """
    verify that the extract_family_name function works correctly.
    Parameters: none
    Return: nothing
    """
    
    # Call the extract_family_name function and verify that it returns a string.
    family_name = extract_family_name("Kazembe; Karen")
    assert isinstance(family_name, str), "extract_family_name function must return a string"
    
    # Call the extract_family_name function eight times and use an assert
    # statement to verify that the string returned by the
    # extract_family_name function is correct each time.
    
    assert extract_family_name("; ") == "" # empty strings
    assert extract_family_name("Kazembe; Karen") == "Kazembe" # normal case
    assert extract_family_name("Kazembe; ") == "Kazembe" # empty given name
    assert extract_family_name("; Karen") == "" # empty family name
    assert extract_family_name("Smith; Bob") == "Smith" # short names
    assert extract_family_name("Zingwangwa; Chilembalemba") == "Zingwangwa" # long names
    assert extract_family_name("Kazembe-Kuluwani; Mwiza") == "Kazembe-Kuluwani" # hyphenated family name
    assert extract_family_name("Kuluwani; Mwiza-Theresa") == "Kuluwani" # hyphenated given name
    

def test_extract_given_name():
    """ 
    verify that the extract_given_name function works correctly.
    Parameters: none
    Return: nothing
    """
    
    # Call the extract_given_name function and verify that it returns a string.
    given_name = extract_given_name("Kazembe; Karen")
    assert isinstance(given_name, str), "extract_given_name function must return a string"
    
    # Call the extract_given_name function eight times and use an assert
    # statement to verify that the string returned by the
    # extract_given_name function is correct each time.
    
    assert extract_given_name("; ") == "" # empty strings
    assert extract_given_name("Kazembe; Karen") == "Karen" # normal case
    assert extract_given_name("Kazembe; ") == "" # empty given name
    assert extract_given_name("; Karen") == "Karen" # empty family name
    assert extract_given_name("Smith; Bob") == "Bob" # short names
    assert extract_given_name("Zingwangwa; Chilembalemba") == "Chilembalemba" # long names
    assert extract_given_name("Kazembe-Kuluwani; Mwiza") == "Mwiza" # hyphenated family name
    assert extract_given_name("Kuluwani; Mwiza-Theresa") == "Mwiza-Theresa" # hyphenated given name


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])