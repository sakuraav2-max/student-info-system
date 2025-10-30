import json
from pathlib import Path
from typing import List, Optional, Dict
from src.models.student import Student
from src.utils.logger import get_logger

logger = get_logger('StudentService')
DATA_FILE = Path(__file__).resolve().parents[2] / 'data' / 'students.json'

class StudentService:
    def __init__(self, data_file: Path = None):
        self.data_file = Path(data_file) if data_file else DATA_FILE
        self.data_file.parent.mkdir(parents=True, exist_ok=True)
        if not self.data_file.exists():
            self._write_data([])

    def _read_data(self) -> List[Dict]:
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            logger.warning("Data file missing or invalid; returning empty list")
            return []
        except Exception:
            logger.exception("Unexpected error reading data file")
            return []

    def _write_data(self, data: List[Dict]):
        try:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2)
        except Exception:
            logger.exception("Failed to write data to file")
            raise

    def list_students(self) -> List[Dict]:
        return self._read_data()

    def add_student(self, student: Student) -> Dict:
        data = self._read_data()
        data.append(student.to_dict())
        self._write_data(data)
        return student.to_dict()

    def find_student(self, student_id: str) -> Optional[Dict]:
        for s in self._read_data():
            if s.get('id') == student_id:
                return s
        return None

    def update_student(self, student_id: str, updates: Dict) -> Optional[Dict]:
        data = self._read_data()
        for i, s in enumerate(data):
            if s.get('id') == student_id:
                s.update({k: v for k, v in updates.items() if v is not None})
                data[i] = s
                self._write_data(data)
                return s
        return None

    def delete_student(self, student_id: str) -> bool:
        data = self._read_data()
        new_data = [s for s in data if s.get('id') != student_id]
        if len(new_data) == len(data):
            return False
        self._write_data(new_data)
        return True
