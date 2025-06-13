# E-commerce Automation Testing Framework

This project is an automated test suite built using Selenium,Pytest and Python for testing key functionalities of a sample e-commerce website, including:

-  Searching for products
-  Adding items to the cart
-  Updating quantity
-  Removing items from the cart


  ## 📁 Project Structure
  Automation-testing/
  
├── pages/

    ├── base_page.py                    (Common reusable WebDriver action)   
    ├── home_page.py                    (Page Object for home/search page)  
    └── cart_page.py                    (Page Object for cart functionality)   
├── tests/

    └── test_search_cart_flow.py        (Test suite)

├── user_config.json                     (User input config file)

├── index.html                           (Simulated local e-commerce webpage)

├── conftest.py                          (Pytest fixtures & browser setup)

├── requirements.txt                     (Python dependencies)

└── report.html                          (HTML test report (generated after run))

##  Tech Stack

- Python 3.x
- Selenium 4
- Pytest
- ChromeDriver
- Pytest-HTML (for test reports)

## Test Cases

| Test Name | Description |
|----------|-------------|
| `test_search_non_existing_product` | Searches an invalid term and expects "No results found" |
| `test_search_existing_product`     | Searches for an actual product and checks result presence |
| `test_add_to_cart`                 | Adds item (by index) to cart and verifies count |
| `test_update_quantity`             | Updates item quantity and checks cart |
| `test_remove_product`              | Removes item from cart and confirms cart is empty |


## Setup Instructions

Step 1: Clone the Repo:

* bash
* git clone https://github.com/kuldeepshinde7/E-commerce-site-test-automation.git
* cd E-commerce-site-test-automation

Step 2: Create & Activate Virtual Environment:
* python -m venv venv
* .\venv\Scripts\activate

Step 3: Install Requirements:
* pip install -r requirements.txt
* pip install pytest-html

 User Configuration:
 * Edit the user_config.json file to control test inputs like search terms or product index.

{
  "search_term": "Laptop",
  "product_index": 3,
  "update_quantity_to": 2
}

Step 4: Run Tests:
* pytest --html=report.html

Running Locally with index.html:
You can open index.html in your browser manually (double-click or open with Live Server) before running the tests to simulate the e-commerce UI.

step 5:Test Report Output:
* After running tests, open report.html to view a styled summary of passed/failed tests.

