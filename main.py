# import dependencies
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import pyfirmata

# set up arduino
port = ''
if port != '':
    board = pyfirmata.Arduino(port)

# set up webdriver
driver = webdriver.Firefox()

# have the browser go to leetcode when it launches
driver.get('https://leetcode.com/')

# here's the fun part
while True:
    # put in try-except because I need an easy way out of this hell
    try:
        # check if you are on leetcode
        tabs_list = []
        for handle in driver.window_handles:
            driver.switch_to.window(handle)
            tabs_list.append(driver.current_url)
        for tab in tabs_list:
            if 'leetcode' not in tab:
                print('BAD')
                if port != '':
                    board.digital[13].write(1)
            else:
                print('GOOD')
    # break somewhat gracefully
    except KeyboardInterrupt:
        break