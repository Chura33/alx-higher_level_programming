#!/usr/bin/node

let row = '';
const num = parseInt(process.argv[2]);
if (isNaN(num)) {
  console.log('Missing size');
} else if (!isNaN(num)) {
  for (let i = 0; i < num; i++) {
    for (let j = 0; j < num; j++) {
      row += 'x';
    }
    console.log(row);
	row = '';
  }
}
