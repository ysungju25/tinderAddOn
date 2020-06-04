from selenium import webdriver
import time

class TinderBot(): # creation of tinder bot
        def __init__(self):
            #self.msg = webdriver.Chrome()
            self.driver = webdriver.Chrome()
    

        #def scrt_code(self):
            #self.msg = webdriver.Chrome()
            
            
            

        def login(self):
            self.driver.get('https://tinder.com/') # goes to tinder dot com

            #self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[1]/div/button') # This finds the xpath it doesn't click it
            # your xpath 

            gButton=self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[1]/div/button')
            gButton.click()


            #switch to google login
            base_window = self.driver.window_handles[0] # base window

            popup = self.driver.switch_to_window(bot.driver.window_handles[1]) # login window

            email_in= self.driver.find_element_by_xpath('//*[@id="identifierId"]')
            email_in.send_keys('RJamesTBot@gmail.com')

            nxt_btn= self.driver.find_element_by_xpath('//*[@id="identifierNext"]')
            nxt_btn.click() 

            pw_in = self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
            pw_in.send_keys('tinderBot') 

            nxt_pw =self.driver.find_element_by_xpath('//*[@id="passwordNext"]')
            nxt_pw.click() 

            #phn_in = bot.driver.find_element_by_xpath('//*[@id="phoneNumberId"]')
           # phn_in.send_keys('5713558188')

    


