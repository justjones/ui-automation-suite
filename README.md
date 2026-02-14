# ui-automation-suite

Production-ready UI automation starter kit built with **Python, Selenium 4, and Pytest**.  
Designed for scalable test architecture, reliability, and CI integration.

---

## Tech Stack

- Python 3.10+
- Pytest
- Selenium 4
- Selenium Manager
- pytest-html
- GitHub Actions

---

## Quick Start

```bash
git clone https://github.com/justjones/ui-automation-suite.git
cd ui-automation-suite
python -m venv venv

## create virtual enviroment

- python -m venv venv

## Activate
- Windows: bash
  venv\Scripts\activate
- Mac/Linux: bash
  source venv/bin/activate

## Install depedencies
- bash
  pip install -r requirements.txt
## USAGE
- Run full test suite:
  bash
    pytest
- Run headless
  bash
    pytest --headless
- Run specific suite
  bash
    pytest tests/ui
- Generate HTML report
  bash
    pytest --html=reports/report.html --self-contained-html

## Configuration
- Supported CLI options
    --base-url
    --browser (chome/firefox)
    --headless
example: pytest --base-url=https://www.saucedemo.com --browser=chrome --headless
Environment varibles (optional)
  export BASE_URL=https://www.saucedemo.com
  export BROWSER=chrome

## Architecture
  Page Object Model
  Pytest fixtures (driver lifecycle)
  Explicit wait strategy (WebDriverWait)
  Screenshots on failure
  HTML reporting
  CI execution on push / pull request

## Project Structure

ui-automation-suite/
├── src/
│   ├── pages/
│   └── utilities/
├── tests/
│   └── ui/
├── reports/
├── .github/workflows/
├── pytest.ini
├── requirements.txt
└── README.md







