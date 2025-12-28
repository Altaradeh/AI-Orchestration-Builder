from ember_ai.supabase_client import supabase
from ember_ai.schemas import WorksheetOutput


def save_worksheet(
    *,
    user_id: str,
    worksheet: WorksheetOutput,
    consent: bool
):
    if not consent:
        return {"status": "skipped", "reason": "user_did_not_consent"}

    payload = {
        "user_id": user_id,
        "worksheet": worksheet.model_dump()
    }

    #result = supabase.table("worksheet_outputs").insert(payload).execute()
    result = supabase.rpc(
    "insert_worksheet_output",
    {
        "p_user_id": user_id,
        "p_worksheet": worksheet.model_dump()
    }
).execute()

    return {"status": "saved"}
