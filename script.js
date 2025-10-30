let students = [];

function loadStudents() {
  const storedData = localStorage.getItem('students');
  if (storedData) {
    students = JSON.parse(storedData);
    renderTable();
  }
}

function saveStudents() {
  localStorage.setItem('students', JSON.stringify(students));
}

function renderTable() {
  const tableBody = document.querySelector("#studentTable tbody");
  tableBody.innerHTML = "";

  students.forEach((student, index) => {
    const row = document.createElement("tr");
    row.innerHTML = `
      <td>${student.firstName}</td>
      <td>${student.lastName}</td>
      <td>${student.age}</td>
      <td>${student.course}</td>
      <td>
        <button onclick="editStudent(${index})">Edit</button>
        <button onclick="deleteStudent(${index})">Delete</button>
      </td>
    `;
    tableBody.appendChild(row);
  });
}

function addStudent() {
  const firstName = document.getElementById("firstName").value;
  const lastName = document.getElementById("lastName").value;
  const age = document.getElementById("age").value;
  const course = document.getElementById("course").value;

  if (!firstName || !lastName || !age || !course) {
    alert("Please fill all fields!");
    return;
  }

  students.push({ firstName, lastName, age, course });
  saveStudents();
  renderTable();
  document.querySelectorAll("input").forEach(input => input.value = "");
}

function editStudent(index) {
  const student = students[index];
  document.getElementById("firstName").value = student.firstName;
  document.getElementById("lastName").value = student.lastName;
  document.getElementById("age").value = student.age;
  document.getElementById("course").value = student.course;

  deleteStudent(index);
}

function deleteStudent(index) {
  students.splice(index, 1);
  saveStudents();
  renderTable();
}

loadStudents();
