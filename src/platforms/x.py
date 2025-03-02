import sys
sys.path.append("d:/Projects/SmarTEEngine")
from playwright.sync_api import sync_playwright
import yaml
def post_to_x(content):
    with open("config/credentials.yaml", "r") as f:
        creds = yaml.safe_load(f)["x"]
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://x.com")
        page.fill("input[name='username']", creds["username"])
        page.fill("input[name='password']", creds["password"])
        page.click("button[type='submit']")
        page.wait_for_timeout(5000)
        page.fill("div[role='textbox']", content)
        page.click("button[data-testid='tweetButtonInline']")
        page.wait_for_timeout(2000)
        print("Posted to X!")
        browser.close()
if __name__ == "__main__":
    sample = "🔥👕 New Arrival! Unleash Your Creativity with our Limited Edition T-Shirts on Teespring! 🎨🛍️ Shop now and let your unique style shine! #Teespring #CreativityUnleashed"
    post_to_x(sample)