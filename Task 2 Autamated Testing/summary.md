**Task 2 Summary: Automated Testing with Selenium**

**Objective**

To automate a test case for a login form using Selenium WebDriver. The test verifies both:

Valid credentials (successful login)

Invalid credentials (login failure message)

**Tools & Setup**

Language: Python

Testing Framework: Selenium WebDriver

AI Tools: GitHub Copilot (used to accelerate scripting logic)

Browser: Chrome (with chromedriver)

**Test Case Description**

1. Valid Login
Input: Correct username and password

Expected Output: Redirect to dashboard or success message

2. Invalid Login
Input: Incorrect username or password

Expected Output: Display of an error message (e.g., "Invalid credentials")

**Screenshots**

**Test Type	       Screenshot**

Valid Login	       valid_login_result.png  

Invalid Login	   invalid_login_result.png

**How AI Enhanced the Process**

Copilot provided instant boilerplate code for:

Setting up the browser

Locating input fields and buttons

Asserting success/error outcomes

Reduced manual coding time by ~50%

Encouraged proper exception handling and waits

**Reflection**

Manual testing of login pages is repetitive and time-consuming. By automating this with AI-assisted Selenium scripts, we:

Increased reliability and repeatability

Reduced human error

Improved test coverage, especially for edge cases

AI tools also made scripting easier for beginners, enabling quicker adaptation of best practices and encouraging clean, reusable test automation code.