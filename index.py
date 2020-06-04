from selenium import webdriver

class TinderBot(): # creation of tinder bot
        def __init__(self):
            self.driver = webdriver.Chrome()

        def login(self):
            self.driver.get('https://tinder.com/') # goes to tinder dot com

            self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[1]/div/button') # click Google log in button