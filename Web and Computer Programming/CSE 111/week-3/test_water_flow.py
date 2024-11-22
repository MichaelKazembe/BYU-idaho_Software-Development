"""
test_water_flow.py

Program that tests the water_flow.py program that calculates the height of a column of water,
the pressure caused by a column of water, and the pressure loss from friction in a pipe.

"""

from pytest import approx
import pytest
from water_flow import water_column_height, \
    pressure_loss_from_pipe, \
    pressure_gain_from_water_height, \
    pressure_loss_from_fittings, \
    reynolds_number, \
    pressure_loss_from_pipe_reduction, \
    convert_kpa_to_psi
    
def test_water_column_height():
    """
    verify that water_column_height works correctly
    parameters: none
    returns: none
    """
    
    # Test the water_column_height function at least four times
    # with different inputs and assert that the function returns
    
    assert water_column_height(0.0, 0.0) == approx(0.0) 
    assert water_column_height(0.0, 10.0) == approx(7.5) 
    assert water_column_height(25.0, 0.0) == approx(25.0)
    assert water_column_height(48.3, 12.8) == approx(57.9)
    

def test_pressure_gain_from_water_height():
    """
    verify that pressure_gain_from_water_height works correctly
    parameters: none
    returns: none
    """
    
    # Test the pressure_gain_from_water_height function at least four times
    # with different inputs and assert that the function returns
    # the correct value.
    
    assert pressure_gain_from_water_height(0.0) == approx(0.000, abs=0.001)
    assert pressure_gain_from_water_height(30.2) == approx( 295.628, abs=0.001)
    assert pressure_gain_from_water_height(50.0) == approx(489.450, abs=0.001)
   
    
    
def test_pressure_loss_from_pipe():
    """
    verify that pressure_loss_from_pipe works correctly
    parameters: none
    returns: none
    """
    
    # Test the pressure_loss_from_pipe function at least four times
    # with different inputs and assert that the function returns
    # the correct value.
    
    assert pressure_loss_from_pipe(0.048692, 0.00, 0.018, 1.75) == approx(0.000, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.000, 1.75) == approx(0.000, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 0.00) == approx(0.000, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.75) == approx(-113.008, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.65) == approx(-100.462, abs=0.001)
    assert pressure_loss_from_pipe(0.286870, 1000.00, 0.013, 1.65) == approx(-61.576, abs=0.001)
    assert pressure_loss_from_pipe(0.286870, 1800.75, 0.013, 1.65) == approx(-110.884, abs=0.001)


def test_pressure_loss_from_fitting():
    """
    verify that pressure_loss_from_fitting works correctly
    parameters: none
    returns: none
    """
    
    # Test the pressure_loss_from_fitting function at least five times
    # with different inputs and assert that the function returns
    # the correct value.
    
    assert pressure_loss_from_fittings(0.00, 3) == approx(0.000, abs=0.001)
    assert pressure_loss_from_fittings(1.65, 0) == approx(0.000, abs=0.001)
    assert pressure_loss_from_fittings(1.65, 2) == approx(-0.109, abs=0.001)
    assert pressure_loss_from_fittings(1.75, 2) == approx(-0.122, abs=0.001)
    assert pressure_loss_from_fittings(1.75, 5) == approx(-0.306, abs=0.001)
    

def test_reynolds_number():
    """
    verify that reynolds_number works correctly
    parameters: none
    returns: none
    """
    
    # Test the reynolds_number function at least five times
    # with different inputs and assert that the function returns
    # the correct value.

    assert reynolds_number(0.048692, 0.00) == approx(0, abs=1)
    assert reynolds_number(0.048692, 1.65) == approx(80069, abs=1)
    assert reynolds_number(0.048692, 1.75) == approx(84922, abs=1)
    assert reynolds_number(0.286870, 1.65) == approx(471729, abs=1)
    assert reynolds_number(0.286870, 1.75) == approx(500318, abs=1)
    
    
def test_pressure_loss_from_pipe_reduction():
    """
    verify that pressure_loss_from_pipe_reduction works correctly
    parameters: none
    returns: none
    """
    
    # Test the pressure_loss_from_pipe_reduction function at least three times
    # with different inputs and assert that the function returns
    # the correct value.
    
    assert pressure_loss_from_pipe_reduction(0.28687, 0.00, 1, 0.048692) == approx(0.000, abs=0.001)
    assert pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692) == approx(-163.744, abs=0.001)
    assert pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692) == approx(-184.182, abs=0.001)


def test_convert_kpa_to_psi():
    """
    verify that convert_to_psi works correctly
    parameters: none
    returns: none
    """
    
    # Test the convert_kpa_to_psi function at least five times
    # with different inputs and assert that the function returns
    # the correct value.
    
    assert convert_kpa_to_psi(0.000) == approx(0.000, abs=0.001)
    assert convert_kpa_to_psi(100.000) == approx(14.504, abs=0.001)
    assert convert_kpa_to_psi(200.000) == approx(29.008, abs=0.001)
    assert convert_kpa_to_psi(700.000) == approx(101.527, abs=0.001)
    assert convert_kpa_to_psi(1000.000) == approx(145.038, abs=0.001)
    

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])