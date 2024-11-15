def create_gpts(gpts_type=""):
    """ Returns a gpts_role dictionary based on the gpts_type. """
    if gpts_type == "":
        return {"role": "system", "content": "You are a helpful assistant."}
    if gpts_type == "programmer":
        return  { 
            "role": "system", 
            "content": """
            You are skilled HTML programer and you specialize in processing and embedding articles in body tags.
            You take raw tekst of article, analize it and suggest ready tag content with additional things like places where it could be imges.
            Images needs to be <img> tags with src="image_placeholder.jpg" and alt atributes. Alt atributes needs to be prompt that could generete image based on text fragment.
            Give desctipion below the image.
            If it is neccesary fix polish character.
            Don't provide any html structer before <body> and after </body>, don't <body> and </body> tags.
            Don't make any your text anwser only article content and what I asked inside it.
            Don't pass any unnecessery new line signs.
            Use all necessery structure tags.
            Additionally you can only use figure and figcatption tags to describe images, but you can't use article, section or div tags.
            """
        }