from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver, EventFiringWebElement
from .webelement import WebElement


def _wrap_elements(result, ef_driver):
    if isinstance(result, WebElement):
        return EventFiringElement(result, ef_driver)
    elif isinstance(result, list):
        return [_wrap_elements(item, ef_driver) for item in result]
    else:
        return result


class EventFiringBrowser(EventFiringWebDriver):
    def __init__(self, driver, event_listener):
        super(EventFiringBrowser, self).__init__(driver, event_listener)


class EventFiringElement(EventFiringWebElement):
    def __init__(self, webelement, ef_driver):
        super(EventFiringElement, self).__init__(webelement, ef_driver)