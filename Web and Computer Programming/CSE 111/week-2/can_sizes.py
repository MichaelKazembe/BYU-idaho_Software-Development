"""
AUTHOR: MICHAEL KAZEMBE
DATE: 12/11/2024

cone_volume.py

TEAM ACTIVITY

Program that computes and prints the storage efficiency 12 steel can sizes

"""
# Import the math module
from math import pi as PI

def main():
    """
    Function that computes and prints the storage efficiency 
    and cost efficiency of 12 steel can sizes
    
    """
    # List of can sizes: name, radius, height, and cost
    can_names = [
        "#1 Picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder", "#5",
        "#6Z", "#8Z short", "#10", "#211", "#300", "#303"
    ]
    can_radiuses = [
        6.83, 7.78, 8.73, 10.32, 10.79, 13.02,
        5.4, 6.83, 15.72, 6.83, 7.62, 8.1
    ]
    can_heights = [
        10.16, 11.91, 11.59, 11.91, 17.78, 14.29,
        8.89, 7.62, 17.78, 12.38, 11.27, 11.11
    ]
    can_costs = [
        0.28, 0.43, 0.45, 0.61, 0.86, 0.83,
        0.22, 0.26, 1.53, 0.34, 0.38, 0.42
    ]
    
    # Loop through the list of can sizes and compute the storage efficiency and cost efficiency
    for i in range(len(can_names)):
        name = can_names[i]
        radius = can_radiuses[i]
        height = can_heights[i]
        cost = can_costs[i]
        
        # Compute the storage efficiency and cost efficiency
        storage_efficiency = compute_storage_efficiency(radius, height)
        cost_efficiency = compute_cost_efficiency(radius, height, cost)
        
        # Print the results
        print_results(name, storage_efficiency, cost_efficiency)
        print()
        
       
def compute_volume(radius, height):
    """
    Function that computes the volume of a steel can given its radius and height
    
    :param radius: the radius of the steel can
    :param height: the height of the steel can
    :return: the volume of the steel can
    """
    
    volume = PI * radius ** 2 * height
    return volume


def compute_surface_area(radius, height):
    """
    Function that computes the surface area of a steel can given its radius and height
    
    :param radius: the radius of the steel can
    :param height: the height of the steel can
    :return: the surface area of the steel can
    """
    
    surface_area = 2 * PI * radius * (radius + height)
    return surface_area


def compute_storage_efficiency(radius, height):
    """
    Function that computes the storage efficiency of a steel can given its radius and height
    
    :param radius: the radius of the steel can
    :param height: the height of the steel can
    :return: the storage efficiency of the steel can
    """
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = volume / surface_area
    return storage_efficiency


def compute_cost_efficiency(radius, height, cost):
    """
    Function that computes the cost efficiency of a steel can given its radius, height and cost
    
    :param radius: the radius of the steel can
    :param height: the height of the steel can
    :param cost: the cost of the steel can
    :return: the cost efficiency of the steel can
    """
    volume = compute_volume(radius, height)
    cost_efficiency = volume / cost
    return cost_efficiency


def print_results(name, storage_efficiency, cost_efficiency):
    """
    Function that prints the results of the storage efficiency and cost efficiency of a steel can
    
    :param name: the name of the steel can
    :param storage_efficiency: the storage efficiency of the steel can
    :param cost_efficiency: the cost efficiency of the steel can
    """
    print(f"{name} Storage Efficiency: {storage_efficiency:.2f}")
    print(f"{name} Cost Efficiency: {cost_efficiency:.0f}")
    
    
#  Call the main function
main()

# END OF PROGRAM