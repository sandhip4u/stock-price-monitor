from src.stock_scraper import get_stock_price

def test_get_stock_price():
    price = get_stock_price("AAPL")
    assert price > 0
