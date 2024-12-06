from flask import Flask, jsonify, request, render_template
import os
from dotenv import load_dotenv
from data.api_data_fetcher import fetch_musicbrainz_data, fetch_wikipedia_data, fetch_news_data
from data.topic_generator import generate_topic, generate_topic_wikipedia, generate_topic_news
from data.roberta_model import generate_blog_post
from data.blog_post_publisher import publish_blog_post
from data.social_media_poster import post_to_social_media
from roberta_model import answer_question

load_dotenv()

app = Flask(__name__)

@app.route('/api/generate-blog-post', methods=['GET'])
def generate_blog_post_route():
    musicbrainz_data = fetch_musicbrainz_data()
    wikipedia_data = fetch_wikipedia_data()
    news_data = fetch_news_data()
    
    topic_musicbrainz = generate_topic(musicbrainz_data)
    topic_wikipedia = generate_topic_wikipedia(wikipedia_data)
    topic_news = generate_topic_news(news_data)
    
    blog_post_musicbrainz = generate_blog_post(topic_musicbrainz)
    blog_post_wikipedia = generate_blog_post(topic_wikipedia)
    blog_post_news = generate_blog_post(topic_news)
    
    publish_blog_post(blog_post_musicbrainz)
    publish_blog_post(blog_post_wikipedia)
    publish_blog_post(blog_post_news)
    
    post_to_social_media(blog_post_musicbrainz)
    post_to_social_media(blog_post_wikipedia)
    post_to_social_media(blog_post_news)
    
    return jsonify({'message': 'Blog posts generated, published, and posted to social media!'})

@app.route('/search', methods=['GET'])
def search_route():
    query = request.args.get('query')
    answer = answer_question(query)
    return render_template('search_results.html', answer=answer)

if __name__ == '__main__':
    app.run(debug=True)
