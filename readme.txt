Code examples for PyTexas2014 talk "Page Objects without a Net"

The example sites are easily served locally. Just switch to the sites
dir and run the following command:

python -m SimpleHTTPServer 9090

Then navigate to http://localhost:9090/ in your browser to see the two demo sites. Ctrl+c will break and quit serving the pages. 

Pago contains a barebones framework for page objects, subclassing Selenium's WebDriver and WebElement.

Two implementations of pago are in modules. 

The scripts dir contains 3 examples. It is expected they are run from the same dir this readme.txt is in.

Example 01 contains everything you should never do. To run it:

python scripts/example_01.py

Example 02 shows how this could be used with py.test. It is run via:

py.test scripts/example_02.py

Example 03 shows how to use it in a stand alone script.

python scripts/example_03.py

Thanks to Adam Goucher for his talk Selenium, You're Doing It Wrong and A Really, Really Fast Tour of WebDriver. If you are looking for a complete Python / Selenium framework for testing with page objects, I recommend py.saunter, Adam's page object testing framework for Python. Unlike the examples here, py.saunter handles test running, environment configuration, as well as providing a framework for you to create page objects.
