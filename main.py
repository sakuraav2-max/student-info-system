from flask import Flask, request, jsonify
from src.services.student_service import StudentService
from src.models.student import Student
from src.utils.logger import get_logger

app = Flask(__name__)
svc = StudentService()
logger = get_logger('student-api')

@app.route('/')
def home():
    return jsonify({"message": "Student Info System API is running!"})

@app.route('/students', methods=['GET'])
def list_students():
    try:
        return jsonify(svc.list_students()), 200
    except Exception as e:
        logger.exception("Failed to list students")
        return jsonify({"error": "internal error"}), 500

@app.route('/students', methods=['POST'])
def add_student():
    data = request.json or {}
    try:
        student = Student.create(data.get('first_name'), data.get('last_name'), data.get('age'), data.get('course'))
        created = svc.add_student(student)
        return jsonify(created), 201
    except Exception as e:
        logger.exception("Failed to add student")
        return jsonify({"error": "bad request"}), 400

@app.route('/students/<student_id>', methods=['GET'])
def get_student(student_id):
    s = svc.find_student(student_id)
    if s:
        return jsonify(s), 200
    return jsonify({"error": "not found"}), 404

@app.route('/students/<student_id>', methods=['PUT'])
def update_student(student_id):
    updates = request.json or {}
    updated = svc.update_student(student_id, updates)
    if updated:
        return jsonify(updated), 200
    return jsonify({"error": "not found"}), 404

@app.route('/students/<student_id>', methods=['DELETE'])
def delete_student(student_id):
    ok = svc.delete_student(student_id)
    if ok:
        return '', 204
    return jsonify({"error": "not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
