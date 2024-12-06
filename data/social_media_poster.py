import os
import requests

def post_to_social_media(blog_post, topic):
    # Add hashtags to the social media post
    hashtags = '#' + '#'.join(topic.lower().split() + ['music', 'entertainment', 'news'])
    social_media_post = f'{blog_post} {hashtags}'
    
    # Rest of the social media posting code...
    # Twitter API settings
    twitter_api_key = os.getenv('TWITTER_API_KEY')
    twitter_api_secret = os.getenv('TWITTER_API_SECRET')
    twitter_access_token = os.getenv('TWITTER_ACCESS_TOKEN')
    twitter_access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

    # Facebook API settings
    facebook_api_key = os.getenv('FACEBOOK_API_KEY')
    facebook_api_secret = os.getenv('FACEBOOK_API_SECRET')
    facebook_access_token = os.getenv('FACEBOOK_ACCESS_TOKEN')

    # Post to Twitter
    twitter_url = 'https://api.twitter.com/1.1/statuses/update.json'
    twitter_params = {
        'status': blog_post[:280],  # truncate to 280 chars
        'oauth_consumer_key': twitter_api_key,
        'oauth_consumer_secret': twitter_api_secret,
        'oauth_token': twitter_access_token,
        'oauth_token_secret': twitter_access_token_secret
    }
    twitter_response = requests.post(twitter_url, params=twitter_params)

    # Post to Facebook
    facebook_url = 'https://graph.facebook.com/me/feed'
    facebook_params = {
        'access_token': facebook_access_token,
        'message': blog_post
    }
    facebook_response = requests.post(facebook_url, params=facebook_params)

    print('Posted to Twitter:', twitter_response.status_code)
    print('Posted to Facebook:', facebook_response.status_code)
