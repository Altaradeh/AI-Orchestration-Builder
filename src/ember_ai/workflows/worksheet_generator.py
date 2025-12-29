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

    schema_description = f"""
    You MUST output valid JSON matching EXACTLY ONE of the following schemas.
    IMPORTANT:
        - Do NOT wrap the output in "WorksheetOutput" or "RefusalOutput"
        - The JSON object itself must match the schema fields directly
        WorksheetOutput schema:
        {WorksheetOutput.model_json_schema()}

        RefusalOutput schema:
        {RefusalOutput.model_json_schema()}
                                                    """
    # 3. Inject structured input (no free text)
    full_prompt = (
    f"{system_prompt}\n\n"
    f"Return ONLY the JSON object. No outer keys. No commentary.\n\n"
    f"{schema_description}\n\n"
    "INPUT (JSON):\n"
    f"{validated_input.model_dump_json()}\n\n"
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
        return WorksheetOutput.model_validate_json(raw_output),raw_output
    except Exception:
        return RefusalOutput.model_validate_json(raw_output),raw_output