#!/usr/bin/node

const num = parseInt(process.argv[2]);

if (!isNaN(num)) {
  for (let i = 0; i < num; i++) {
    for (let j = 0; j < num; j++) {
      process.stdout.write('x');
    }
    process.stdout.write('\n');
  }
} else {
  console.log('Missing size');
}
