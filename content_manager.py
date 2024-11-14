import os, os.path

def read_from_file():
    file = open("article.txt", "r")
    return file.read()

def write_to_results_history(content, gpts_type="", prompt=""):
    number = len([name for name in os.listdir("./results_history") if os.path.isfile("./results_history/"+name)])
    file_name = "attempt" + str(number+1) + ".txt"
    file = open(f"./results_history/{file_name}", "x")
    file.write(f"gpts: {gpts_type}\npromt: {prompt}\ncontent: {content}")
    file.close()
    
def write_to_html_file(content):
    file = open(f"article.html", "w")
    file.write(content)
    file.close()

def write_to_files(content, gpts_type="", prompt=""):
    write_to_results_history(content=content, gpts_type=gpts_type, prompt=prompt)
    write_to_html_file(content=content)