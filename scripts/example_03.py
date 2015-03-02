import sys
sys.path.append('.')

from pago.errors import ExpectedElementError
from pago.driver import WebDriver
desired_capabilities = {'browserName': 'chrome'}
command_executor = "http://127.0.0.1:4444/wd/hub"

from modules.pagesofreps.base import JqueryPagination

driver = WebDriver(desired_capabilities=desired_capabilities, command_executor=command_executor)

test_page = JqueryPagination(driver).open()

while True:
    try:
        test_page = test_page.next()
    except ExpectedElementError as eee:
        break

test_page.driver.close()
test_page.driver.quit()
