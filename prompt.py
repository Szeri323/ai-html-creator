def create_prompt(content, prompt_type="article"):
    """ Returns a prompt dictionary based on the content and prompt_type. """
    if prompt_type == "article":
        return  {
            "role": "user",
            "content": f"Chciałbym abyś użył tego tekstu: {content}."
        }