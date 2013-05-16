import time

import inject

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


@inject.param("browser", "webdriver")
def sample_search(browser):
    browser.get("http://www.yahoo.com")  # Load page
    assert "Yahoo!" in browser.title
    elem = browser.find_element_by_name("p")  # Find the query box
    elem.send_keys("seleniumhq" + Keys.RETURN)
    time.sleep(0.2)  # Let the page load, will be added to the API
    try:
        link_xpath = "//a[contains(@href,'http://seleniumhq.org')]"
        browser.find_element_by_xpath(link_xpath)
    except NoSuchElementException:
        assert 0, "can't find seleniumhq"
