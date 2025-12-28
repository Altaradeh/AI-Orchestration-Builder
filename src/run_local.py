from ember_ai.workflows.worksheet_generator import generate_worksheet
from ember_ai.workflows.save_worksheet import save_worksheet

# -----------------------------
# Simulated educator input
# -----------------------------
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

# -----------------------------
# Step 1: Generate worksheet
# -----------------------------
result = generate_worksheet(sample_input)
print("\n--- GENERATED WORKSHEET ---")
print(result)

# -----------------------------
# Step 2: Simulate opt-in save
# -----------------------------
USER_ID = "11111111-1111-1111-1111-111111111111"  # fake UUID for local test
CONSENT_TO_SAVE = True  # change to False to test opt-out

save_result = save_worksheet(
    user_id=USER_ID,
    worksheet=result,
    consent=CONSENT_TO_SAVE
)

print("\n--- SAVE RESULT ---")
print(save_result)
