from unittest.mock import Mock
from burger import Burger


class TestBurger:

    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients[0] == mock_ingredient

    def test_remove_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(Mock())
        burger.add_ingredient(mock_ingredient)
        burger.move_ingredient(1, 0)
        assert burger.ingredients[0] == mock_ingredient

    def test_get_price(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        expected_price = burger.get_price()
        actual_price = 67.0
        assert expected_price == actual_price

    def test_get_receipt(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        expected_result = (
        f'(==== {mock_bun.get_name()} ====)\n'
        f'= {mock_ingredient.get_type().lower()} {mock_ingredient.get_name()} =\n'
        f'(==== {mock_bun.get_name()} ====)\n\n'
        f'Price: {burger.get_price()}'
        )
        actual_result = burger.get_receipt()
        assert actual_result == expected_result
