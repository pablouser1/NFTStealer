from os import getenv, environ
from dotenv import load_dotenv
from nftstealer.Stealer import Stealer
from nftstealer.Twitter import Twitter

def checkEnv(requiredEnv):
    currentEnv = environ
    for env in requiredEnv:
        if not env in environ:
            raise Exception(f'{env} is not set')

def postNft(stealer: Stealer, twitter: Twitter):
    link = stealer.randomLink()
    if link:
        nft = stealer.getNft(link)
        if nft.id:
            # Send to twitter
            twitter.send(nft)

if __name__ == '__main__':
    load_dotenv()
    requiredEnv = [
        'TWITTER_CONSUMER_KEY',
        'TWITTER_CONSUMER_KEY_SECRET',
        'TWITTER_ACCESS_TOKEN',
        'TWITTER_ACCESS_TOKEN_SECRET'
    ]
    checkEnv(requiredEnv)
    # TOKENS
    CONSUMER_KEY = getenv(requiredEnv[0])
    CONSUMER_KEY_SECRET = getenv(requiredEnv[1])
    ACCESS_TOKEN = getenv(requiredEnv[2])
    ACCESS_TOKEN_SECRET = getenv(requiredEnv[3])

    stealer = Stealer()
    twitter = Twitter(CONSUMER_KEY, CONSUMER_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    link = stealer.randomLink()
    if link:
        nft = stealer.getNft(link)
        if nft.id:
            # Send to twitter
            twitter.send(nft)
    
    stealer.cleanup()
