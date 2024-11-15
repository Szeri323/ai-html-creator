import os, os.path

def read_from_file(file_name):
    """ Takes file name and reads and returns it content. """
    file = open(file_name, "r")
    content = file.read()
    file.close()
    return content
def write_to_results_history(content, gpts_type="", prompt=""):
    """ Creates results_history dir if it does not exist, counts files inside, creats new file and give it name base on existing files number. """
    if not os.path.exists("./results_history"):
        os.makedirs("./results_history")
    number = len([name for name in os.listdir("./results_history") if os.path.isfile("./results_history/"+name)])
    file_name = "attempt" + str(number+1) + ".txt"
    file = open(f"./results_history/{file_name}", "x")
    file.write(f"gpts: {gpts_type}\npromt: {prompt}\ncontent: {content}")
    file.close()
    
def write_to_html_file(content, file_name="artykul.html"):
    """ Takes content and file name and write it to HTML file. """
    file = open(file_name, "w")
    file.write(content)
    file.close()

def write_to_files(content, gpts_type="", prompt=""):
    """ Takes content, gpts_type and prompt and call other functions and provide necessery arguments. """
    write_to_results_history(content=content, gpts_type=gpts_type, prompt=prompt)
    write_to_html_file(content=content)

def write_to_img(image_urls):
    """ Takes image_urls list, creates img directory if not exists, creates images_urls file that holds generated urls."""
    if not os.path.exists("./img"):
        os.makedirs("./img")
    file = open("./img/img_urls", "a")
    for image_url in image_urls:
        file.write(f"{image_url}\n")
    file.close()
    