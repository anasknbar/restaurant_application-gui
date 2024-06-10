import pytest
from unittest.mock import patch, MagicMock


from project.project import calculate_order_price,place_order

@pytest.fixture
def mock_globals(monkeypatch):
    
    mock_extra_cheese_int = MagicMock()
    mock_extra_ketchup_int = MagicMock()
    mock_soft_drink_int = MagicMock()
    mock_pizza_selected_option = MagicMock()
    mock_pizza_quantity_int = MagicMock()
    mock_burger_selected_option = MagicMock()
    mock_burger_quantity_int = MagicMock()

    monkeypatch.setattr('project.project.extra_cheese_int', mock_extra_cheese_int)
    monkeypatch.setattr('project.project.extra_ketchup_int', mock_extra_ketchup_int)
    monkeypatch.setattr('project.project.soft_drink_int', mock_soft_drink_int)
    monkeypatch.setattr('project.project.pizza_selected_option', mock_pizza_selected_option)
    monkeypatch.setattr('project.project.pizza_quantity_int', mock_pizza_quantity_int)
    monkeypatch.setattr('project.project.burger_selected_option', mock_burger_selected_option)
    monkeypatch.setattr('project.project.burger_quantity_int', mock_burger_quantity_int)

 
    pizza_prices = {'Margherita': 10, 'Pepperoni': 12}
    burger_prices = {'Cheeseburger': 8, 'Veggie': 7}
    
    monkeypatch.setattr('project.project.pizza_prices', pizza_prices)
    monkeypatch.setattr('project.project.burger_prices', burger_prices)

    return {
        'extra_cheese_int': mock_extra_cheese_int,
        'extra_ketchup_int': mock_extra_ketchup_int,
        'soft_drink_int': mock_soft_drink_int,
        'pizza_selected_option': mock_pizza_selected_option,
        'pizza_quantity_int': mock_pizza_quantity_int,
        'burger_selected_option': mock_burger_selected_option,
        'burger_quantity_int': mock_burger_quantity_int
    }

def test_calculate_order_price(mock_globals):
    mock_globals['extra_cheese_int'].get.return_value = 1
    mock_globals['extra_ketchup_int'].get.return_value = 1
    mock_globals['soft_drink_int'].get.return_value = 1
    mock_globals['pizza_selected_option'].get.return_value = 'Margherita'
    mock_globals['pizza_quantity_int'].get.return_value = 2
    mock_globals['burger_selected_option'].get.return_value = 'Cheeseburger'
    mock_globals['burger_quantity_int'].get.return_value = 1

    total_price = calculate_order_price()
    assert total_price == 1 + 1 + (1 * 2) + (10 * 2) + (8 * 1)

@patch('project.project.messagebox.askquestion')
@patch('project.project.messagebox.showinfo')
def test_place_order(mock_showinfo, mock_askquestion, mock_globals):
    mock_globals['extra_cheese_int'].get.return_value = 1
    mock_globals['extra_ketchup_int'].get.return_value = 1
    mock_globals['soft_drink_int'].get.return_value = 1
    mock_globals['pizza_selected_option'].get.return_value = 'Margherita'
    mock_globals['pizza_quantity_int'].get.return_value = 2
    mock_globals['burger_selected_option'].get.return_value = 'Cheeseburger'
    mock_globals['burger_quantity_int'].get.return_value = 1

    mock_askquestion.return_value = 'yes'
    place_order()
    mock_showinfo.assert_called_with("Information", "Thank you for choosing our restaurant :)")

    mock_askquestion.return_value = 'no'
    place_order()
    mock_showinfo.assert_called_with("Information", "See you later")
