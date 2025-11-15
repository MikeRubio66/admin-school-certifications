from pydantic import BaseModel
class CourseCreate(BaseModel):
    title: str
    description: str

class CourseOut(CourseCreate):
    id: int
