from keyword import iskeyword
from typing import Union, Dict, Any, Optional
import json

NumericType = Union[int, float]


class NestedKey:
    """
    Class representing a nested key in the Advertisement class.
    """

    def __init__(self, mapping: Dict[str, Any]):
        """
        Initialize the NestedKey with the provided mapping.

        Args:
            mapping (dict): The dictionary representing the nested key.
        """
        for nested_key in mapping:
            if isinstance(mapping[nested_key], dict):
                self.__dict__[nested_key] = NestedKey(mapping[nested_key])
            else:
                self.__dict__[nested_key] = mapping[nested_key]

    def __getattr__(self, nested_key: str) -> Any:
        """
        Get the value of the specified attribute.

        Args:
            nested_key (str): The attribute key.

        Returns:
            Any: The value of the attribute.
        """
        if nested_key[-1] == '_' and iskeyword(nested_key[:-1]):
            nested_key = nested_key[:-1]
        return self.__dict__[nested_key]

    def __str__(self, level: int = 0) -> str:
        """
        Return a string representation of the NestedKey.

        Args:
            level (int): The level of nesting.

        Returns:
            str: The string representation of the NestedKey.
        """
        indentation = '_' * level * 5
        result = []
        nested_keys = []
        for key in self.__dict__:
            if not isinstance(self.__dict__[key], NestedKey):
                result.append(indentation + str(self.__dict__[key]))
            else:
                nested_keys.append(key)
        for key in nested_keys:
            result.append(indentation + '| ' + key + ':')
            result.append(self.__dict__[key].__str__(level + 1))
        return '\n'.join(result)


class ColoredMixin:
    """
    Mixin class for adding color to the string representation.
    """

    color_code = 36

    def __str__(self, color: Optional[int] = None) -> str:
        """
        Return a colored string representation.

        Args:
            color (int, optional): The color code. Defaults to None.

        Returns:
            str: The colored string representation.
        """
        if color is None:
            color = ColoredMixin.color_code
        colored_str = f'\033[1;{color};40m' + super().__str__()
        colored_str += '\033[0;37;40m'
        return colored_str


class Advertisement(ColoredMixin, NestedKey):
    """
    Class representing an advertisement with nested keys.
    """

    def __init__(self, mapping: Dict[str, Any]) -> None:
        """
        Initialize the Advertisement with the provided mapping.

        Args:
            mapping (dict): The dictionary representing the advertisement.
        """
        self.validate_title(mapping)
        self._cost: NumericType = 0
        if 'cost' in mapping:
            self.cost = mapping['cost']
            mapping.pop('cost')
        super().__init__(mapping)

    @staticmethod
    def validate_title(mapping: Dict[str, Any]) -> None:
        """
        Check if the 'title' key is present and its value is a string.

        Args:
            mapping (dict): The dictionary representing the advertisement.

        Raises:
            ValueError: If 'title' is not present or is not a string.
        """
        if 'title' not in mapping:
            raise ValueError('Title must be present in the mapping.')
        if not isinstance(mapping['title'], str):
            raise ValueError('Title must be a string.')

    @property
    def cost(self) -> NumericType:
        """
        Get the cost of the advertisement.

        Returns:
            NumericType: The cost of the advertisement.
        """
        return self._cost

    @cost.setter
    def cost(self, value: NumericType) -> None:
        """
        Set the cost of the advertisement.

        Args:
            value (NumericType): The new cost value.

        Raises:
            ValueError: If the value is not a number or is negative.
        """
        if not isinstance(value, (float, int)):
            raise ValueError("Cost must be a number")
        if value < 0:
            raise ValueError("Cost must be a non-negative number.")
        self._cost = value


if __name__ == '__main__':
    json_str = """{
        "title": "python",
        "category": "programming",
        "cost": 0,
        "location": {
            "address": "City, Street, 7",
            "metro_stations": ["Station"],
            "nested": {
                "four": "two"
                }
            }
    }"""
    json_obj = json.loads(json_str)
    adv = Advertisement(json_obj)
    print(adv)
