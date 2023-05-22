import twitter
from image_generation import ImageGenerator
import aidungeon
from os import system


prompt = 'Top event of the day: '
ai_remember = 'It is a news feed in a local fantasy newspaper of a small fantasy town located somewhere in the forest. Lots of things can happen in such a fantasy place. The time is 50\'s or 70\'s, and only good news allowed. The report contains only one main fantasy news article. Fantasy news must be fun or cool, not sad. There are also news about different fantasy creatures.'
style_hint = 'Use a fantasy newspaper writing style. The report contains only one main fantasy news article.'
banned_words = ['article', 'stab', 'kill', 'dead', 'kidnap', 'second', 'you', 'next event:', 'murder', 'next headline:', 'next article:']
image_style = 'fantasy style, digital painting, artstation, unreal engine, octane render, concept art, hyper realistic lighting, illustration, concept art, fantasy'

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
        image_generator.generate_image(prompt=f'{raw_news}, {image_style}')
        system('cls')
        print('Tweeting the news...')
        twitter.createTweet(ready_to_post_news)
        system('cls')
        print('Done!')
