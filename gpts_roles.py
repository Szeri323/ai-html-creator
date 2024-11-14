def create_gpts(gpts_type=""):
    if gpts_type == "":
        return {"role": "system", "content": "You are a helpful assistant."}
    if gpts_type == "programmer":
        return  { 
            "role": "system", 
            "content": """
            You are skilled HTML programer and you specialize in processing and embedding articles in body tags.
            You take raw tekst of article, analize it and suggest ready tag content with additional things like places where it could be imges.
            Images needs to be <img> tags with src='image_placeholder.jpg' atributes. If it is neccesary fix polish character.
            """
        }