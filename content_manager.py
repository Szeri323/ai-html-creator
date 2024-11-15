import os, os.path

def read_from_file(file_name):
    """ Takes a file name, reads its content, and returns it. """
    file = open(file_name, "r")
    content = file.read()
    file.close()
    return content
def write_to_results_history(content, gpts_type="", prompt=""):
    """ Creates a results_history directory if it does not exist, counts the files inside, creates a new file, and names it based on the number of existing files. """
    if not os.path.exists("./results_history"):
        os.makedirs("./results_history")
    number = len([name for name in os.listdir("./results_history") if os.path.isfile("./results_history/"+name)])
    file_name = "attempt" + str(number+1) + ".txt"
    file = open(f"./results_history/{file_name}", "x")
    file.write(f"gpts: {gpts_type}\npromt: {prompt}\ncontent: {content}")
    file.close()
    
def write_to_html_file(content, file_name="artykul.html"):
    """ Takes content and a file name, then writes it to an HTML file. """
    file = open(file_name, "w")
    file.write(content)
    file.close()

def write_to_files(content, gpts_type="", prompt=""):
    """ Takes content, gpts_type, and a prompt, then calls other functions and provides the necessary arguments. """
    write_to_results_history(content=content, gpts_type=gpts_type, prompt=prompt)
    write_to_html_file(content=content)

def write_to_img(image_urls):
    """ Takes an image_urls list, creates an img directory if it does not exist, and creates an image_urls file to store the generated URLs."""
    if not os.path.exists("./img"):
        os.makedirs("./img")
    file = open("./img/img_urls", "a")
    for image_url in image_urls:
        file.write(f"{image_url}\n")
    file.close()
    