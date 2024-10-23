from dotenv import load_dotenv 
from os import environ
import google.generativeai as genai
from google.generativeai.types.generation_types import GenerateContentResponse

try:
    from gemini import GEMINI_API_KEY
except ImportError:
    from tools.gemini import GEMINI_API_KEY


class GeminiClient:
    def __init__(self):
        
        self.client = genai.GenerativeModel('models/gemini-pro')
        
    def make_prompt(self, query: str, context: str, level:int=1) -> str:
        """Creates a prompt suitable for the model, alongside the given context.

        Args:
            query (str): The question being asked.
            context (str): The context for the model to use when generating.
            level (int): The level of the prompt, from 1 (basic) to 3 (advanced)

        Returns:
            str: The prompt to be used for the model
        """
        
        formatted_context:str = context.replace("'", "").replace('"', "")
        
        prompt:str = f"question: {query}.\n"
        
        match level:
            case 3:
                prompt += f"""Supplementary Context : \n{formatted_context}\n 
                Note: If the question is not related to the context, please start your response with 'OUT OF CONTEXT', and then use your knowledge to attempt to answer the question briefly."""
                
            case 2:
                prompt += f"""Supplementary Context : \n {formatted_context}\n
                Note: If the question is not related to the context, please respond with 'OUT OF CONTEXT'."""
            case _:
                pass
            
        return prompt + "\n Your Response : "
    
    def prompt_model(self, prompt:str) -> str:
        """Prompts the gemini model, and returns the response text.

        Args:
            prompt (str): The prompt, ideally created from make_prompt.

        Returns:
            str: The response from the model.
        """
        
        model_response: GenerateContentResponse = self.client.generate_content(contents=prompt)
        return model_response.text