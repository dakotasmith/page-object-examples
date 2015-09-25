
from selenium.webdriver.support.events import AbstractEventListener
import subprocess


class MaListener(AbstractEventListener):
    def before_quit(self, driver):
        subprocess.call(['say', '"quitting selenium!!!"'])

    def before_find(self, by, value, driver):
        subprocess.call('say "looking by {0} for {1}"'.format(by, value).split())

    def before_click(self, element, driver):
        subprocess.call('say "clicking on a {0} tag"'.format(element.tag_name, element.text).split())

