#  Drinkwell Automation Testing
 The "Drinkwell Project Selenium Functional Testing Automation" is an automated testing framework using Selenium to perform functional tests on the Drinkwell 
 project, ensuring its features work as expected.
 This repository contains the Selenium-based functional testing automation scripts for the Drinkwell application. The tests are written in Python and utilize 
 the Selenium WebDriver with Chrome for execution.

## Project Overview
 The Drinkwell application provides a comprehensive platform for managing water-related resources. This automation project tests critical functionalities to 
 ensure the application's reliability and usability.

## Server URL: http://13.214.1.75/#/login

## Technologies Used
Python: Programming language for scripting.
Selenium WebDriver: For browser automation.
ChromeDriver: Browser driver for Chrome.
Pytest: Testing framework for organizing and executing test cases.
Prerequisites
## Before running the test scripts, ensure the following:

Python (version 3.8 or above) is installed.
Google Chrome is installed, and the version matches the downloaded ChromeDriver.
## Install required Python packages by running:
bash
pip install -r requirements.txt

## Test Scripts
The following scripts are included:

tests/Login_Reviewing_Info.py: Tests login and info review functionality.
tests/Change_pass_Logout_invalid_login.py: Validates password change, logout, and invalid login attempts.
tests/account_add_edit_delete.py: Handles adding, editing, and deleting user accounts.
tests/add_new_card_recharge_card_assign_card_to_user.py: Tests adding cards, recharging cards, and assigning cards to users.
tests/check_balance_View_Cards_assign_Cards.py: Validates balance checks and card management.
tests/All_Setting.py: Comprehensive tests for all settings and configurations.

## Drinkwell Automation Testing
Drinkwell_Project_Selenium_Functional-Testing_Automation/
├── .vscode/                  # VS Code settings
├── tests/                    # Test scripts
│   ├── All_Setting.py
│   ├── Change_pass_Logout_invalid_login.py
│   ├── Login_Reviewing_Info.py
│   ├── account_add_edit_delete.py
│   ├── add_new_card_recharge_card_assign_card_to_user.py
│   ├── check_balance_View_Cards_assign_Cards.py
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation

## License
This project is licensed under the MIT License.


