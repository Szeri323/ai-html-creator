def create_prompt(content, prompt_type="article"):
    """ Returns prompt dictionary based on content and prompt_type. """
    if prompt_type == "article":
        return  {
            "role": "user",
            "content": f"Chciałbym abyś użył tego tekstu: {content}."
        }