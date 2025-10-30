from dataclasses import dataclass, asdict
import uuid
from typing import Optional

@dataclass
class Student:
    id: str
    first_name: str
    last_name: str
    age: Optional[int] = None
    course: Optional[str] = None

    @staticmethod
    def create(first_name: str, last_name: str, age: int = None, course: str = None):
        return Student(
            id=str(uuid.uuid4()),
            first_name=first_name or "",
            last_name=last_name or "",
            age=age,
            course=course
        )

    def to_dict(self):
        return asdict(self)
