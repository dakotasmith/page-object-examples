import sys
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver

sys.path.append('.')

from pago.errors import ExpectedElementError
from pago.driver import WebDriver
from pago.listener import MaListener

desired_capabilities = {'browserName': 'chrome'}
command_executor = "http://127.0.0.1:4444/wd/hub"

from modules.pagesofreps.base import JqueryPagination

remote_webdriver = WebDriver(desired_capabilities=desired_capabilities, command_executor=command_executor)
driver = EventFiringWebDriver(remote_webdriver, MaListener())
test_page = JqueryPagination(driver)
test_page.open()

while True:
    try:
        test_page = test_page.next()
    except ExpectedElementError as eee:
        break

test_page.driver.close()
test_page.driver.quit()
