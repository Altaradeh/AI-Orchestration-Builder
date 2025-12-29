def rules_layer() -> str:
    return """
SYSTEM RULES (NON-OVERRIDABLE):

You may only produce one of the following outputs:
1. A valid WorksheetOutput JSON
2. A valid RefusalOutput JSON

Never mix the two.
Never explain outside JSON.
"""
