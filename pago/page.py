import time
from selenium.common.exceptions import NoAlertPresentException

#TODO create WaitForElementError class
from pago.errors import WaitForElementError


class Page(object):

    timeout_seconds = 20

    def __init__(self, driver):
        self.driver = driver

    @property
    def referrer(self):
        return self.driver.execute_script('return document.referrer')

    def find_element_by_locator(self, locator):
        return self.driver.find_element_by_locator(locator)

    def find_elements_by_locator(self, locator):
        return self.driver.find_elements_by_locator(locator)

    def wait_for_available(self, locator):
        for i in range(self.timeout_seconds):
            if self.driver.is_element_available(locator):
                break
            time.sleep(.5)
        else:
            raise WaitForElementError('Wait for available timed out')
        return True

    def wait_for_visible(self, locator):
        for i in range(self.timeout_seconds):
            if self.driver.is_visible(locator):
                break
            time.sleep(.5)
        else:
            raise WaitForElementError('Wait for visible timed out')
        return True

    def wait_for_hidden(self, locator):
        for i in range(self.timeout_seconds):
            if self.driver.is_visible(locator):
                time.sleep(.5)
            else:
                break
        else:
            raise WaitForElementError('Wait for hidden timed out')
        return True

    def wait_for_alert(self):
        for i in range(self.timeout_seconds):
            try:
                alert = self.driver.switch_to_alert()
                if alert.text:
                    break
            except NoAlertPresentException as nape:
                pass
            time.sleep(.5)
        else:
            raise NoAlertPresentException(msg='Wait for alert timed out')
        return True


