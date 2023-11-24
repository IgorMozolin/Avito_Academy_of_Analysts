from cli import Margherita, cli
import pytest
from click.testing import CliRunner


def test_order_with_delivery():
    """
    Test ordering a pizza with delivery.

    Steps:
    1. Order a Pepperoni pizza with delivery.
    2. Verify that the log message indicates the pizza preparation time.
    3. Verify that the log message indicates the delivery time.

    """
    runner = CliRunner()
    result = runner.invoke(cli, [
        'order',
        '--delivery',
        '--size',
        'XL',
        'Pepperoni'
    ])
    assert "Prepared in" in result.output
    assert "Delivered for" in result.output


def test_add_ingredient_to_receipt():
    """
    Test adding an ingredient to a pizza's receipt.

    Steps:
    1. Create a Margherita pizza.
    2. Add 'olives' to the pizza's receipt.
    3. Verify that 'olives' is in the pizza's receipt.
    """
    margherita = Margherita()
    margherita.add_to_receipt('olives')
    assert 'olives' in margherita.receipt


def test_delete_ingredient_from_receipt():
    """
    Test deleting an ingredient from a pizza's receipt.

    Steps:
    1. Create a Margherita pizza with 'mushrooms' in the receipt.
    2. Delete 'mushrooms' from the pizza's receipt.
    3. Verify that 'mushrooms' is not in the pizza's receipt.
    """
    margherita = Margherita()
    margherita.add_to_receipt('mushrooms')
    margherita.del_from_receipt('mushrooms')
    assert 'mushrooms' not in margherita.receipt


def test_display_menu():
    """
    Test displaying the menu.

    Steps:
    1. Run the 'menu' command.
    2. Verify that the output contains information
    about available pizzas and their ingredients.
    """
    runner = CliRunner()
    result = runner.invoke(cli, ['menu'])
    assert "Hawaiian" in result.output
    assert "Margherita" in result.output
    assert "Pepperoni" in result.output


if __name__ == '__main__':
    pytest.main()
