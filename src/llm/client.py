import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

class StarCoderClient:
    # Manages interaction with Groq API for code explanation.

    def __init__(self):
        self.api_token = os.getenv("GROQ_API_KEY")
        self.model_id = os.getenv("GROQ_MODEL")

        if not self.api_token:
            raise ValueError("GROQ_API_KEY not found in .env file")

        self.client = Groq(api_key=self.api_token)

    def generate_explanation(self, prompt: str) -> str:
        # Sends the prompt to Groq API and retrieves the generated text.
        # Args:
        #     prompt (str): The complete prompt with RTCCF framework
        # Returns:
        #     str: Generated explanation or error message
        try:
            message = self.client.chat.completions.create(
                model=self.model_id,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=0.2,  # Low creativity for factual accuracy
                max_tokens=150,  
                top_p=0.9,
            )
            return message.choices[0].message.content
        except Exception as e:
            return f"Error connecting to AI service: {str(e)}"
