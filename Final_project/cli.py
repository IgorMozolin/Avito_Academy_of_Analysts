import click
import math
import random
from typing import Union


def log(template: str = 'Prepared in {} minutes! 🍪',
        min_time: int = 5, max_time: int = 20) -> callable:
    """
    A decorator for logging the preparation time of a function.

    Args:
        template (str): The log message template.
        min_time (int): Minimum time for cooking in minutes.
        max_time (int): Maximum time for cooking in minutes.

    Returns:
        callable: The decorated function.
    """
    def decorator(func: callable) -> callable:
        """
        Decorator function.

        Args:
            func (callable): The function to be decorated.

        Returns:
            callable: The decorated function.
        """
        def wrapper(*args, **kwargs) -> callable:
            """
            Wrapper function.

            Returns:
                callable: The result of the decorated function.
            """
            res = f"{template.format(random.randint(min_time, max_time))}"
            print(res)
            return res

        return wrapper

    return decorator


class Pizza:
    """
    A class representing a pizza.

    Attributes:
        radii (dict): A dictionary mapping pizza sizes to their radii values.
        receipt (list): A list of ingredients in the pizza.
        radius (int): The radius of the pizza.
        area (float): The area of the pizza.

    Methods:
        __str__: Returns a string representation of the pizza.
        __eq__: Compares the pizza with another object for equality.
        __sub__: Computes the difference in area between two pizzas.
        cook: Logs the preparation time of cooking the pizza.
        add_to_receipt: Adds an ingredient to the pizza's receipt.
        del_from_receipt: Removes an ingredient from the pizza's receipt.
        dict: Returns a dictionary representation of the pizza.
    """
    radii = {"XL": 35, "L": 30}

    def __init__(self, size: str = "XL") -> None:
        """
        Initializes a pizza with a specified size.

        Args:
            size (str): The size of the pizza, default is 'XL'.
        """
        self.receipt = None
        self.radius = self.radii.get(size)
        if self.radius is not None:
            self.area = math.pi * self.radius ** 2
        else:
            self.area = 0

    def __str__(self) -> str:
        """
        Returns a string representation of the pizza.

        Returns:
            str: The string representation of the pizza.
        """
        return f"{self.__class__.__name__} ({self.radius} cm)"

    def __eq__(self, value: Union[int, 'Pizza']) -> bool:
        """
        Compares the pizza with another object for equality.

        Args:
            value (Union[int, 'Pizza']): The object to compare with.

        Returns:
            bool: True if the objects are equal, False otherwise.
        """
        if isinstance(value, int):
            return self.radius == value
        if isinstance(value, Pizza):
            return self.radius == value.radius
        return False

    def __sub__(self, other: 'Pizza') -> float:
        """
        Computes the difference in area between two pizzas.

        Args:
            other (Pizza): The other pizza to compute the difference with.

        Returns:
            float: The difference in area.
        """
        return self.area - other.area

    @log(template='Prepared in {} minutes! 🍪')
    def cook(self) -> None:
        """
        Logs the preparation time of cooking the pizza.
        """
        pass

    def add_to_receipt(self, ingredient: str) -> None:
        """
        Adds an ingredient to the pizza's receipt.

        Args:
            ingredient (str): The ingredient to add.
        """
        if self.receipt is None:
            self.receipt = [ingredient]
        elif ingredient not in self.receipt:
            self.receipt.append(ingredient)

    def del_from_receipt(self, ingredient: str) -> None:
        """
        Removes an ingredient from the pizza's receipt.

        Args:
            ingredient (str): The ingredient to remove.
        """
        if self.receipt and ingredient in self.receipt:
            self.receipt.remove(ingredient)

    def dict(self) -> dict:
        """
        Returns a dictionary representation of the pizza.

        Returns:
            dict: A dictionary representation of the pizza.
        """
        return {str(self): self.receipt}


class Margherita(Pizza):
    """
    A class representing a Margherita pizza, a subclass of Pizza.
    """
    def __init__(self, size: str = 'XL') -> None:
        """
        Initializes a Margherita pizza with a specified size.

        Args:
            size (str): The size of the pizza, default is 'XL'.
        """
        super().__init__(size)
        self.receipt = ['tomato sauce', 'mozzarella', 'tomatoes']


class Pepperoni(Pizza):
    """
    A class representing a Pepperoni pizza, a subclass of Pizza.
    """
    def __init__(self, size: str = 'XL') -> None:
        """
        Initializes a Pepperoni pizza with a specified size.

        Args:
            size (str): The size of the pizza, default is 'XL'.
        """
        super().__init__(size)
        self.receipt = ['tomato sauce', 'mozzarella', 'pepperoni']


class Hawaiian(Pizza):
    """
    A class representing a Hawaiian pizza, a subclass of Pizza.
    """
    def __init__(self, size: str = 'XL') -> None:
        """
        Initializes a Hawaiian pizza with a specified size.

        Args:
            size (str): The size of the pizza, default is 'XL'.
        """
        super().__init__(size)
        self.receipt = ['tomato sauce', 'mozzarella', 'chicken', 'pineapples']


class Delivery:
    """
    A class representing a pizza delivery service.

    Methods:
        delivery: Logs the delivery time of delivering a pizza.
    """
    @log(template='Delivered for {} minutes! 🚀', min_time=25, max_time=45)
    def delivery(self) -> None:
        """
        Logs the delivery time of delivering a pizza.
        """
        pass


pizzas = {'Hawaiian': Hawaiian,
          'Margherita': Margherita,
          'Pepperoni': Pepperoni,
          }


@click.group()
def cli() -> None:
    """
    Command line interface for interacting with pizza orders and delivery.
    """
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
@click.option('--size',
              default='XL',
              type=click.Choice(['XL', 'L']),
              help='Pizza size (XL or L)')
def order(pizza: str, delivery: bool, size: str) -> None:
    """
    Order a pizza with optional delivery.

    Args:
        pizza (str): The type of pizza to order.
        delivery (bool): Whether to include delivery.
        size (str): The size of the pizza, default is 'XL'.
    """
    if pizza.lower() in map(str.lower, pizzas):
        pizza_instance = pizzas[pizza.capitalize()](size=size)
        pizza_instance.cook()

    if delivery:
        Delivery().delivery()


@cli.command()
def menu() -> None:
    """
    Display the menu of available pizzas.
    """
    for key, value in pizzas.items():
        emoji = ''
        if key == 'Hawaiian':
            emoji = ' 🍍'
        if key == 'Margherita':
            emoji = ' 🍅'
        if key == 'Pepperoni':
            emoji = ' 🍕'
        click.echo(
            click.style(
                f"{key}{emoji}: {', '.join(value().receipt)}"
            )
        )


if __name__ == '__main__':
    cli()