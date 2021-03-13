def not_now(browser):
    not_now_button = browser.find_elements_by_xpath("//button[text()='Not Now']")
    if not_now_button:
        not_now_button[0].click()