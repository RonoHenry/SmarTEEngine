from agents.content_creator import create_teespring_post
from agents.platform_adapter import adapt_content
from platforms.x import post_to_x
from platforms.instagram import post_to_instagram
def run():
    post = create_teespring_post()
    x_content = adapt_content(post, "x")
    ig_content = adapt_content(post, "instagram")
    post_to_x(x_content)
    post_to_instagram(ig_content)
if __name__ == "__main__":
    run()