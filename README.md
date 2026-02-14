# ui-automation-suite

Production-ready UI automation starter kit built with **Python, Selenium 4, and Pytest**.  
Designed to be cloned and extended for real projects with clean architecture, stable waits, reporting, and CI integration.

---

## ✅ Key Features

- Page Object Model (POM) for maintainability
- Pytest fixtures for driver lifecycle + setup/teardown
- Explicit wait strategy (WebDriverWait) for stability
- Config-driven execution (base URL, browser, headless, timeouts)
- Screenshots on failure + structured logging
- HTML reports (pytest-html)
- CI pipeline via GitHub Actions (runs on PRs and pushes)

---

## 🧰 Tech Stack

- Python 3.10+
- Pytest
- Selenium 4
- Selenium Manager (or WebDriver Manager)
- pytest-html
- GitHub Actions

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/justjones/ui-automation-suite.git
cd ui-automation-suite
