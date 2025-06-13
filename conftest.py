"""
conftest.py

Loads configuration from config.json manually and provides reusable fixtures.
Also sets up Selenium WebDriver for Chrome.
"""

import pytest
import json
import os
from selenium import webdriver

@pytest.fixture(scope="session")
def config():
    config_path = os.path.abspath("config.json")
    with open(config_path, 'r') as f:
        return json.load(f)

# Fixtures from config
@pytest.fixture
def search_term(config):
    return config["search_term"]

@pytest.fixture
def non_existing_term(config):
    return config["non_existing_term"]

@pytest.fixture
def product_index(config):
    return config["product_index_to_add"]

@pytest.fixture
def quantity(config):
    return config["quantity"]

# WebDriver fixture
@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get("file://" + os.path.abspath("index.html"))
    yield driver
    driver.quit()

