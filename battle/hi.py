import requests
import json

# Insert facebook token here
access_token = "EAACEdEose0cBAKvVkDNfzhCPZBsETxt8aprLFJmrqEZAv4TaXCVg7PwqWMJEeti8RhI2zk9vKNZBFgjWyLKBzbY7zaZCO8hzzNKYn2x66vYq63ullcZCTol2NQaKcLcZBR3P8LwicIZCHZC5iKiwJd09ECaao4mHrYNVQG8tRZAVWZC2t9FZAYxDRvWA8wE1AvJl1ZBMm8THZBYntngZDZD"


def comment_on_posts(posts, amount):
    counter = 0
    for post in posts:
        if counter >= amount:
            break
        else:
            counter = counter + 1
        url = "https://graph.facebook.com/{0}/comments".format(post['id'])
        message = "Hi bro!"
        parameters = {'access_token': access_token, 'message': message}
        s = requests.post(url, data=parameters)


def get_posts():
    payload = {'access_token': access_token}
    r = requests.get('https://graph.facebook.com/me/feed', params=payload)
    result = json.loads(r.text)
    return result['data']


if __name__ == "__main__":
    posts = get_posts()
    comment_on_posts(posts, 25)