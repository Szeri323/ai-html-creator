import re

def find_prompts():
    """ Function search article for alt atributes in html tags and return them as an list. """
    file = open("./artykul.html", "r")
    html_text = file.read()
    
    alt_pattern = re.compile(r'alt="([^"]*)"')
    alt_matches = alt_pattern.findall(html_text)
    alt_values = [match for match in alt_matches]
    
    return alt_values