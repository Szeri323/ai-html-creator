import os
from dotenv import load_dotenv
from openai import OpenAI
from api_call import create_article, create_image

def main():
    
    try:
        load_dotenv()
        api_key = os.getenv('API_KEY')
        client = OpenAI(api_key=api_key)

        choice = int(input("Choose: Create article(1), Create images from article alt atributes(2)"))
        
        if choice == 1:
            create_article(client)
        elif choice == 2 and os.path.isfile("./artykul.html"):
           create_image(client)
        else:
            print("No action was performed.")
           
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
