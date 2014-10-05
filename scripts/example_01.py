import time
from selenium import webdriver

# Example 01
# The worst example

# Remember to use Chrome against Taco Todos because Persistence.js doesn't seem to be FF compatible without plug-ins

chrome = webdriver.Chrome()
chrome.get('http://localhost:9090/tacotodos/')
time.sleep(2)

chrome.find_element_by_id('new-todo').send_keys('Bacon, egg & cheese taco')
time.sleep(2)

assert True == chrome.find_element_by_class_name('ui-tooltip-top').is_displayed()

# Sending a new line is the equivalent of pressing return
chrome.find_element_by_id('new-todo').send_keys('\n')
time.sleep(1)

first_todo = chrome.find_element_by_class_name('todo')
assert "Bacon, egg & cheese taco" == first_todo.text

# Click the first taco, putting it into edit mode
first_todo.click()
time.sleep(1)

# The text box already has an existing value, so this ends up appending what we send_keys to what is already there
first_todo.find_element_by_name('todo.content').send_keys('Potato & egg taco')
time.sleep(2)

# If we don't want that, we have to clear the element
first_todo.find_element_by_name('todo.content').clear()
time.sleep(1)

first_todo.find_element_by_name('todo.content').send_keys('Potato & egg taco')
time.sleep(1)

first_todo.find_element_by_name('todo.content').send_keys('\n')
time.sleep(1)

# The new name should be displayed and the given taco count should be 1
assert "Potato & egg taco" == first_todo.text
assert "1 taco to eat" == chrome.find_element_by_class_name('todo-count').text

# Click the delete (x) for the first taco in the list
# This can fail because the element is really only visible on hover, and we can't really hover over elements
# Considering that, I am not even sure why this works, TQBH
first_todo.find_element_by_class_name('todo-destroy').click()

# Add three more tacos
chrome.find_element_by_id('new-todo').send_keys('Bean & cheese taco\n')
chrome.find_element_by_id('new-todo').send_keys('Fish taco\n')
chrome.find_element_by_id('new-todo').send_keys('Crispy taco\n')

time.sleep(1)

# There should be a message saying we have 3 tacos to eat, and there should be 3 tacos in our list
assert "3 tacos to eat" == chrome.find_element_by_class_name('todo-count').text
assert 3 == len(chrome.find_elements_by_class_name('todo'))

# I click the checkbox for the last taco in the list
chrome.find_element_by_xpath('//*[@id="todo-list"]/li[3]/div[1]/input').click()

# There should be a message saying we have 2 tacos to eat but we still have 3 tacos in our list
assert "2 tacos to eat" == chrome.find_element_by_class_name('todo-count').text
assert 3 == len(chrome.find_elements_by_class_name('todo'))

# The button to remove tacos we've eaten should be displayed
assert True == chrome.find_element_by_class_name('todo-clear').is_displayed()
assert 'Clear 1 eaten taco' == chrome.find_element_by_class_name('todo-clear').text

chrome.find_element_by_class_name('todo-clear').click()
time.sleep(1)

# Now there should just be 2 items in the list, and the clear button should be hidden
assert 2 == len(chrome.find_elements_by_class_name('todo'))
assert False == chrome.find_element_by_class_name('todo-clear').is_displayed()

# I click the checkboxes for the first and second tacos in the list
# Using XPATH this way to locate these elements would always require clicking the higher numbered elements first
chrome.find_element_by_xpath('//*[@id="todo-list"]/li[1]/div[1]/input').click()
chrome.find_element_by_xpath('//*[@id="todo-list"]/li[2]/div[1]/input').click()
time.sleep(1)

assert "0 tacos to eat" == chrome.find_element_by_class_name('todo-count').text

chrome.close()
chrome.quit()