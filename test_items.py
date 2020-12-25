from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pytest
import time
import math

def test_add_basket(browser):
 link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
 browser.get(link)
 time.sleep(30)
 check=browser.find_element_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket")
 assert check, "Success"