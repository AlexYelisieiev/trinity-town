import twitter
from image_generation import ImageGenerator
import aidungeon
from os import system


prompt = 'Top event of the day: '
AIRemember = 'It is a news feed in a local newspaper of a small FANTASY (it is important) town located somewhere in the forest. The time is 50\'s or 70\'s. The town is fantasy. News are mostly about unreal stuff going on in the city and around it. Only good news allowed. The report contains only one main news.'
styleHint = 'Use a newspaper writing style. Only good news allowed. The report contains only one main news.'

if __name__ == '__main__':
    g = aidungeon.AIDGenerator(
        prompt=prompt,
        AIRemember=AIRemember,
        styleHint=styleHint
    )

    while True:
        system('cls')
        raw_news, ready_to_post_news = g.generateNewsFeed()
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
    generator = ImageGenerator()
    generator.generate_image(prompt=f'{raw_news}, digital art, fantasy style, artstation')
    system('cls')
    print('Tweeting the news...')
    twitter.createTweet(ready_to_post_news)
    system('cls')
    print('Done!')
