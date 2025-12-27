from ember_ai.prompts.rules import rules_layer
from ember_ai.prompts.safety import safety_layer
from ember_ai.prompts.task import task_layer
from ember_ai.prompts.tone import tone_layer


def build_prompt(tone: str) -> str:
    """
    Builds the full prompt with hard-enforced ordering.
    """
    return "\n".join([
        rules_layer(),
        safety_layer(),
        task_layer(),
        tone_layer(tone)
    ])
