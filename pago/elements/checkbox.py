class CheckBox(object):

    def __set__(self, instance, value):
        try:
            e = instance.element.find_element_by_locator(self.locator)
        except AttributeError:
            e = instance.driver.find_element_by_locator(self.locator)
        if e.is_selected() != value:
            e.click()

    def __get__(self, instance, owner=None):
        try:
            e = instance.element.find_element_by_locator(self.locator)
        except AttributeError:
            e = instance.driver.find_element_by_locator(self.locator)
        return e.is_selected()

