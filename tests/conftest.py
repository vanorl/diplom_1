from unittest.mock import Mock
import pytest


@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = 'bun_for_test'
    bun.get_price.return_value = 9.0
    return bun

@pytest.fixture
def mock_ingredient():
    ingredient = Mock()
    ingredient.get_price.return_value = 49.0
    ingredient.get_name.return_value = 'ingredient_for_test'
    ingredient.get_type.return_value = 'FILLING'
    return ingredient
