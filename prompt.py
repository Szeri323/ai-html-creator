def create_prompt(content, prompt_type=""):
    if prompt_type =="":
        return  {
            "role": "user",
            "content": f"Chciałbym abyś użył tego tekstu: {content}."
        }