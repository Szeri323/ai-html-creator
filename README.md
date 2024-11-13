# AI HTML Content Creator

## AI HTML Content Creator project is written in Python and uses OpenAI API.

## Main concepts
AI HTML Content Creator creates HTML code from given text of article. It makes propositions of tags HTML and image placeholders.

## AI HTML Content Creator contains:
- main script that import other modules, calls function and handle errors,
- gpts_roles.py and prompt.py are modules that creates specific behaviore of api calls. Because of those two module we can manage of AI agent behaviore,
- content manager allows to read and write files,
- results_history dir is created after first execution of the program. It has to save all model anwser in case of future analize.
- requirements file allows recreate envirement need for poper working of program,

## Requirements for usage 
- You have to had python 3 installed on your computer,
- You need an account on open.ai platform available [here](https://platform.openai.com/). **WARNING IT IS NOT FREE** (It is some [free trial for $18, but you need check it by your own](https://community.openai.com/t/how-can-i-get-free-trial-credits/26742)) and it is diffrent account than [ChatGPT account](https://chatgpt.com/). Next you need to generate api key and export it to your envirement variables for linux and mac:  windows: 

### To run the project make sure you have installed Python 3 and downloaded this repository. Open your cli and make sure you are in project root directory and type (you ommit & and > signs): 
for linux and mac:
```
$ git clone https://github.com/Szeri323/ai-html-creator
$ pip install -r requirements.txt
$ python3 main.py
```
or for windows:
```
> git clone https://github.com/Szeri323/ai-html-creator
> pip install -r requirements.txt
> python main.py
```

## For more informations check:
- [OpenAI Docs](https://platform.openai.com/docs/quickstart)
- [Python Docs](https://docs.python.org/3/index.html)
- [Pip Docs](https://pypi.org/project/pip/)