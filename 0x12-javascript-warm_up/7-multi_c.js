#!/usr/bin/node

const num = parseInt(process.argv[2]);

if (!num) {
  console.log('Missing number of occurrences');
}
for (let i = 0; i < num; i++) {
  console.log('c is fun');
}
