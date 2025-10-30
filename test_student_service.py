from src.services.student_service import StudentService
from src.models.student import Student
from pathlib import Path
import tempfile

def test_add_and_find_student():
    with tempfile.TemporaryDirectory() as tmpdir:
        data_path = Path(tmpdir) / "students.json"
        svc = StudentService(data_path)
        s = Student.create("Test", "User", 18, "BSIT")
        svc.add_student(s)
        found = svc.find_student(s.id)
        assert found['first_name'] == "Test"
