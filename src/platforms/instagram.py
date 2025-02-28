from platforms.browser_utils import login_to_platform
def post_to_instagram(content, image_path="../data/media/test_tee.jpg"):  # Adjusted path
    page, browser = login_to_platform("instagram")
    page.click("button[class*='_acan']")  # New post button
    page.wait_for_timeout(1000)
    page.query_selector("input[type='file']").set_input_files(image_path)
    page.wait_for_timeout(2000)
    page.click("button[class*='Next']")
    page.wait_for_timeout(1000)
    page.fill("textarea", content)
    page.click("button[class*='Share']")
    page.wait_for_timeout(2000)
    print("Posted to Instagram!")
    browser.close()
if __name__ == "__main__":
    post_to_instagram("Test post from SmarTEEngine!")