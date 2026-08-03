import os
import json

from dotenv import load_dotenv
from groq import Groq

from app.models.financial_profile import FinancialProfile
from app.models.tax_result import TaxResult
from app.models.explanation_result import ExplanationResult

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


class ExplanationAgent:

    @staticmethod
    def explain(profile: FinancialProfile, result: TaxResult) -> ExplanationResult:

        schema = ExplanationResult.model_json_schema()

        profile_json = json.dumps(profile.model_dump(), indent=2)
        result_json = json.dumps(result.model_dump(), indent=2)

        system_prompt = f"""
            You are a friendly tax explanation assistant for Indian taxpayers.

            You will receive:
            - A FinancialProfile (income sources, deductions, taxes paid)
            - A TaxResult (computed tax figures)

            Your responsibilities:
            1. Explain the income sources present in the FinancialProfile.
            2. Explain the deductions applied and their relevant sections (80C, 80D, etc.).
            3. Explain the tax computation using the values already present in TaxResult. Do not infer or explain Indian tax laws independently.
            4. Explain the refund or tax payable amount.
            5. Use simple language suitable for a normal taxpayer.

            Rules:
            - Do NOT recalculate taxes.
            - Do NOT change or contradict any TaxResult values.
            - Do NOT give legal advice.
            - If any value is zero or missing, do not speculate why.
            - Only explain the provided data.
            - Return ONLY valid JSON matching this schema.

            Schema:
            {schema}
        """

        user_prompt = f"""
            Financial Profile:
            {profile_json}

            Tax Result:
            {result_json}
        """

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            temperature=0,
            response_format={"type": "json_object"},
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ]
        )

        return ExplanationResult.model_validate_json(
            response.choices[0].message.content
        )
