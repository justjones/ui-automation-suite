# ui-automation-suite
Designed to demonstrate real-world automation engineering practices including maintainable framework design, test reliability strategies, and CI integration.
UI automation framework built using Python, Selenium, and Pytest to validate core user flows of a sample web application.

This project demonstrates clean framework architecture, maintainability principles, and CI-ready automation practices.


Tech stack:
  Python 3.x
  Pytest
  Selenium 4
  Selenium Manager / WebDriver Manager

How to run Locally:
  git clone https://github.com/justjones/ui-automation-suite.git
  cd ui-automation-suite
Create and activate virtual environment:
  bash
  python -m venv venv
  Windows: 
  bash
  venv\Scripts\activate
  Mac/Linux
  bash
  source venv/bin/activate
intstall dependencies:
  bash
  pip install -r requirements.txt
run tests:
  bash
  pytest
run tests in headless mode:
  bash
  pytest --headless
Generate HTML report:
  bash
  pytest --html=reports/report..html

Framework features
  Page Object Model
  Fixtures
  Parametrization (data-driven)
  Wait strategy (explicit waits)
  Logging + screenshots on failure
  Reports
  CI pipeline

Environment Configuration: 
  environment variablels can be configured via:
    .env file (if used)
    Command-line options
    CI secrets (for GitHub Actions)
    Example: bash export BASE_URL=https://example.com
    
Test coverage list:
  The suite currently validates the following flows:
Login (valid & invalid scenarios)
  Product search / filtering
  Add / remove from cart
  Form validation
  Navigation and page verification
 
Framework Architecture

This project follows industry best practices for scalable UI automation:
✔ Page Object Model (POM)
Encapsulates page locators and actions to improve readability and maintainability.
✔ Pytest Fixtures
Reusable driver setup and teardown logic using conftest.py.
✔ Data-Driven Testing
Test parametrization using @pytest.mark.parametrize.
✔ Explicit Wait Strategy
WebDriverWait implementation to improve test stability.
✔ Logging & Screenshots
Automatic screenshots captured on test failure.
✔ Reporting
HTML reports generated via pytest-html.
✔ Continuous Integration
GitHub Actions workflow runs tests automatically on push and pull requests.

Folder structure:
ui-automation-suite/
│
├── src/
│   ├── pages/
│   ├── utilities/
│
├── tests/
│   ├── test_login.py
│   ├── test_cart.py
│
├── reports/
│
├── pytest.ini
├── requirements.txt
└── README.md
