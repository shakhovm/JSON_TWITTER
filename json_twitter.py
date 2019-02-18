import requests
import json
import tweepy
from hidden import oauth


def create_twitter_json(consumer_key, consumer_secret, token_key, token_secret, path):
    """

    (str, str, str, str, str) -> None

    """
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(token_key, token_secret)
    api = tweepy.API(auth)
    t = api.me()
    x = json.loads(json.dumps(t._json, indent=4))
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(x, file, indent=4)


def get_inf_from_json(path, keys):
    with open(path, encoding='utf-8') as file:
        js = json.loads(file.read())
    keys = keys.split('.')
    for key in range(len(keys)):
        js = js[keys[key]]
    return js


if __name__ == "__main__":
    consumer_key, consumer_secret, token_key, token_secret = oauth()["consumer_key"], \
                                                             oauth()["consumer_secret"], \
                                                             oauth()["token_key"], \
                                                             oauth()["token_secret"]
    create_twitter_json(consumer_key, consumer_secret, token_key, token_secret, "twitter_account.json")
    key = input("Enter a key: ")
    print(get_inf_from_json("twitter_account.json", key))
