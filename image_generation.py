from time import sleep
import pyautogui as pygui


class ImageGenerator(object):
    '''Generates images using the given prompt and copies them
    to the clipboard.
    '''
    
    def __init__(self, prompt: str = '') -> None:
        self.prompt = prompt

    def generate_image(self, prompt: str) -> None:
        '''The main function for the image generation.
        
        Args:
            prompt: prompt used for the generation. Not modified
            inside the function.
        '''

        allowed_characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890~!*()-_=+[{]}|;:\'\",.?'
        
        prompt = prompt or self.prompt
        # Remove non-ascii characters
        prompt = ''.join(
            symbol if symbol in allowed_characters else ' ' for symbol in prompt
        )
        pygui.press('win')
        pygui.sleep(2)
        pygui.write('google chrome', interval=0.05)
        pygui.sleep(1)
        pygui.press('enter')
        pygui.sleep(0.8)
        for _ in range(4):
            pygui.hotkey('win', 'up')
            pygui.sleep(0.01)
        pygui.sleep(4)
        pygui.write('https://www.bing.com/create', interval=0.05)
        pygui.sleep(0.05)
        pygui.press('enter')
        pygui.sleep(7)
        pygui.click(x=401, y=185)
        pygui.write(prompt, interval=0.07)
        pygui.press('enter')
        pygui.sleep(37)
        pygui.leftClick(x=488, y=422)
        pygui.sleep(5)
        pygui.rightClick()
        pygui.sleep(2)
        pygui.leftClick(542, 483)
        sleep(2)
        pygui.hotkey('alt', 'f4', interval=0.5)
