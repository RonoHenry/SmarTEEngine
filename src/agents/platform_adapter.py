import sys
sys.path.append("d:/Projects/SmarTEEngine")  # Keep path fix
def adapt_content(content, platform):
    if platform == "x":
        return content[:280]  # Safety trim
    elif platform == "instagram":
        return f"{content} #TeespringSale #StyleYourWay"
    return content
if __name__ == "__main__":
    sample = "🔥👕 New Arrival! Unleash Your Creativity with our Limited Edition T-Shirts on Teespring! 🎨🛍️ Shop now and let your unique style shine! #Teespring #CreativityUnleashed"
    print(adapt_content(sample, "x"))
    print(adapt_content(sample, "instagram"))