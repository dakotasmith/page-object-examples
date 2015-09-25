from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from pago.errors import ExpectedElementError
from pago.page import Page

locators = {
    'loading_indicator': 'id=loading',
    'search_results': 'id=Searchresult',
    'next_button': 'class=next',
    'prev_button': 'class=prev'

}

page_url = "http://127.0.0.1:9090/pagesofreps/"

class JqueryPagination(Page):

    def wait_until_loaded(self):
        self.wait_for_available(locators['search_results'])
        try:
            self.wait_for_hidden(locators['loading_indicator'])
        except NoSuchElementException as nsee:
            pass
        except StaleElementReferenceException as sere:
            pass
        self.wait_for_available(locators['search_results'])
        return self

    def open(self):
        self.driver.get(page_url)
        return self.wait_until_loaded()

    def next(self):
        e = self.find_element_by_locator(locators['next_button'])
        if e.tag_name == 'a':
            e.click()
        else:
            raise ExpectedElementError('Tried to click Next button but not a link')
        return self.wait_until_loaded()

    def prev(self):
        self.find_element_by_locator(locators['prev_button']).click()
        return self.wait_until_loaded()

