from langchain_openai import ChatOpenAI

from ember_ai.prompts.builder import build_prompt
from ember_ai.schemas import WorksheetInput, WorksheetOutput, RefusalOutput
from ember_ai.config import OPENAI_MODEL


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

    # 3. Inject structured input (no free text)
    full_prompt = (
        f"{system_prompt}\n\n"
        "INPUT (JSON):\n"
        f"{validated_input.model_dump_json()}\n\n"
        "RESPONSE:\n"
        "Return ONLY valid JSON matching the worksheet schema."
    )

    # 4. Initialize LLM (single call, stateless)
    llm = ChatOpenAI(
        model=OPENAI_MODEL,
        temperature=0.3
    )

    # 5. Invoke once
    response = llm.invoke(full_prompt)

    # 6. Validate output strictly
    try:
        return WorksheetOutput.model_validate_json(response.content)
    except Exception:
        return RefusalOutput(
            reason="invalid_output",
            message="LLM output did not match the required worksheet schema."
        )
