def complex_multiply(a: float, b: float, c: float, d: float) -> (float, float):
    """Multiplies two complex numbers using only three multiplications of real numbers.

    Args:
        a: the real part of the first complex number
        b: the imaginary part of the first complex number
        c: the real part of the second complex number
        d: the imaginary part of the second complex number

    Returns:
        The real part and the imaginary part of the product.
    """
    alpha = a * c
    beta = b * d
    gamma = (a + b) * (c + d)
    return alpha - beta, gamma - alpha - beta
