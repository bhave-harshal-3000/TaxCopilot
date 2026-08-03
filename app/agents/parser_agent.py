import os

from dotenv import load_dotenv
from groq import Groq

from app.models.form16_data import Form16Data
from app.services.pdf_service import PDFService
from app.models.document_registry import DOCUMENT_SCHEMAS

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


class ParserAgent:

    @staticmethod
    def parse(filepath: str, document_type: str):

        text = PDFService.extract_text(filepath)

        print(text) #debugging
        
        schema_class = DOCUMENT_SCHEMAS[document_type]
        schema = schema_class.model_json_schema()

        system_prompt = f"""
            You are an expert parser for Indian Income Tax documents.
            Your task is to extract structured information.
            Return ONLY a valid JSON object.
            The JSON MUST strictly follow this schema:

            {schema}

            Rules:
            - Do not invent values.
            - If a field is missing, return null.
            - Do not return markdown.
            - Do not explain anything.
            - Output only JSON.
        """
        #end of prompt

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            temperature=0,
            response_format={
                "type": "json_object"
            },
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": text
                }
            ]
        )
        
        print(response.choices[0].message.content) #debugging
        
        try:
            parsed = schema_class.model_validate_json(response.choices[0].message.content)
            return parsed

        except Exception as e:
            print(e)
            raise
    
    