import re

def find_prompts(file_name):
    """ The function searches an article for alt attributes in HTML tags and returns them as a list. """
    file = open(file_name, "r")
    html_text = file.read()
    
    alt_pattern = re.compile(r'alt="([^"]*)"')
    alt_matches = alt_pattern.findall(html_text)
    alt_values = [match for match in alt_matches]
    
    return alt_values