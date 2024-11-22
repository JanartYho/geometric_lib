def area(a, b, c):
    if a < 0 or b < 0 or c < 0:
        raise ValueError("Sides cannot be negative")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Invalid triangle sides")
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


def perimeter(a, b, c):
    if a < 0 or b < 0 or c < 0:
        raise ValueError("Sides cannot be negative")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Invalid triangle sides")
    return a + b + c
