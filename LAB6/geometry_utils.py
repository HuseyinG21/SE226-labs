import math

def circle_area(radius):
    try:
        if radius <= 0:
            raise ValueError("Dimensions must be strictly positive.")
        return math.pi * radius ** 2
    except TypeError:
        raise TypeError("Radius must be a number.")

def circle_perimeter(radius):
    if radius <= 0:
        raise ValueError("Dimensions must be strictly positive.")
    return 2 * math.pi * radius

def rectangle_area(width, height):
    if width <= 0 or height <= 0:
        raise ValueError("Dimensions must be strictly positive.")
    return width * height

def rectangle_perimeter(width, height):
    if width <= 0 or height <= 0:
        raise ValueError("Dimensions must be strictly positive.")
    return 2 * (width + height)

def triangle_area(base, height):
    if base <= 0 or height <= 0:
        raise ValueError("Dimensions must be strictly positive.")
    return 0.5 * base * height