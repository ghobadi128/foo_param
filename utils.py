def validate_radius(radius):
    """
    Validate the radius to ensure it's a positive number.
    
    Parameters:
        radius (float): The radius of the sphere.
    
    Raises:
        ValueError: If the radius is not positive.
    """
    if radius <= 0:
        raise ValueError("Radius must be a positive number.")