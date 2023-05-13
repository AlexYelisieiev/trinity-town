import twitter
from image_generation import ImageGenerator
import aidungeon
from os import system


prompt = 'Top event of the day: '
ai_remember = 'It is a news feed in a local newspaper of a small fantasy town located somewhere in the forest. Lots of things can happen in such a fantasy place. The time is 50\'s or 70\'s. Only good news allowed. The report contains only one main news article. Lots of things can happen in such a fantasy place. News must be fun or cool, not sad. The news is fantasy.'
style_hint = 'Use a newspaper writing style. The report contains only one main news article.'
banned_words = ['next event:', 'next headline:', 'next article:', 'found dead', 'finds dead', 'kills', 'killed']

if __name__ == '__main__':
    news_generator = aidungeon.AIDGenerator(
        prompt=prompt,
        ai_remember=ai_remember,
        style_hint=style_hint,
        banned_words=banned_words
    )
    while True:
        while True:
            system('cls')
            raw_news, ready_to_post_news = news_generator.generateNewsFeed()
            system('cls')
            print(ready_to_post_news)
            action = input(
                'Tweet the news? (y - yes / n - no / e - exit): '
            ).lower().strip()
            if action == 'y':
                break
            elif action == 'e':
                quit()

        system('cls')
        print('Generating an image...')
        # Generate an image
        image_generator = ImageGenerator()
        image_generator.generate_image(prompt=f'{raw_news}, digital art, fantasy style, ultra realistic, artstation')
        system('cls')
        print('Tweeting the news...')
        twitter.createTweet(ready_to_post_news)
        system('cls')
        print('Done!')
