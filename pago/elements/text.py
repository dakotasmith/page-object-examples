class Text(object):

    def __set__(self, instance, value):
        try:
            e = instance.element.find_element_by_locator(self.locator)
        except AttributeError:
            e = instance.driver.find_element_by_locator(self.locator)
        if value == "clear()":
            e.clear()
        else:
            e.send_keys(value)

    def __get__(self, instance, owner=None):
        try:
            e = instance.element.find_element_by_locator(self.locator)
        except AttributeError:
            e = instance.driver.find_element_by_locator(self.locator)
        text = None
        if e.tag_name in ["input", "textarea"]:
            text = e.get_attribute("value")
        else:
            text = e.text
        return text

