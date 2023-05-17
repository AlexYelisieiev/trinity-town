from selenium import webdriver
import pyautogui as pygui
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from datetime import datetime
from image_generation import ImageGenerator
import os
from time import sleep


WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
TIME_TO_IMPLICITLY_WAIT = 15
MAXIMUM_LENGTH = 280


# A class used to generate news
# Also uses ImageGenerator
class AIDGenerator(object):

    def __init__(self, prompt, ai_remember='', style_hint='', banned_words=None) -> None:
        self.prompt = prompt
        self.ai_remember = ai_remember
        self.style_hint = style_hint
        self.banned_words = banned_words or []

    def generateNewsFeed(self) -> tuple[str, str]:
        # Setting options
        options = Options()
        options.add_argument(
            'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        )
        options.add_argument('headless')

        # It was moved inside a cycle for deletig the driver every
        # time if it has to generate a new article
        # # Creating driver
        # driver = webdriver.Chrome(
        #     executable_path=r'./chromedriver.exe',
        #     options=options
        # )
        # driver.set_window_size(WINDOW_WIDTH, WINDOW_HEIGHT)

        # # Tell the driver not to panic if it
        # # doesn't find anything and just wait for n seconds
        # driver.implicitly_wait(TIME_TO_IMPLICITLY_WAIT)

        # TODO: add a function for action perform and reset.
        
        news = ''
        # Check the lengh and banned words
        while not news or len(news) > 280 or len(news) < 100 or any(banned_word.lower() in news.lower() for banned_word in self.banned_words) or news[-1] == ':' or news[-1] == ',':
            # Creating driver
            driver = webdriver.Chrome(
                executable_path=r'./chromedriver.exe',
                options=options
            )
            driver.set_window_size(WINDOW_WIDTH, WINDOW_HEIGHT)

            # Tell the driver not to panic if it
            # doesn't find anything and just wait for n seconds
            driver.implicitly_wait(TIME_TO_IMPLICITLY_WAIT)

            driver.get('https://play.aidungeon.io/main/home')
            driver.refresh()
            sleep(10)
            # Press buttons
            driver.find_element(
                By.XPATH, '//div[contains(text(), "PLAY")]'
            ).click()
            driver.find_element(
                By.XPATH, '//div[@aria-label="Quick Start"]'
            ).click()
            driver.find_element(
                By.XPATH, '//div[text()="Custom"]'
            ).click()

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
                driver.find_element(
                    By.XPATH, '//textarea[@aria-label="Memory"]'
                )
            )
            action.send_keys(self.ai_remember)

            # Enter note
            action.click(
                driver.find_element(
                    By.XPATH, '//textarea[@aria-label="Authors Note"]'
                )
            )
            action.send_keys(self.style_hint)
    
            # NOTE: The oldest model performs better, therefore the
            # following code's commented
            # # Select model
            # action.click(
            #     driver.find_element(
            #         By.XPATH, '//div[contains(text(), "adventure-griffin-v1.2.0")]'
            #     )
            # )
            
            # action.perform()
            # action.reset_actions()

            # sleep(0.5)
            
            # action.click(
            #     driver.find_element(
            #         By.XPATH, '//div[contains(text(), "adventure-griffin-v2.0 (beta)")]'
            #     )
            # )

            action.perform()
            action.reset_actions()

            # Click on prompt field
            action.click(
                driver.find_element(
                    By.XPATH, '//textarea[@placeholder="What happens next?"]'
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
            global raw_news
            raw_news = ' '.join(
                span.text for span in driver.find_elements(
                    By.TAG_NAME, 'span'
                )
            )

            # # Replace special characters
            # unneded_characters = ['\n', '\r', '\t', '\b', '\a', '\f', '\v']
            # for character in unneded_characters:
            #     raw_news.replace(character, '')

            news = raw_news + '\n#AI #AIart #art #AInews #fantasy #fiction\n'

            # Create today's date
            now = datetime.now()
            now = now.strftime('%A, %d, %Y')

            # Add date to generated
            news = news.replace('of the day', f'on {now}').replace('   ', ' ')

            driver.close()
        return raw_news, news
