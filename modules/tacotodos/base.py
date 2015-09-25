from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from pago.elements.checkbox import CheckBox
from pago.errors import ExpectedElementError, WaitForElementError
from pago.page import Page
from pago.elements.text import Text

locators = {
    'new_todo': 'id=new-todo',
    'tooltip_enter': 'class=ui-tooltip-top',
    'todo': 'class=todo',
    'todo_content': 'name=todo.content',
    'todo_count': 'class=todo-count',
    'todo_clear': 'class=todo-clear',
    'todo_done': 'name=todo.done'
    ''

}

page_url = "http://localhost:9090/tacotodos"


class NewTodo(Text):

    def __init__(self):
        self.locator = locators['new_todo']


class TacoTodoPage(Page):
    new_todo = NewTodo()

    @property
    def todos_completed(self):
        count = 0
        e = self.find_elements_by_locator(locators['todo_clear'])
        if e and e[0].text:
            count = int(e[0].text.split()[1])
        return count

    @property
    def todos_remaining(self):
        count = 0
        e = self.find_elements_by_locator(locators['todo_count'])
        if e and e[0].text:
            count = int(e[0].text.split(' ')[0])
        return count

    @property
    def todos_listed(self):
        return len(self.find_elements_by_locator(locators['todo']))

    def open(self):
        self.driver.get(page_url)
        return self.wait_until_loaded()

    def wait_until_loaded(self):
        self.wait_for_available(locators['new_todo'])
        return self

    def clear_completed_todos(self):
        try:
            self.find_element_by_locator(locators['todo_clear']).click()
        except ElementNotVisibleException as enve:
            raise ExpectedElementError()

    def complete_all_todos(self):
        [TacoTodoWrap(self.driver, e).complete() for e in self.find_elements_by_locator(locators['todo'])]


class TacoTodoWrap(object):

    class TodoDone(CheckBox):

        def __init__(self):
            self.locator = locators['todo_done']

    done = TodoDone()

    def __init__(self, driver, element):
        self.driver = driver
        self.element = element

    def edit(self):
        self.element.click()

    def complete(self):
        if not self.done:
            self.done = True
