# AI HTML Content Creator

## Main concepts
The AI HTML Content Creator project is written in Python and uses the OpenAI API to generate HTML code from a given article text. It also suggests HTML tags and image placeholders with alt attributes that can be used as prompts for image creation.

## Project contains:
- main script manages configuration, calls functions, and handles errors,
- api_call.py takes an OpenAI client and makes API calls.
- gpts_roles.py and prompt.py are modules that define the specific behavior of API calls and AI agent.
- content manager allows reading from and writing to files,
- prompt_finder.py searches files for alt atributes,
- results_history directory is created after first program execution. It stores all model anwsers for future analysis.
- requirements file allows the recreation of the enviroment necessary for the program to work correctly,
- HTML files: artykul.html, szablon.html, podglad.html

## Requirements for usage 
1. Ensure Python 3 is installed on your computer,
2. OpenAI Account:
    - You need an account on the OpenAI platform, available [here](https://platform.openai.com/). - **WARNING IT IS NOT FREE** (It is some [free trial for $18](https://community.openai.com/t/how-can-i-get-free-trial-credits/26742), but you need check it by your own) 
    - Note that this account is diffrent from a [ChatGPT account](https://chatgpt.com/). 
    - After registering, generate an API key and export it to your environment variables:

        For Linux and macOS: Use the command below to set your API key:
        ```bash
        export OPENAI_API_KEY="your_api_key"
        ```
        For Windows: Use the command:
        ```cmd
        set OPENAI_API_KEY="your_api_key"
        ```
        Using a .env File:
        Create a .env file in the project’s root directory and add the following line:

        ```makefile
        API_KEY="your_api_key"
        ```

        The dotenv module in the main script will automatically load this file.

First Running

To run the project, ensure you have Python 3 installed and the repository downloaded. Follow the steps below based on your operating system.
For Linux and macOS:

- Open your CLI and navigate to the directory where you want to clone the repository.
- Run the following commands:

    ```bash
    git clone https://github.com/Szeri323/ai-html-creator
    cd ai-html-creator
    pip install -r requirements.txt
    python3 main.py
    ```

For Windows:

- Open your Command Prompt and navigate to the directory where you want to clone the repository.
- Run the following commands:

```cmd
git clone https://github.com/Szeri323/ai-html-creator
cd ai-html-creator
pip install -r requirements.txt
python main.py
```

## For more informations check:
- [OpenAI Docs](https://platform.openai.com/docs/quickstart)
- [Python Docs](https://docs.python.org/3/index.html)
- [Pip Docs](https://pypi.org/project/pip/)

## Ideas for Future Improvements:

- Prompt Optimization: Enhance the quality and efficiency of prompts for better AI outputs.
- Model Selection: Allow users to choose from available models dynamically.
- Website Article Conversion: Add functionality to read and convert article text directly from websites using the requests library.
- Template Generator: Create custom HTML templates for different use cases.
- Preview Generator: Implement a feature to generate and display live previews of the created HTML content.