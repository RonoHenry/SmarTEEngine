import ollama
def generate_post(prompt):
    response = ollama.chat(model="mistral", messages=[{"role": "user", "content": prompt}])
    return response["message"]["content"].strip()
if __name__ == "__main__":
    print(generate_post("Write a 280-char teaser for a new Teespring t-shirt"))