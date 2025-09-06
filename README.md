
## OrangeHRM Automation Framework (Python + Selenium + Pytest)

This is a **hybrid automation framework** built with **Python, Selenium, and Pytest**.  
The framework is designed to test the **OrangeHRM web application**, but it can be extended to any web project.  
It follows the **Page Object Model (POM)** design pattern, which makes the code **clean, reusable, and easy to maintain**.  


The framework includes:
- Cross-browser support (Chrome, Firefox, Edge)
- Logging system
- Configuration management
- Screenshots on failure
- HTML test reports
- Support for grouping tests (sanity, regression)

 ## Project Folder Structure
Here is how the project is organized. Each folder and file has a clear responsibility.

📦 OrangeHRM_Automation_Framework

├── 📂 configuration
    
     └── config.ini     # Stores environment details like URL, username, password

├── 📂 logs

    └── automation.log    # Stores logs for each test execution

├── 📂 pageObjects

     └── LoginPage.py     # Page Object class for login page
     └── DashboardPage.py # Example for dashboard page

├── 📂 testCases


    └── conftest.py        # Pytest fixtures (browser setup, teardown, hooks)
     └── test_login.py     # Test case that verifies login functionality
     └── test_dashboard.py # Example test case for dashboard

├── 📂 utilities
     
     └── readProperties.py   # Reads values from config.ini
     └── customLogger.py     # Provides reusable logging utility

├── 📂 reports

     └── pytest_report.html   # Stores HTML reports of test execution

├── 📂 screenshots

     └── failed_test.png     # Stores screenshots of failed test cases

├── requirements.txt    # List of required Python packages


├── pytest.ini     # Pytest configuration (markers, options)

├── run.bat         # Batch file for test execution
## Features Explained
1. **Page Object Model (POM):** Each web page is represented by a Python class with its own locators and methods. This avoids code duplication.  
2. **Cross-browser Testing:** You can run tests on different browsers (Chrome, Firefox, Edge) by passing a parameter.  
3. **Configuration Management:** Common values like URL and login credentials are stored in `config.ini`. This avoids hardcoding values inside test cases.  
4. **Custom Logging:** Every step in the test execution is logged into `logs/automation.log` for easy debugging.  
5. **Screenshots on Failure:** If a test fails, the framework automatically captures a screenshot and saves it inside the `screenshots/` folder.  
6. **Reports:** After execution, a clean HTML report is generated inside the `reports/` folder showing test results.  
7. **Pytest Fixtures:** Fixtures in `conftest.py` handle browser setup and teardown in a reusable way.  
8. **Grouping Tests:** You can mark tests as `sanity` or `regression` and run them selectively.  

---
## Getting Started

### 1. Prerequisites
- Install **Python 3.11+**  
- Install **pip** (Python package manager)  
- Install browser drivers (e.g., ChromeDriver, GeckoDriver)  

### 2. Install Dependencies
All required packages are listed in `requirements.txt`. Install them with:
```bash
pip install -r requirements.txt

```

### 3. Run Tests
Run all tests with Chrome (default):
```bash
pytest -v -s --html=reports/report.html
```

Run tests in parallel (using pytest-xdist):

```bash 
pytest -v -s -n=3 --browser chrome --html=reports/report.html
```



## Reports, Logs & Screenshots

- Logs: Execution logs are saved in `logs/automation.log.` They show steps, failures, and errors.

- Reports: After execution, a test summary is generated in `reports/pytest_report.html.`

- Screenshots: If a test fails, a screenshot is captured automatically and stored in `screenshots/.`

## Future Enhancements

- Integrate with Jenkins CI/CD for automated execution.

- Add Allure Reports for advanced reporting.

- Implement Data Driven Testing using Excel (openpyxl).

- Expand framework for API testing along with UI tests.
## Authors

- ‍Author

Developed by Bhushan 

Contact: bhushanambilkar25@gmail.com

This project is open for learning and contributions. Feel free to fork and enhance it.
