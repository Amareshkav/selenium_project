import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def setUp():
    #driver = webdriver.Chrome(executable_path = r"C:\Users\Balabheem Shivaraj\OneDrive\Desktop\Amaresh_proj\Driver\Chrome\chromedriver.exe")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    yield driver
    driver.close()