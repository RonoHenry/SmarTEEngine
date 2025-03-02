import ollama
import sys
# Force UTF-8 output
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')
def generate_post(prompt):
    response = ollama.chat(model="mistral:latest", messages=[{"role": "user", "content": prompt}])
    return response["message"]["content"].strip()
if __name__ == "__main__":
    print(generate_post("Write a 280-char teaser for a new Teespring t-shirt"))