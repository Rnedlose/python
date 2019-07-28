from selenium import webdriver
from instapy_cli import client
import os
import time

class Bot:

    def __init__(self, username, password):
        """
        Initialize and create an instance of the Bot class.

        Call the login method to authenticate a user with IG.

        Args:   
            username:str: The Instagram username for a user
            password:str: The Instagram password for a user

        Attributes:
            driver:Selenium.webdriver.Chrome: The Chromedriver that is used to automate browser actions.

        """
        self.username = username
        self.password = password
        self.base_url = 'https://www.instagram.com'
        self.driver = webdriver.Chrome('./chromedriver')
        
        self.login()

    def login(self):        
        self.driver.get('{}/accounts/login/'.format(self.base_url))
        time.sleep(2)

        self.driver.find_element_by_name('username').send_keys(self.username)
        time.sleep(2)

        self.driver.find_element_by_name('password').send_keys(self.password)
        time.sleep(2)

        self.driver.find_elements_by_xpath("//div[contains(text(),'Log In')]")[0].click()
        time.sleep(2)
    
    def goto_user(self, user):
        self.driver.get('{}/{}/'.format(self.base_url, user))

    def follow_user(self, user):
        self.goto_user(user)
        time.sleep(2)
        follow_button = self.driver.find_elements_by_xpath("//button[contains(text(), 'Follow')]")[0]
        follow_button.click()

    def post_photos(self):
        directory = ('/home/rod/Desktop/myprojects/Python-Projects/environments/Wallpapers')
        for filename in os.listdir(directory):
            image = directory +'/' + filename
            with client(username, password) as cli:        
                text = input('Enter description and #hashtag for your upload: ')
                cli.upload(image, text)    

if __name__ == '__main__':
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    user = input('What profile would you like to follow: ')
    
    bot = Bot(username, password)
    bot.follow_user(user)

    bot.post_photos()

    time.sleep(2)
    
