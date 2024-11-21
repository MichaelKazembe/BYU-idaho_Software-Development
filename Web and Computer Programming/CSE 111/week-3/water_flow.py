
def water_column_height(tower_height, tank_height):
    """ 
    calculates and returns the height of a column of water from a tower height and a tank wall height
    parameters:
        tower_height: the height of the tower
        tank_height: the height of the tank wall
    returns:
        the height of the column of water
    
    """
    
    water_height = tower_height + (3 * tank_height) / 4
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
    
    water_density = 998.2 # kg/m^3
    gravity = 9.810665 # m/s^2
    
    pressure = water_density * gravity * height/1000
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
    
    water_density = 998.2 # kg/m^3
    
    pressure =  - (friction_factor * pipe_length * water_density \
                * fluid_velocity ** 2) / 2000 * pipe_diameter
    return pressure