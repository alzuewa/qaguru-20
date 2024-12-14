from appium.webdriver.common.appiumby import AppiumBy
from selene import browser

search_field = browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia'))
input_field = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text'))
search_results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
