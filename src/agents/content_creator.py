from models.llm_interface import generate_post
def create_teespring_post():
    prompt = "Generate a catchy post for a new Teespring t-shirt sale, keep it short"
    return generate_post(prompt)
if __name__ == "__main__":
    print(create_teespring_post())