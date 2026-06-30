from google import genai
from dotenv import load_dotenv
import os
load_dotenv()

client = genai.Client(api_key=os.getenv("api_key"))


def ask_gemini(prompt):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=(
                "u are manav who speaks hindi,gujrati as well as english."
                "u analyze chat history and respond like manav "
                "use emoji when needed"
                "u respond in only one language english but u can write hindi and gujrati in english "
                "dont add extra word "
                "u dont give ans in all three language answer in language which other side is speaking"
                f"User: {prompt}"
            )
        )

        return response.text

    except Exception as e:
        return f"Sorry, I encountered an error: {e}"