"""
AUTHOR: MICHAEL KAZEMBE
DATE: 22/11/2024

water_flow.py

Program that calculates the height of a column of water, 
the pressure caused by a column of water, and 
the pressure loss from friction in a pipe.

"""

# Constants
EARTH_ACCELERATION_OF_GRAVITY = 9.8066500
WATER_DENSITY = 998.2000000
WATER_DYNAMIC_VISCOSITY = 0.0010016


def water_column_height(tower_height, tank_height):
    """ 
    calculates and returns the height of a column of water from a tower height and a tank wall height
    parameters:
        tower_height: the height of the tower
        tank_height: the height of the tank wall
    returns:
        the height of the column of water
    
    """
    
    water_height = tower_height + ((3 * tank_height) / 4)
    return water_height


def pressure_gain_from_water_height(height):
    """
    calculates and returns the pressure caused by earth's gravity 
    acting on a column of water
    parameters:
        height: the height of the column of water
    returns:
        the pressure caused by the column of water
    """
    
    pressure = (WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY * height)/1000
    return pressure


def pressure_loss_from_pipe(pipe_diameter,
        pipe_length, friction_factor, fluid_velocity):
    """
    calculates and returns the pressure loss from friction in a pipe
    parameters:
        pipe_diameter: the diameter of the pipe
        pipe_length: the length of the pipe
        friction_factor: the friction factor of the pipe
        fluid_velocity: the velocity of the fluid in the pipe
    returns:
        the pressure loss from friction in the pipe
    """
    
    pressure =  - (friction_factor * pipe_length * WATER_DENSITY \
        * (fluid_velocity ** 2)) / (2000 * pipe_diameter)
    return pressure


def pressure_loss_from_fittings(
        fluid_velocity, quantity_fittings):
    """
    Calculates and returns the pressure loss from fittings in a pipe
    parameters:
        fluid_velocity: the velocity of the fluid in the pipe
        quantity_fittings: the number of fittings in the pipe
    returns:
        the pressure loss from fittings in the pipe
    """
    

    
    pressure = -(0.04 * WATER_DENSITY * fluid_velocity ** 2 \
        * quantity_fittings) / 2000
    return pressure


def reynolds_number(hydraulic_diameter, fluid_velocity):
    """
    calculates and returns the reynolds number of a fluid flow
    parameters:
        hydraulic_diameter: the hydraulic diameter of the fluid flow
        fluid_velocity: the velocity of the fluid flow
    returns:
        the reynolds number of the fluid flow
    """
    
 
    reynolds_number = (WATER_DENSITY * hydraulic_diameter \
        * fluid_velocity) / WATER_DYNAMIC_VISCOSITY
    return reynolds_number


def pressure_loss_from_pipe_reduction(larger_diameter,
        fluid_velocity, reynolds_number, smaller_diameter):
    """
    calculates and returns the pressure loss from a pipe diameter reduction
    parameters:
        larger_diameter: the diameter of the larger pipe
        fluid_velocity: the velocity of the fluid in the pipe
        reynolds_number: the reynolds number of the fluid flow
        smaller_diameter: the diameter of the smaller pipe  
    returns:
        the pressure loss from the pipe diameter reduction
    """
    
    k = (0.1 + (50/reynolds_number)) * ((larger_diameter/smaller_diameter) ** 4 - 1)
    
    pressure = - (k * WATER_DENSITY * fluid_velocity ** 2) / 2000
    return pressure


def convert_kpa_to_psi(pressure):
    """
    converts pressure from kilopascals to pounds per square inch
    parameters:
        pressure: the pressure in kilopascals
    returns:
        the pressure in pounds per square inch
    """
    
    psi = pressure * 0.1450377377 # 1 kilopascal = 0.1450377377 psi
    return psi


PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)
HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)
def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))
    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)
    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss
    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss
    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss
    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss
    # Convert pressure to psi
    psi = convert_kpa_to_psi(pressure)
    print(f"Pressure at house: {pressure:.1f} kilopascals(kPa), {psi:.1f} pounds per sq inch(psi)")
if __name__ == "__main__":
    main()