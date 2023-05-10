from time import sleep
import pyautogui as pygui
from selenium.webdriver import ActionChains
from selenium.webdriver import Chrome
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import config


# Tweets something. Also pastes an image
def createTweet(text: str) -> None:
    # Create opt's and set user agent
    options = Options()
    options.add_argument(
        'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
        )

    driver = Chrome(
        executable_path=r'./chromedriver.exe',
        options=options
    )

    # Window size
    driver.set_window_size(1920, 1080)

    driver.implicitly_wait(10)
    driver.get('https://twitter.com/i/flow/login')
    driver.refresh()

    # Entering nickname
    sleep(10)
    identifier = driver.find_element(By.TAG_NAME, 'input')
    identifier.send_keys(config.user, Keys.ENTER)

    # Entering password
    sleep(10)
    actionChain = ActionChains(driver)
    actionChain.send_keys(config.password, Keys.ENTER)
    actionChain.perform()
    actionChain.reset_actions()
    
    try:
        # Find the main tweet field
        sleep(10)
        placeForText = driver.find_element(
            By.XPATH, '//div[@aria-label="Tweet text"]'
        )
        placeForText.send_keys(text)
    except Exception:
        # Entering email
        sleep(10)
        actionChain.send_keys(config.email, Keys.ENTER)
        actionChain.perform()
        actionChain.reset_actions()

        # Find the main tweet field
        sleep(10)
        placeForText = driver.find_element(
            By.XPATH, '//div[@aria-label="Tweet text"]'
        )
        placeForText.send_keys(text)

    # Paste the generated image
    sleep(1)
    pygui.hotkey('ctrl', 'v', interval=0.5)
    sleep(5)

    # Send the tweet
    for _ in range(10):
        actionChain.send_keys(Keys.TAB)
    actionChain.send_keys(Keys.ENTER)
    actionChain.perform()
    sleep(1)
    driver.close()
