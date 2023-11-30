from typing import Any


class Color:
    """
    A class representing an RGB color with ANSI
    escape codes for terminal output.

    Attributes:
        END (str): ANSI escape code for resetting text attributes.
        START (str): ANSI escape code for starting colored text.
        MOD (str): ANSI escape code modifier for setting text attributes.
    """

    END = '\033[0'
    START = '\033[1;38;2'
    MOD = 'm'

    def __init__(self, r: int, g: int, b: int) -> None:
        """
        Initializes a Color instance with RGB values.

        Args:
            r (int): Red component (0-255).
            g (int): Green component (0-255).
            b (int): Blue component (0-255).
        """
        self.r = r
        self.g = g
        self.b = b

    def __repr__(self) -> str:
        """
        Returns the ANSI escape code representation of the color.

        Returns:
            str: ANSI escape code representation.
        """
        return f'{self.START};{self.r};{self.g};' \
               f'{self.b}{self.MOD}●{self.END}{self.MOD}'

    def __eq__(self, other: Any) -> bool:
        """
        Checks if two Color instances are equal.

        Args:
            other (Any): Another object to compare.

        Returns:
            bool: True if equal, False otherwise.
        """
        if isinstance(other, Color):
            return self.r == other.r and self.g == other.g and \
                   self.b == other.b
        else:
            return False

    def __add__(self, other: 'Color') -> 'Color':
        """
        Adds two Color instances together, clamping values to 255.

        Args:
            other (Color): Another Color instance.

        Returns:
            Color: Result of the addition.
        """
        if isinstance(other, Color):
            new_r = min(self.r + other.r, 255)
            new_g = min(self.g + other.g, 255)
            new_b = min(self.b + other.b, 255)
            return Color(new_r, new_g, new_b)
        else:
            raise TypeError

    def __hash__(self) -> int:
        """
        Computes the hash value for a Color instance.

        Returns:
            int: Hash value.
        """
        return hash((self.r, self.g, self.b))

    def __mul__(self, other: float) -> 'Color':
        """
        Multiplies the color intensity by a given factor.

        Args:
            other (float): Multiplication factor (0.0 to 1.0).

        Returns:
            Color: Result of the multiplication.
        """
        if 0.0 <= other <= 1.0:
            cl = -256 * (1 - other)
            F = (259 * (cl + 255))/(255 * (259 - cl))
            new_r = F * (self.r - 128) + 128
            new_g = F * (self.g - 128) + 128
            new_b = F * (self.b - 128) + 128
            return Color(int(new_r), int(new_g), int(new_b))
        else:
            raise TypeError

    def __rmul__(self, other: float) -> 'Color':
        """
        Allows multiplication of a Color instance by a factor on the right.

        Args:
            other (float): Multiplication factor (0.0 to 1.0).

        Returns:
            Color: Result of the multiplication.
        """
        return self * other


if __name__ == "__main__":
    red = Color(255, 0, 0)
    print(red)
    green = Color(0, 255, 0)
    print(red == green)
    print(red == Color(255, 0, 0))
    print(red == 1)
    print(red + green)
    orange1 = Color(255, 165, 0)
    orange2 = Color(255, 165, 0)
    color_list = [orange1, red, green, orange2]
    print(set(color_list))
    print(0 * red)
    print(red * 0.5)
