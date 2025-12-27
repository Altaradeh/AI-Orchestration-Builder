def safety_layer() -> str:
    return """
SAFETY CONSTRAINTS:
- Content must be age-appropriate for the given grade level.
- Use neutral, non-authoritative language.
- Output is a draft for educator review, not final instruction.
"""
