from gpts_roles import create_gpts
from prompt import create_prompt
from content_manager import read_from_file,write_to_files,write_to_img
from prompt_finder import find_prompts


def create_article(client):
    """ Function takes open ai client as an argument and generates content of article depends on custom parameters like content, gpts and prompt. """
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
    """ Function takes open ai client as an argument, uses find_promts function to search alt attributes (they are also prompts) and generates images based on them. The images are stored in list as urls and are written to file. """
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