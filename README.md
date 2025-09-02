# Sprint_6

Autotests for https://qa-scooter.praktikum-services.ru/ with usage of Selenium, POM and Allure.

## Structure
- '__allure-reports__/': Allure report data
- '__src__/': Sources
- - '__locators__/': Locators
- - '__pages__/': Page Objects
- - __config.py__ - project constants
- '__test__/': Tests
- __.gitignore__: gitignore file
- __conftest.py__: Fixtures
- __pytest.ini__: pytest config
- __requirements.txt__: requirements file 

## Install
- Install _Firefox_ and _geckodriver_
- _pip install selenium pytest allure-pytest_ or _pip install -r reqiurements.txt_

## Tests run
_pytest --alluredir=allure-results_ or simple _pytest_

## Report generating
_allure serve allure-results_