import sys
sys.path.append('.')

from pago.driver import WebDriver
desired_capabilities = {'browser_name': 'chrome'}
command_executor = "http://127.0.0.1:4444/wd/hub"

from modules.tacotodos.base import TacoTodoPage

class TestTacoTodos(object):

    def setup_method(self, method):
        self.driver = WebDriver(desired_capabilities=desired_capabilities,
                                command_executor=command_executor)
        self.current_method_name = method.__name__

    def teardown_method(self, method):
        self.driver.close()
        self.driver.quit()

    def test_todo_counts(self):
        tacotodos = TacoTodoPage(self.driver).open()
        tacotodos.new_todo = 'Bean and egg taco \n'
        tacotodos.new_todo = 'Potato, egg & cheese \n'
        tacotodos.new_todo = 'Nopales y huevos\n'
        tacotodos.new_todo = 'Crispy taco\n'
        tacotodos.new_todo = 'Cruspy taco\n'
        tacotodos.new_todo = 'Crepes\n'
        assert 6 == tacotodos.todos_remaining
        tacotodos.complete_all_todos()
        assert 6 == tacotodos.todos_completed
        assert 6 == tacotodos.todos_listed
        assert 0 == tacotodos.todos_remaining
        tacotodos.clear_completed_todos()
        assert 0 == tacotodos.todos_listed
        assert 0 == tacotodos.todos_completed

