import yaml
def load_credentials():
    with open("../config/credentials.yaml", "r") as f:  # Adjusted path
        return yaml.safe_load(f)
if __name__ == "__main__":
    print(load_credentials())