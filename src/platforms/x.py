from platforms.browser_utils import login_to_platform
def post_to_x(content):
    page, browser = login_to_platform("x")
    page.fill("div[role='textbox']", content)
    page.click("button[data-testid='tweetButtonInline']")
    page.wait_for_timeout(2000)
    print("Posted to X!")
    browser.close()
if __name__ == "__main__":
    post_to_x("Test tweet from SmarTEEngine!")