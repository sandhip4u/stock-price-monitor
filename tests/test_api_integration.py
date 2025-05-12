from src.stock_api import get_stock_price_from_api

def test_get_stock_price_from_api():
    price = get_stock_price_from_api("AAPL", "your_alpha_vantage_api_key")
    assert price > 0
