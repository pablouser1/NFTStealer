import tweepy
from io import BytesIO
from nftstealer.models import Nft

class Twitter:
    api: tweepy.API

    def __init__(self, consumer_key: str, consumer_secret: str, access_token: str, access_token_secret: str):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)
    
    def send(self, nft: Nft):
        print("Sending to Twitter")
        f = BytesIO(nft.data)
        filename = f'{nft.id}.png'
        media = self.api.media_upload(filename=filename, file=f)
        self.api.update_status(media_ids=[media.media_id_string], status="")
