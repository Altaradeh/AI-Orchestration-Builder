# src/run_local.py

from ember_ai.workflows.worksheet_generator import generate_worksheet
import ember_ai.config
print ("Using OpenAI Model:", ember_ai.config.OPENAI_MODEL)
sample_input = {
    "grade_level": 3,
    "subject": "Math",
    "topic": "Multiplication and division within 100",
    "standards_or_objectives": "Solve one-step word problems involving multiplication and division.",
    "constraints": "No student personal data. Use simple language. Include answer key.",
    "worksheet_type": "Mixed practice",
    "item_count": 5,
    "difficulty": "easy",
    "time_estimate_minutes": 20,
    "tone": "supportive"
}

result = generate_worksheet(sample_input)
print(result)
