const http = require('http');
const fs = require('fs');

const DB_FILE = process.argv[2];

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
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

      const output = [];
      output.push(`Number of students: ${students.length}`);

      Object.keys(fields).forEach((field) => {
        const list = fields[field];
        output.push(`Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`);
      });

      resolve(output.join('\n'));
    });
  });
}

const app = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    countStudents(DB_FILE)
      .then((report) => {
        res.end(`This is the list of our students\n${report}`);
      })
      .catch((err) => {
        res.end(`This is the list of our students\n${err.message}`);
      });
  } else {
    res.statusCode = 404;
    res.end('Not found');
  }
});

app.listen(1245);

module.exports = app;
