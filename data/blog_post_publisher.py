import os

def publish_blog_post(blog_post, topic):
    # Add meta tags to the blog post
    meta_tags = ', '.join(topic.lower().split() + ['music', 'entertainment', 'news'])
    blog_post_with_meta = f'<meta name="keywords" content="{meta_tags}">{blog_post}'
    
    with open("blog_post.txt", "w") as f:
        f.write(blog_post_with_meta)
    print("Blog post published with meta tags!")
