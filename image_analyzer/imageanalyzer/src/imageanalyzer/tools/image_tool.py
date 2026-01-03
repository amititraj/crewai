import base64
from crewai.tools import BaseTool
from crewai import LLM
from config.settings import settings
from openai import OpenAI

class ImageTool(BaseTool):   
    name: str =  "analyze_image_tool"
    description: str = (
         "Analyzes an image using GPT-4o and returns a description." 
    )

    def encode_image_to_base64(self,image_path):
        with open(image_path, "rb") as f:
            image_bytes = f.read()
        return base64.b64encode(image_bytes).decode("utf-8")

    def _run(self,image_path: str) -> str:
        image_base64 = self.encode_image_to_base64(image_path)   
        client = OpenAI(api_key=settings.OPENAI_API_KEY,base_url=settings.BASE_URL)
        #llm = LLM(model=settings.MODEL,base_url=settings.BASE_URL,api_key=settings.OPENAI_API_KEY)
        #response = llm.chat(
        response = client.chat.completions.create(
            model=settings.MODEL,            
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "What does this image show?"},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{image_base64}"
                            }
                        }
                    ]
                }
            ]
        )
        print(response.choices[0].message.content)
        return response.choices[0].message.content