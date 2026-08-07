const fs = require('fs');

const readDatabase = (path) => new Promise((resolve, reject) => {
  fs.readFile(path, 'utf-8', (err, data) => {
    if (err) {
      reject(err);
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

    resolve(fields);
  });
});

module.exports = readDatabase;
