from langchain_openai import ChatOpenAI

from ember_ai.prompts.builder import build_prompt
from ember_ai.schemas import WorksheetInput, WorksheetOutput, RefusalOutput
from ember_ai.config import OPENAI_MODEL
import warnings

warnings.filterwarnings(
    "ignore",
    message=".*response_format is not default parameter.*"
)

def generate_worksheet(input_data: dict):
    # 1. Validate input
    try:
        validated_input = WorksheetInput(**input_data)
    except Exception as e:
        return RefusalOutput(
            reason="invalid_input",
            message=str(e)
        )

    # 2. Build full prompt (rules → safety → task → tone)
    system_prompt = build_prompt(validated_input.tone)
    schema_description = WorksheetOutput.model_json_schema()
    # 3. Inject structured input (no free text)
    full_prompt = (
    f"{system_prompt}\n\n"
    "You MUST return JSON matching this schema:\n"
    f"{schema_description}\n\n"
    "INPUT (JSON):\n"
    f"{validated_input.model_dump_json()}\n\n"
    "Return ONLY valid JSON. No commentary."
    )

    # 4. Initialize LLM (single call, stateless)
    llm = ChatOpenAI(
        model=OPENAI_MODEL,
        temperature=0.3,
        response_format={"type": "json_object"},
    )

    # 5. Invoke once
    response = llm.invoke(full_prompt)

    # 6. Validate output strictly
    raw_output = response.content

    try:
        return WorksheetOutput.model_validate_json(raw_output)
    except Exception as first_error:
        # One repair attempt
        repair_prompt = (
            "The previous output did not match the required JSON schema.\n"
            "Fix the JSON to exactly match the schema. Do not change content meaning.\n\n"
            f"SCHEMA:\n{WorksheetOutput.model_json_schema()}\n\n"
            f"INVALID JSON:\n{raw_output}"
        )

        repair_response = llm.invoke(repair_prompt)

        try:
            return WorksheetOutput.model_validate_json(repair_response.content)
        except Exception:
            return RefusalOutput(
                reason="invalid_output",
                message="LLM output could not be coerced into the required schema."
            )
