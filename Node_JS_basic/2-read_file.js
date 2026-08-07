const fs = require('fs');

function countStudents(path) {
  let data;
  try {
    data = fs.readFileSync(path, 'utf-8');
  } catch (err) {
    throw new Error('Cannot load the database');
  }

  const lines = data.split('\n').filter((line) => line.trim() !== '');
  const students = lines.slice(1);

  const fields = {};

  students.forEach((line) => {
    const parts = line.split(',');
    const firstname = parts[0];
    const field = parts[parts.length - 1];

    if (!fields[field]) {
      fields[field] = [];
    }
    fields[field].push(firstname);
  });

  console.log(`Number of students: ${students.length}`);

  Object.keys(fields).forEach((field) => {
    const list = fields[field];
    console.log(`Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`);
  });
}

module.exports = countStudents;
