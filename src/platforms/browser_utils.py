from playwright.sync_api import sync_playwright
def test_login(platform, username, password):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(f"https://{platform}.com")
        page.fill("input[name='username']", username)
        page.fill("input[name='password']", password)
        page.click("button[type='submit']")
        page.wait_for_timeout(5000)  # Wait for login
        print(f"Logged into {platform}: {page.title()}")
        browser.close()
if __name__ == "__main__":
    test_login("x", "your_x_handle", "your_x_pass")