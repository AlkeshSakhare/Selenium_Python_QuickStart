# Selenium_Python_QuickStart

install Python 3.6+, Pycharm, Jdk 12

Install below python package

pip install webdriver-manager

pip install selenium

pip install pywin32 -> to handle windows exception while doing automation

pip install requests -> to send http request

pip install mysql-connector-python -> to connect db

pip install -U pytest -> to write unit test

pip install -U openpyxl -> to read / write xlsx file

Demo Site: https://www.selenium.dev/selenium/web/

Code samples: https://github.com/SeleniumHQ/seleniumhq.github.io/tree/trunk/examples/python

Tutorials: https://www.youtube.com/watch?v=2DD-ynCIZ4w&list=PLUDwpEzHYYLsuUBvuoYTlN0KsBB5t-BDa

Python Tutorials : https://www.youtube.com/watch?v=spX3jkOTOU8&list=PLUDwpEzHYYLsX-gCM7sAp43NF6Y_1rBb_

Selenium Doc: https://selenium-python.readthedocs.io

Cheatsheet:

1. https://dev.to/razgandeanu/selenium-cheat-sheet-9lc

2. https://app.endtest.io/guides/docs/how-to-create-web-tests/

Selenium Tutorials: https://www.youtube.com/watch?v=2DD-ynCIZ4w&list=PLUDwpEzHYYLsuUBvuoYTlN0KsBB5t-BDa&index=1



PIP commands:

pip freeze : to see all installed packages

pip show -V selenium : to see install packages information

pip install -U selenium : to install package

pip uninstall selenium : to uninstall package


POM:- 

Ref 1: https://www.browserstack.com/guide/page-object-model-in-selenium-python

Ref 2: https://www.lambdatest.com/blog/page-object-model-in-selenium-python/

Ref 3: https://medium.com/@zackbunch/page-object-model-pom-in-selenium-python-73d0a805f2a8

Ref 4: https://training.saucelabs.com/codelabs/Module3-SeleniumPython/index.html?index=..%2F..seleniumpython

Ref 5: https://github.com/gunesmes/page-object-python-selenium

Ref 6: https://selenium-python.readthedocs.io/page-objects.html

Project-Directory
     |--------- Src
                    |--------- PageObject
                                       |--------- Pages
                                                    |--------- *Page.py (Implementation of methods that make use of the respective Locators declared in Locators.py) 
                                       |--------- Locators.py
                    |--------- TestBase
                                       |--------- WebDriverSetup.py
     |--------- Test
                    |--------- Scripts
                                       |--------- test_*.py (Implementation of test code)(There should be 1:1 mapping of *Page.py and test_*.py as it helps in making the code more modular)
                    |--------- TestSuite
                                       |--------- TestRunner.py (contains TestSuite, which is a collection of test cases)