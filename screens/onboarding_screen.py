from appium.webdriver.common.appiumby import AppiumBy
from selene import browser

skip_button = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button'))
add_language_button = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/addLanguageButton'))
paginator = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/view_onboarding_page_indicator'))
continue_button = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button'))
page_title = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView'))
get_started_button = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_done_button'))
