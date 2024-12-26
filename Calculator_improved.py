class Calculator:
    """
    A simple calculator class to perform basic arithmetic operations.
    """

    @staticmethod
    def add(a: float, b: float) -> float:
        """
        Adds two numbers.
        :param a: First number.
        :param b: Second number.
        :return: Sum of a and b.
        """
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        """
        Subtracts the second number from the first.
        :param a: First number.
        :param b: Second number.
        :return: Difference between a and b.
        """
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """
        Multiplies two numbers.
        :param a: First number.
        :param b: Second number.
        :return: Product of a and b.
        """
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        """
        Divides the first number by the second.
        :param a: Dividend.
        :param b: Divisor.
        :return: Result of the division.
        :raises ValueError: If b is zero.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
