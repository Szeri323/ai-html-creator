from gpts_roles import create_gpts
from prompt import create_prompt
from content_manager import read_from_file,write_to_files,write_to_img
from prompt_finder import find_prompts


def create_article(client):
    """ The function takes an OpenAI client as an argument and generates the content of an article based on custom parameters such as content, GPTs, and prompts. """
    content = read_from_file("article.txt")
    gpts = create_gpts(gpts_type="programmer")
    prompt = create_prompt(content)
    
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            gpts,
            prompt
        ]
    )

    write_to_files(completion.choices[0].message.content,"", "")
    
def create_image(client):
    """ The function takes an OpenAI client as an argument, uses the find_prompts function to search for alt attributes (which also serve as prompts), and generates images based on them. The images are stored in a list as URLs and written to a file. """
    image_urls = []
    prompts = find_prompts("./artykul.html")
    
    for prompt in prompts:
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        image_url = response.data[0].url
        image_urls.append(image_url)
        
    write_to_img(image_urls)