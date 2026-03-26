# 🍔 Stellar Burgers: UI Automation Framework (Part 3)

![CI/CD Status](https://github.com/AlyaSmirnova/Diplom_3/actions/workflows/ui-tests.yml/badge.svg?branch=main)
[![Python Version](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org)
[![Framework](https://img.shields.io/badge/Framework-Pytest-blue?logo=pytest\&logoColor=white)](https://docs.pytest.org/)
[![Selenium](https://img.shields.io/badge/Tested%20with-Selenium-43B02A?logo=selenium\&logoColor=white)](https://www.selenium.dev)
[![Reports](https://img.shields.io/badge/Reports-Allure-orange?logo=allure)](https://github.com/AlyaSmirnova/Diplom_3)

## ✅ Table of Contents
1. [Description](#-description)
2. [Tech Stack & Tools](#-tech-stack--tools)
3. [Project Architecture (POM)](#-project-architecture-pom)
4. [Advanced Automation Solutions](#-advanced-automation-solutions)
5. [Allure Reporting Features](#-allure-reporting-features)
6. [Test Coverage](#-test-coverage)
7. [Execution Guide](#-execution-guide)
8. 7. [CI/CD Workflow](#-cicd-workflow)

## 💫 Description
This is the final part of the graduation project: a **UI Automation Framework** for the **Stellar Burgers** web service. 
The suite validates critical user paths using **Selenium WebDriver** and the **Page Object Model (POM)** pattern. The framework is designed for cross-browser stability, covering both **Chrome** and **Firefox**.

## 🧑‍💻 Tech Stack & Tools
- **Language:** Python 3.11+
- **Testing Framework:** [Pytest](https://docs.pytest.org/)
- **Browser Automation:** [Selenium WebDriver](https://www.selenium.dev)
- **Design Pattern:** Page Object Model (POM)
- **Reporting:** Allure Framework
- **CI/CD:** GitHub Actions

## 📁 Project Architecture (POM)
```text
Diplom_3/
    ├── .github/workflows/              # CI/CD pipeline configuration 
    ├── allure-results/                 # Raw test execution data (generated after run) 
    ├── pages                           # Page Object classes
    │   ├── base_page.py                # Common wrapper for Selenium methods
    │   ├── main_page.py                # Constructor & Ingredients logic
    │   ├── login_page.py               # Auth & Password recovery navigation
    │   ├── personal_account_page.py    # Profile & Order History management
    │   ├── reset_password_page.py      # Password recovery flow (email & reset steps)
    │   ├── order_queue_page.py         # Real-time Order Feed & Statistics
    │  
    ├── srs/                            # Support modules
    │   ├── config.py                   # Environment & Browser settings
    │   ├── data.py                     # Static test data (user credentials)
    │   ├── locators.py                 # Centralized web element locators
    │ 
    ├── tests/                          # Automated Test Scenarios
    │   ├── test_reset_password_page.py
    │   ├── test_personal_account_page.py
    │   ├── test_main-functionality_page.py
    │   ├── test_order_queue_page.py
    │   
    ├── conftest.py                     # Fixtures
    ├── pytest.ini                      # Pytest & Allure configuration
    ├── requirements.txt                # Project dependencies
    └── README.md                       # Comprehensive project documentation
```

## 🛠 Advanced Automation Solutions

To ensure industry-standard stability and maintainability, the following professional solutions were implemented in this framework:

*   **Dynamic Condition Handling:** Instead of using hardcoded timeouts, the framework implements a custom `wait_for_result_of_condition` (Expected Conditions). This allows the suite to accurately handle asynchronous UI updates, such as waiting for a specific Order ID to appear in the real-time Feed.
*   **JavaScript Injection Strategy:** A `click_with_js` method was implemented in the `BasePage`. This bypasses `ElementClickInterceptedException` caused by non-interactive overlays or lingering modal animations, ensuring 100% test stability in both **Chrome** and **Firefox**.
*   **Data Normalization & Cleaning:** Integrated logic to handle inconsistent string formats. The framework automatically strips `#` symbols and leading zeros (`lstrip('0')`) when validating Order IDs between the confirmation modal and the Order Feed.
*   **Fluent Page Object Model:** 
    *   **Encapsulation:** All locators are strictly separated into `src/locators.py`; test scripts have no direct access to them, following clean code principles.
    *   **Method Chaining:** Page methods return element objects or page instances, allowing for concise and readable test scenarios.
*   **Cross-Browser Compatibility:** Full support for multi-browser execution via `conftest.py` fixtures, with specific adjustments for **GeckoDriver** (Firefox) and **ChromeDriver** behavior.
*   **Smart Invisibility Waits:** Robust logic to wait for modal overlays to fully disappear before proceeding with background interactions, preventing "flaky tests" during high-load scenarios.

## 📊 Allure Reporting Features

The project is integrated with the **Allure Framework** to provide high-level visibility and deep technical analysis of the UI automation process. Key reporting features include:

*   **Behavior-Driven Hierarchy:** Tests are logically structured using `@allure.feature` (e.g., *Main Page*, *Order Feed*) and `@allure.story` (e.g., *Ingredients Modal*, *Real-time Sync*), providing a clear business-level overview.
*   **Granular Step Execution:** Detailed `@allure.step` tracking for every action within Page Objects. This allows for pinpointing exactly where a failure occurred (e.g., "Wait for element to be clickable" vs. "Perform Drag-and-Drop").
*   **Dynamic Data Visualization:** Clear representation of test execution flow, including dynamic variables like generated Order IDs and real-time counter values.
*   **Success & Failure Root-Cause Analysis:** Comprehensive logging of Selenium `TimeoutException` or `AssertionError`, with clean stack traces translated into readable test steps.
*   **Environment Metadata:** The report includes details about the environment, such as the browser used (**Chrome** vs. **Firefox**) and the Base URL, ensuring context for every test run.

## 🧪 Test Coverage

The automation suite provides 100% coverage for the critical user paths of the **Stellar Burgers** web service, ensuring stability across major functional modules:

### 1. Main Page & Burger Constructor
*   **Navigation Logic:** Validating seamless transitions between the "Constructor" and "Order Feed" sections.
*   **Ingredient Management:** 
    *   Opening and closing the detailed information modal for specific ingredients.
    *   Verifying real-time counter increments when ingredients are added to the order.
*   **Order Creation:** 
    *   Testing the **Drag-and-Drop** functionality for both Chrome (ActionChains) and Firefox (JavaScript simulation).
    *   Full checkout flow for authorized users, from adding ingredients to receiving a unique Order ID.

### 2. Live Order Feed & Global Statistics
*   **Real-time Synchronization:** Verifying that a newly created Order ID successfully appears in the general Feed list.
*   **Workflow Tracking:** Ensuring that active orders are correctly displayed in the "At Work" (In Progress) section of the dashboard.
*   **Counter Dynamics:** Validating that "Total Orders" and "Orders Today" statistics increment correctly after a successful purchase.

### 3. User Profile & Session Management
*   **Authorized Access:** Navigating to the Personal Account and "Order History" sections.
*   **Session Termination:** Verifying the "Logout" functionality, ensuring secure session closure and redirection to the Login page.

### 4. Password Recovery Flow (`/forgot-password`)
*   **Entry Points:** Transitioning from the Login form to the recovery initiation page.
*   **Verification Steps:** 
    *   Validating email submission and successful navigation to the password reset form.
    *   **UI/UX Interactions:** Testing the password visibility toggle (eye icon) and verifying active field highlighting during input.

### 5. Cross-Browser & Technical Validation
*   **Browser Compatibility:** Consistent execution across **Chrome** and **Firefox** environments.
*   **Data Integrity:** Multi-stage validation of Order IDs, ensuring data consistency between the confirmation modal and the Feed database.

## 🚀 Execution Guide

### 1. Environment Setup
Clone the repository and set up a local virtual environment to ensure dependency isolation:

1. **Clone repository**
> ```bash 
> git clone https://github.com/AlyaSmirnova/Diplom_3
> cd Diplom_3
📦 Repository: [Diplom_3](https://github.com/AlyaSmirnova/Diplom_3)

2. **Create a virtual environment**
> ```bash 
> python -m venv venv

3. **Activate the virtual environment**
> ```bash 
> source venv/bin/activate

4. **Install required dependencies**
> `$ pip install -r requirements.txt`

### 2. Running Tests
The framework supports parallel execution and cross-browser testing. You can trigger tests using the following commands:
> ```bash 
> pytest

### 3. Generating Allure Report
After the test execution is complete, the `allure-results` folder will be generated. To view the interactive report:
> ```bash 
> allure serve allure-results

## ⚙️ CI/CD Workflow
The project is fully integrated with **GitHub Actions**. The pipeline automatically:
1.  Sets up a **Python 3.11** environment on an Ubuntu runner.
2.  Installs **Chrome** and **Firefox** webdrivers.
3.  Executes the full UI suite in **headless mode**.
4.  Deploys the final **Allure Report** to **GitHub Pages** for easy viewing of test results.
