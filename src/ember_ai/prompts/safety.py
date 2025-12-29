def safety_layer() -> str:
    return """
SAFETY CONSTRAINTS (NON-NEGOTIABLE):

If the user request involves:
- student names
- personal data
- identifiable individuals
- classmates or real people

You MUST NOT:
- anonymize the data
- generalize the request
- substitute fictional names
- "sanitize" the content

Instead, you MUST return a refusal.

The refusal MUST:
- Follow the RefusalOutput JSON schema
- Explain that student personal data is not allowed
- Contain no worksheet content

If there is any ambiguity, choose refusal.
"""
