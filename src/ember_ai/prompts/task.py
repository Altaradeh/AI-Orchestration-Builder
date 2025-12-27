def task_layer() -> str:
    return """
TASK:
Generate an educator worksheet based strictly on the provided inputs.
Include:
- Metadata
- Worksheet sections with questions
- Answer key
- Safety notes

Follow item_count, worksheet_type, difficulty, and constraints exactly.
Do not assume information not provided.
"""
