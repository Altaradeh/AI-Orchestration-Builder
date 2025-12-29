from ember_ai.workflows.worksheet_generator import generate_worksheet
from ember_ai.workflows.save_worksheet import save_worksheet
from ember_ai.schemas import RefusalOutput, WorksheetOutput
# -----------------------------
# Simulated educator input
# -----------------------------
VALID_INPUT = {
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

REFUSAL_INPUT = {
    "grade_level": 3,
    "subject": "Math",
    "topic": "Multiplication using student names and personal data",
    "standards_or_objectives": "Students will practice multiplication using their classmates’ names.",
    "constraints": "Include student names and personal details.",# This should trigger refusal
    "worksheet_type": "Mixed practice",
    "item_count": 5,
    "difficulty": "easy",
    "time_estimate_minutes": 20,
    "tone": "supportive"
}


# -----------------------------
# Step 1: Generate worksheet
# -----------------------------

print("\n--- GENERATED WORKSHEET ---")

result,raw_json = generate_worksheet(VALID_INPUT)

print("\n--- RAW LLM OUTPUT ---")
print(raw_json)

# -----------------------------
# Simulate Refusal
# -----------------------------
if isinstance(result,RefusalOutput):
    exit()


# -----------------------------
# Step 2: Simulate opt-in save
# -----------------------------

CONSENT_TO_SAVE = False  # change to False to test opt-out
USER_ID = "11111111-1111-1111-1111-111111111111"  # fake UUID for local test
save_result = save_worksheet(
    user_id=USER_ID,
    worksheet=result,
    consent=CONSENT_TO_SAVE
)

print("\n--- SAVE RESULT ---")
print(save_result)
