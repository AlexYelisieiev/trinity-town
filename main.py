import twitter
import aidungeon
from os import system


prompt = 'Top event of the day: '
AIRemember = 'It is a news feed in a local newspaper of a small FANTASY (it is important) town located somewhere in the forest. The time is 50\'s or 70\'s. The town is fantasy. News are mostly about unreal stuff going on in the city and around it. Only good news allowed.'
styleHint = 'Use a newspaper writing style. Always write only one sentence. Only good news allowed.'

if __name__ == '__main__':
    g = aidungeon.AIDGenerator(
        prompt=prompt,
        AIRemember=AIRemember,
        styleHint=styleHint
    )

    while True:
        system('cls')
        news = g.generateNewsFeed()
        system('cls')
        print(news)
        action = input(
            'Tweet the news? (y - yes / n - no / e - exit): '
        ).lower().strip()
        if action == 'y':
            break
        elif action == 'e':
            quit()

    system('cls')
    twitter.createTweet(news)
    system('cls')
    print('Done!')
