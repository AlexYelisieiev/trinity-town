from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Keys
from datetime import datetime
import os


WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
TIME_TO_IMPLICITLY_WAIT = 15
MAXIMUM_LENGTH = 280


# A class used to generate news
class AIDGenerator(object):

    def __init__(self, prompt, AIRemember='', styleHint='') -> None:
        self.prompt = prompt
        self.AIRemember = AIRemember
        self.styleHint = styleHint

    def generateNewsFeed(self) -> str:

        # Setting options
        options = Options()
        options.add_argument(
            'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        )
        options.add_argument('headless')

        # Creating driver
        driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe',
            options=options
        )
        driver.set_window_size(WINDOW_WIDTH, WINDOW_HEIGHT)

        # Tell the driver not to panic if it
        # doesn't find anything and just wait for n seconds
        driver.implicitly_wait(TIME_TO_IMPLICITLY_WAIT)

        
        news = ''
        while not news or len(news) > 280 or len(news) < 65:
            driver.get('https://play.aidungeon.io/main/home')

            # Press buttons
            driver.find_element_by_xpath(
                '//div[text()="PLAY"]').click()
            driver.find_element_by_xpath(
                '//div[@aria-label="Quick Start"]').click()
            driver.find_element_by_xpath(
                '//div[text()="Custom"]').click()

            # Create an action chain
            action = webdriver.ActionChains(driver)

            # Let's open settings panel
            for _ in range(33):
                action.send_keys(Keys.TAB)
            action.click()
            action.perform()

            action.reset_actions()

            # Enter mem
            action.click(
                    driver.find_element_by_xpath(
                        '//textarea[@aria-label="Memory"]'
                    )
                )
            action.send_keys(self.AIRemember)

            # Enter note
            action.click(
                driver.find_element_by_xpath(
                    '//textarea[@aria-label="Authors Note"]'
                )
            )
            action.send_keys(self.styleHint)
            action.perform()

            action.reset_actions()

            # Click on prompt field
            action.click(
                driver.find_element_by_xpath(
                    '//textarea[@placeholder="What happens next?"]'
                )
            )
            action.perform()

            action.reset_actions()

            # Enter prompt
            sleep(2)
            action.send_keys(self.prompt, Keys.ENTER)
            action.perform()
            action.reset_actions()

            # Refresh
            sleep(8)
            driver.refresh()
            sleep(10)

            # Find news
            news = ' '.join(
                span.text for span in driver.find_elements_by_tag_name(
                    'span')).strip()
            news = '#AI #AInews\n' + news

            # Create today's date
            now = datetime.now()
            now = now.strftime('%A, %d, %Y')

            # Add date to generated
            news = news.replace('of the day', f'on {now}').replace('   ', ' ')
            
            driver.close()

        return news
