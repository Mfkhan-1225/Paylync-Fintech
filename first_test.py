from playwright.sync_api import sync_playwright
import os
from dotenv import load_dotenv

load_dotenv()

app_url = os.getenv("APP_URL")
email = os.getenv("APP_EMAIL")
password = os.getenv("APP_PASSWORD")

# Start Playwright
with sync_playwright() as p:
    # Launch the browser (Chromium)
    browser = p.chromium.launch(headless=False, args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()

    # Go to the login page
    page.goto(app_url)
    # Fill the Email Address field (adjusting the selector based on your page)
    page.fill('input[name="email_address"]', email)  # Use the correct selector for the email field

    # Fill the Password field (adjusting the selector based on your page)
    page.fill('input[name="email_password"]', password)  # Use the correct selector for the password field

    page.wait_for_timeout(2000)

    # Click the Sign In button
    page.click('button')  # Adjust the button selector based on the login screen

    # Click on the Search field
    # page.get_by_placeholder("Search").fill("automationreseller@yopmail.com")

    page.wait_for_timeout(3000)

    page.locator('mat-icon[data-mat-icon-name="menu"]').click()

    page.wait_for_timeout(3000)

    print("here 1")

    page.locator('span:text("Invoices")').locator(
        "xpath=ancestor::a").click()  # Adjust the button selector based on the dashboard menu screen

    print("here 2")
    page.wait_for_timeout(5000)

    page.get_by_role("button", name="CREATE INVOICE").click()

    page.wait_for_timeout(5000)

    print("here 3")

    page.get_by_placeholder("Choose a customer").click()
    page.get_by_text("CP 100", exact=True).click()

    page.wait_for_timeout(5000)

    print("here 4")

    page.get_by_placeholder("Select a Product/Service").click()
    page.get_by_text("Baseball Bat", exact=True).click()
    print("here 422")

    page.wait_for_timeout(5000)

    qty_input = page.get_by_placeholder("QTY")
    qty_input.fill("5")

    page.wait_for_timeout(5000)

    page.get_by_role("button", name="SAVE").click()

    input("Press Enter to close browser...")

    # Close the browser
#  browser.close()
