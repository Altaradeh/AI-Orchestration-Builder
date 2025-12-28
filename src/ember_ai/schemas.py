from pydantic import BaseModel, Field
from typing import List, Optional


class WorksheetInput(BaseModel):
    grade_level: int = Field(..., gt=0)
    subject: str
    topic: str
    standards_or_objectives: str
    constraints: str
    worksheet_type: str
    item_count: int = Field(..., gt=0)
    difficulty: str
    time_estimate_minutes: int = Field(..., gt=0)
    tone: str


class WorksheetItem(BaseModel):
    id: str
    question: str
    answer: str
    work_hint: Optional[str] = None


class WorksheetSection(BaseModel):
    title: str
    type: str
    items: List[WorksheetItem]


class WorksheetMetadata(BaseModel):
    grade_level: str
    subject: str
    topic: str
    difficulty: str
    time_estimate_minutes: int
    instructions_for_students: str


class SafetyNotes(BaseModel):
    student_data: str
    human_in_loop: str

class AnswerKeyItem(BaseModel):
    id: str
    correct_answer: str
    
class WorksheetOutput(BaseModel):
    metadata: WorksheetMetadata
    sections: List[WorksheetSection]
    answer_key: List[AnswerKeyItem]
    safety_notes: SafetyNotes

class RefusalOutput(BaseModel):
    reason: str
    message: str

