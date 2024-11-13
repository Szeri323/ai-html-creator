import os, os.path

def read_from_file():
    file = open("article.txt", "r")
    return file.read()

def write_to_file(content, gpts_type="", prompt=""):
    number = len([name for name in os.listdir("./results_history") if os.path.isfile("./results_history/"+name)])
    file_name = "attempt" + str(number+1) + ".txt"
    file = open(f"./results_history/{file_name}", "x")
    file.write(f"""gpts: {gpts_type}
promt: {prompt}
content: {content}""")
    file.close()
    