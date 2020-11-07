def greece():
    greeting = "Main.py"
    embed = "https://gist.github.com/Naweid/263d70f64f93acadb788b2e06cb2aaf5"
    info = {"greeting": greeting, "embed": embed}
    return info

def spain():
    greeting = "Welcome to Spain"
    embed = "http://127.0.0.1:5000/spain/"
    info = {"greeting": greeting, "embed": embed}
    return info

def france():
    greeting = "All.html"
    embed = "https://gist.github.com/Naweid/caee047f7f4a88159fcb16327b7d1413"
    info = {"greeting": greeting, "embed": embed}
    return info

def germany():
    greeting = "Welcome to Germany"
    embed = "http://127.0.0.1:5000/italy/"
    info = {"greeting": greeting, "embed": embed}
    return info

def alldata():
    return [greece(), spain(), france(), germany()]

#Data "setup" for Projects
#next step would be to extract project data from a database
def setup():
    #Source Data
    name = "Nighthawk Coding"
    github = "https://github.com/nighthawkcoders"
    linkedin = "https://www.linkedin.com/in/john-mortensen-1021/"
    youtube = "https://www.youtube.com/channel/UClIKOsDS5dsfzFA3zveDT3Q?view_as=subscriber"
    twitter = "https://twitter.com/NighthawkCoding"
    source = {"name": name, "github": github, "linkedin": linkedin, "youtube": youtube, "twitter": twitter}