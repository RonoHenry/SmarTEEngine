import sys
sys.path.append("d:/Projects/SmarTEEngine")
# UTF-8 attempt in Python
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass
def adapt_content(content, platform):
    if platform == "x":
        return content[:280]
    elif platform == "instagram":
        return f"{content} #TeespringSale #StyleYourWay"
    return content
if __name__ == "__main__":
    sample = "🔥👕 New Arrival! Unleash Your Creativity with our Limited Edition T-Shirts on Teespring! 🎨🛍️ Shop now and let your unique style shine! #Teespring #CreativityUnleashed"
    x_content = adapt_content(sample, "x")
    ig_content = adapt_content(sample, "instagram")
    # Try printing, fallback to ASCII if it fails
    try:
        print(x_content)
        print(ig_content)
    except UnicodeEncodeError:
        print("Bash choked on emojis—here’s ASCII:")
        print(''.join(c for c in x_content if ord(c) < 128))
        print(''.join(c for c in ig_content if ord(c) < 128))