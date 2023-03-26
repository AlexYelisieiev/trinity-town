from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver import Chrome
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
import config


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

    # Entering nickname
    sleep(10)
    identifier = driver.find_element_by_tag_name('input')
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
        placeForText = driver.find_element_by_xpath('//div[@aria-label="Tweet text"]')
        placeForText.send_keys(text)

    except:
        # Entering email
        sleep(10)
        actionChain.send_keys(config.email, Keys.ENTER)
        actionChain.perform()
        actionChain.reset_actions()

        # Find the main tweet field
        sleep(10)
        placeForText = driver.find_element_by_xpath('//div[@aria-label="Tweet text"]')
        placeForText.send_keys(text)

    # Send the tweet
    for _ in range(8):
        actionChain.send_keys(Keys.TAB)
    actionChain.send_keys(Keys.ENTER)
    actionChain.perform()
    
    sleep(1)

    driver.close()
