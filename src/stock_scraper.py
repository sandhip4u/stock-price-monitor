from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

def get_stock_price(stock_symbol):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(f"https://www.marketwatch.com/investing/stock/{stock_symbol.lower()}")
    sleep(5)  # wait for page to load
    price_element = driver.find_element(By.XPATH, "//bg-quote[@class='value']")
    price = price_element.text.replace(',', '')
    driver.quit()
    return float(price)
