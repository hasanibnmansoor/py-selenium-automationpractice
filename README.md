# py-selenium-automationpractice
Python Selenium Web Automation Framework for automationpractice.com

Python-Selenium based UI automation test framework for `http://www.automationpractice.com`, loosely based on the Page Object Model design pattern popular for Web based automation testing. Tests are written in pure python using Pytest test framework.

## Installation Instructions

Note: This framework was developed and tested in Mac OS.

* Python 3.7 +. Follow Instructions here to install latest python versions: https://realpython.com/intro-to-pyenv/. Recommended to have a virtualenv created prior to downloading script from Github.

* In the directory of interest, clone the repository:
```
pyenv activate <virtualenv-name> # Skip this step is virtualenv is not created.
git clone https://github.com/hasanibnmansoor/py-selenium-automationpractice.git
cd py-selenium-automationpractice/
pip install -e .
```
## How is framework folders structured?

* `helpers/base.py` Module has a class `BaseDriver` which is used as a base helper class that, all page object classes would inherit.
* `pages` sub-package to hold all page objects.
      * `home`
      * `women`
      * `cartmodal`
      * `cartsummary`
      * `productdetails`
      * `payment`
      * `shipping`
      * `authentication`
      * `address`
* `utilities` Common Package Utilities
* `tests` Package for Tests. Follows `pytest` framework structure
      * `conftest.py` - Holds Fixtures and Setup/Teardown logic
      * `pytest.ini` - Default CLI Arguments

## How are tests written?

Contrary to common Class Based Tests (unittest/JUnit style tests), tests are written using Pytest framework structure using pytest fixtures to handle the setup and teardown mechanism. Command line argument defaults are stored in pytest.ini file.

CLI arguments required to be passed in during test execution:
```
    --browser <Chrome | Firefox> : Takes in values 'Chrome' & 'Firefox'. Based on user provided value, framework would initiate respective webdriver. This makes this framework a mini-cross-broswer framework as well. Defaults to Firefox (for test).
    --implictlyWait : Defaults to 60 seconds. However, based on requirement, we could provide any greater or lesser value during runtime.
    --reruns : Defaulted to 2 times. Detemrines number of times test reruns on failure
    --html= --self-contained-html : Optional. For getting HTML Reports.
    --username Account used to login automationpractice.com
    --password Password used to login automationpractice.com
```

## How to run tests?
```
# Go to tests/ folder and run
cd ~/pyautomationpractice/tests/
pytest
# Note above default CLI arguments are already set in pytest.ini file inside tests folder. If wish to modify defaults, then provide the values in CLI, like
pytest --reruns 2 --broswer Chrome
```
## Future Improvements

This is a minimalistic framework designed to support one end-to-end product order scenario for testing purposes. To make it a full-fledged framework, following improvements could be made out:
* Refactor BaseDriver class
* Implement Screenshot on Failure Utility
* Custom Reporting Mechanism
* More Granular Functional Test Verification
* etc..

