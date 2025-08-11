from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

PROMISED_DOWN = 80
PROMISED_UP = 80
class Internet_speed_twitter_bot:
    def __init__(self):
        self.down = 0
        self.up = 0
    def get_internet_speed(self):
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chrome_option)
        driver.get("https://www.speedtest.net/")
        go_button = driver.find_element(By.CLASS_NAME,'start-text')
        go_button.click()
        sleep(60)
        down_speed = driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        up_speed = driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.up = float(up_speed.text)
        self.down = float(down_speed.text)
        print(self.up)
        print(self.down)
    def tweet_at_provider(self):
        if self.up < PROMISED_UP or self.down < PROMISED_DOWN:
            print(self.up)
            print(self.down)
            chrome_option = webdriver.ChromeOptions()
            chrome_option.add_experimental_option("detach", True)
            driver = webdriver.Chrome(options=chrome_option)
            driver.get("https://twitter.com/?lang=en")
            sleep(2)
            try:
                sign_in_button = driver.find_element(By.XPATH,
                                                     '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a/div')
                sign_in_button.click()
                sleep(3)
                email = driver.find_element(By.XPATH,
                                            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
                email.send_keys("ritowork25@gmail.com", Keys.ENTER)
                sleep(3)
                password = driver.find_element(By.XPATH,
                                               '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
                password.send_keys("ritotweet@123", Keys.ENTER)
            except NoSuchElementException:
                user_name = driver.find_element(By.XPATH,
                                                '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
                user_name.send_keys("ritospacee", Keys.ENTER)
                sleep(2)
                password = driver.find_element(By.XPATH,
                                               '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
                password.send_keys("ritotweet@123", Keys.ENTER)
                sleep(4)
                message = driver.find_element(By.XPATH,
                                              '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
                tweet = f'Hey @AllianceBroadb1, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?Please fix it'
                message.send_keys(tweet)
                sleep(5)
                send_button = driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div/span/span')
                send_button.click()

bot = Internet_speed_twitter_bot()
bot.get_internet_speed()
bot.tweet_at_provider()